from datetime import date, datetime

from django import template
from django.views import View
from django.db.models import Q
from django.urls import reverse
from django.template import loader
from django.shortcuts import redirect
from django.http import JsonResponse, QueryDict
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from dashboard.utils import is_ajax, form_validation_error, delete_image
from facerec.models import ModelWajah
from presensi.utils import save_image
from presensi.models import Jabatan, Pegawai, Presensi, Shift
from presensi.forms import JabatanForm, PegawaiForm, ShiftForm

@login_required(login_url='/login/')
def index(request):
    today = date.today()
    presensi = Presensi.objects.all().filter(tanggal=today)
    context = {
        'nav': 'dashboard',
        'hadir': presensi.filter(Q(keterangan='Hadir') | Q(keterangan='Telat')).count(),
        'pegawai': Pegawai.objects.all().count(),
        'izin': presensi.filter(Q(keterangan='Izin') | Q(keterangan='Sakit')).count()
    }
    context['absen'] = context['pegawai'] - context['hadir'] - context['izin']
    context.update(dict(Pegawai.total_info()))
    context['model'] = ModelWajah.objects.get(id=1)
    context['data'] = presensi.order_by('-id')[:5]
    html_template = loader.get_template('pages/dashboard.html')
    return HttpResponse(html_template.render(context, request))

@method_decorator(login_required(login_url='login'), name='dispatch')
class PegawaiView(View):
    context = {}

    def get(self, request, pk=None, action=None):
        path = request.get_full_path()

        if not pk:
            pegawai = Pegawai.objects.all()
            context = {
                'nav': 'pegawai',
                'data': pegawai,
            }
            html_template = loader.get_template('pages/pegawai.html')
            return HttpResponse(html_template.render(context, request))

        if 'masuk' in path or 'izin' in path or 'alfa' in path:
            print(pk)
            pk = int(path.split('/')[2])
            print(pk)
            pegawai = self.get_object(pk)
            today = date.today()
            now = datetime.now().time()
            if 'masuk' in path:
                ket = 'Hadir'
            elif 'izin' in path:
                ket = 'Izin'
            elif 'alfa' in path:
                ket = 'Tidak Hadir'
            Presensi(
                pegawai = pegawai,
                tanggal = today,
                masuk = now,
                pulang = datetime.strptime('00:00', '%H:%M'),
                keterangan = ket,
            ).save()
            return redirect('izin')

        if '/delete/confirm' in path:
            pk = int(path.split('/')[2])
            response = {'valid': 'success', 'message': 'Berhasil menghapus data.'}
            self.delete(pk)
            return JsonResponse(response)

        if is_ajax(request):
            if 'delete' in path:
                self.context['template'] = self.get_del_modal(pk)
            else:
                self.context['template'] = self.get_create_form(pk)

        return JsonResponse(self.context)
    
    def put(self, request, pk=None, action=None):
        id_ = self.get_object(pk)
        form = PegawaiForm(QueryDict(request.body), instance=id_)
        if form.is_valid():
            form.save()
            response = {'valid': 'success', 'message': 'Berhasil memperbarui data.'}
        else:
            response = {'valid': 'error', 'message': form_validation_error(form)}
        return JsonResponse(response)

    def delete(self, pk=None):
        data = Pegawai.objects.get(id=pk)
        data.delete()
        delete_image(data.nama)
        return redirect('pegawai')
        
    def get_create_form(self, pk=None):
        form = PegawaiForm()
        if pk:
            form = PegawaiForm(instance=self.get_object(pk))
        return render_to_string('partial/modal_form.html', {'form': form, 'data': 'pegawai'})
    
    def get_del_modal(self, pk=None):
        id_ = pk
        if pk:
            id_ = self.get_object(pk)
        return render_to_string('partial/modal_del.html', {'data': id_, 'page': 'pegawai'})

    def get_object(self, pk):
        return Pegawai.objects.get(id=pk)

# @login_required(login_url='/login/')
# def pegawai_view(request):
#     pegawai = Pegawai.objects.all()
#     context = {
#         'nav': 'pegawai',
#         'data': pegawai,
#     }
#     html_template = loader.get_template('pages/pegawai.html')
#     return HttpResponse(html_template.render(context, request))

# @login_required(login_url='/login/')
# def pegawaidetail_view(request, pk=None):
#     print(request, pk)
#     return redirect('pegawai')
    # html_template = loader.get_template('pages/pegawai.html')
    # return HttpResponse(html_template.render(request))

@method_decorator(login_required(login_url='login'), name='dispatch')
class JabatanView(View):
    context = {}

    def get(self, request, pk=None, action=None):
        path = request.get_full_path()

        if '/delete/confirm' in path:
            pk = int(path.split('/')[2])
            response = {'valid': 'success', 'message': 'Berhasil menghapus data.'}
            self.delete(pk)
            return JsonResponse(response)
        
        if is_ajax(request):            
            if 'delete' in path:
                self.context['template'] = self.get_del_modal(pk)
            else:
                self.context['template'] = self.get_create_form(pk)
        
        if not pk:
            form = JabatanForm()
            jabatan = Jabatan.objects.all()
            context = {
                'nav': 'jabatan',
                'data': jabatan,
                'form': form
            }
            html_template = loader.get_template('pages/jabatan.html')
            return HttpResponse(html_template.render(context, request))

        return JsonResponse(self.context)
    
    def post(self, request, pk=None, action=None):
        form = JabatanForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('jabatan')
        
    def put(self, request, pk=None, action=None):
        id_ = self.get_object(pk)
        form = JabatanForm(QueryDict(request.body), instance=id_)
        if form.is_valid():
            form.save()
            response = {'valid': 'success', 'message': 'Berhasil memperbarui data.'}
        else:
            response = {'valid': 'error', 'message': form_validation_error(form)}
        return JsonResponse(response)

    def delete(self, pk=None):
        data = Jabatan.objects.get(id=pk)
        data.delete()
        return redirect('jabatan')

    def get_create_form(self, pk=None):
        form = JabatanForm()
        if pk:
            form = JabatanForm(instance=self.get_object(pk))
        print(form)
        return render_to_string('partial/modal_form.html', {'form': form, 'data': 'jabatan'})
    
    def get_del_modal(self, pk=None):
        id_ = pk
        if pk:
            id_ = self.get_object(pk)
        return render_to_string('partial/modal_del.html', {'data': id_, 'page': 'jabatan'})

    def get_object(self, pk):
        data = Jabatan.objects.get(id=pk)
        return data
    
# @login_required(login_url='/login/')
# def jabatan_view(request):
    # form = JabatanForm()
    # jabatan = Jabatan.objects.all()
    # context = {
    #     'nav': 'jabatan',
    #     'data': jabatan,
    #     'form': form
    # }
    # html_template = loader.get_template('pages/jabatan.html')
    # return HttpResponse(html_template.render(context, request))

@login_required(login_url='/login/')
def tambah_view(request):
    form = PegawaiForm()
    context = {
        'nav': 'tambah',
        'form': form
    }
    if request.method == 'POST':
        form = PegawaiForm(request.POST)
        files = request.FILES.getlist('foto')
        if form.is_valid():
            nama = form.cleaned_data['nama']
            save_image(nama, files)
            obj = form.save(commit=False)
            obj.foto = f'{nama}/'
            obj.save()
            return redirect('pegawai')

    html_template = loader.get_template('pages/tambah.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url='/login/')
def presensi_view(request):
    today = date.today()
    params = request.GET
    tgl = datetime.strptime(params.get('date'), '%d-%m-%Y').date() if params.get('date') else today
    presensi = Presensi.objects.all().filter(tanggal=tgl)
    
    context = {
        'nav': 'presensi',
        'data': presensi,
        'tanggal': tgl.strftime('%d-%m-%Y')
    }
    html_template = loader.get_template('pages/presensi.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url='/login/')
def kelolaizin_view(request):
    today = date.today()
    params = request.GET
    tgl = datetime.strptime(params.get('date'), '%d-%m-%Y').date() if params.get('date') else today
    pegawai = Pegawai.objects.exclude(presensi__tanggal=tgl)

    context = {
        'nav': 'izin',
        'data': pegawai,
        'tanggal': tgl.strftime('%d-%m-%Y')
    }
    html_template = loader.get_template('pages/izin.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url='/login/')
def shift_view(request):
    form = ShiftForm()
    shift = Shift.objects.all()
    context = {
        'nav': 'shift',
        'shifts': shift,
        'form': form
    }
    
    if request.method == 'POST':
        sh = Shift.objects.filter(id_shift=request.POST['id_shift']).values_list('id', flat=True)
        if sh.exists():
            ids = Shift.objects.get(id=int(sh[0]))
            form = ShiftForm(request.POST, instance=ids)
            if form.is_valid():
                form.save()
        else:
            form = ShiftForm(request.POST or None)
            if form.is_valid():
                form.save()

    html_template = loader.get_template('pages/shift.html')
    return HttpResponse(html_template.render(context, request))

def pages(request):
    context = {}

    try:
        load_template = request.path.split('/')[-1]
        
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        elif load_template == ' ':
            return HttpResponseRedirect(reverse('index'))

        html_template = loader.get_template('pages/' + load_template)
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))