from django.views import View
from django.shortcuts import redirect
from django.http import JsonResponse, QueryDict
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from presensi.models import Jabatan, Pegawai, Shift, Order
from presensi.forms import JabatanForm, PegawaiForm, ShiftForm, OrderForm

# @method_decorator(login_required(login_url='login'), name='dispatch')
# class PegawaiView(View):
#     context = {}

#     def get(self, request, pk=None, action=None):
#         path = request.get_full_path()
#         if '/delete/confirm' in path:
#             pk = int(path.split('/')[2])
#             response = {'valid': 'success', 'message': 'Berhasil menghapus data.'}
#             self.delete(pk)
#             return JsonResponse(response)

#         if is_ajax(request):
#             if 'delete' in path:
#                 self.context['template'] = self.get_del_modal(pk)
#             else:
#                 self.context['template'] = self.get_create_form(pk)
#         return JsonResponse(self.context)
    
#     def put(self, request, pk=None, action=None):
#         id_ = self.get_object(pk)
#         form = PegawaiForm(QueryDict(request.body), instance=id_)
#         if form.is_valid():
#             form.save()
#             response = {'valid': 'success', 'message': 'Berhasil memperbarui data.'}
#         else:
#             response = {'valid': 'error', 'message': form_validation_error(form)}
#         return JsonResponse(response)

#     def delete(self, pk=None):
#         data = Pegawai.objects.get(id=pk)
#         data.delete()
#         delete_image(data.nama)
#         return redirect('pegawai')
        
#     def get_create_form(self, pk=None):
#         form = PegawaiForm()
#         if pk:
#             form = PegawaiForm(instance=self.get_object(pk))
#         return render_to_string('partial/modal_form.html', {'form': form, 'data': 'employee'})
    
#     def get_del_modal(self, pk=None):
#         id_ = pk
#         if pk:
#             id_ = self.get_object(pk)
#         return render_to_string('partial/modal_del.html', {'data': id_, 'page': 'employee'})

#     def get_object(self, pk):
#         return Pegawai.objects.get(id=pk)

# @method_decorator(login_required(login_url='login'), name='dispatch')
# class ShiftView(View):
#     context = {}
    
#     def get(self, request, pk=None, action=None):
#         path = request.get_full_path()
#         if '/delete/confirm' in path:
#             pk = int(path.split('/')[2])
#             response = {'valid': 'success', 'message': 'Berhasil menghapus data.'}
#             self.delete(pk)
#             return JsonResponse(response)

#         if is_ajax(request):            
#             if 'delete' in path:
#                 self.context['template'] = self.get_del_modal(pk)
#             else:
#                 self.context['template'] = self.get_create_form(pk)
#         return JsonResponse(self.context)
    
#     def post(self, request, pk=None, action=None):
#         form = ShiftForm(request.POST)
#         if form.is_valid():
#             form.save()
#             response = {'valid': 'success', 'message': 'Berhasil menambahkan data.'}
#         else:
#             response = {'valid': 'error', 'message': form_validation_error(form)}
#         return JsonResponse(response)
    
#     def put(self, request, pk=None, action=None):
#         id_ = self.get_object(pk)
#         form = ShiftForm(QueryDict(request.body), instance=id_)
#         if form.is_valid():
#             form.save()
#             response = {'valid': 'success', 'message': 'Berhasil memperbarui data.'}
#         else:
#             response = {'valid': 'error', 'message': form_validation_error(form)}
#         return JsonResponse(response)

#     def delete(self, pk=None):
#         shift = Shift.objects.get(id=pk)
#         shift.delete()
#         return redirect('shift')
        
#     def get_create_form(self, pk=None):
#         form = ShiftForm()
#         if pk:
#             form = ShiftForm(instance=self.get_object(pk))
#         return render_to_string('partial/modal_form.html', {'form': form, 'data': 'shifts'})
    
#     def get_del_modal(self, pk=None):
#         id_ = pk
#         if pk:
#             id_ = self.get_object(pk)
#         return render_to_string('partial/modal_del.html', {'data': id_, 'page': 'shifts'})

#     def get_object(self, pk):
#         shift = Shift.objects.get(id=pk)
#         return shift


# @method_decorator(login_required(login_url='login'), name='dispatch')
# class JabatanView(View):
#     context = {}

#     def get(self, request, pk=None, action=None):
#         path = request.get_full_path()
#         if '/delete/confirm' in path:
#             pk = int(path.split('/')[2])
#             response = {'valid': 'success', 'message': 'Berhasil menghapus data.'}
#             self.delete(pk)
#             return JsonResponse(response)

#         if is_ajax(request):            
#             if 'delete' in path:
#                 self.context['template'] = self.get_del_modal(pk)
#             else:
#                 self.context['template'] = self.get_create_form(pk)
#         return JsonResponse(self.context)
    
#     def post(self, request, pk=None, action=None):
#         form = JabatanForm(request.POST)
#         if form.is_valid():
#             form.save()
#             response = {'valid': 'success', 'message': 'Berhasil menambahkan data.'}
#         else:
#             response = {'valid': 'error', 'message': form_validation_error(form)}
#         return JsonResponse(response)

#     def put(self, request, pk=None, action=None):
#         id_ = self.get_object(pk)
#         form = JabatanForm(QueryDict(request.body), instance=id_)
#         if form.is_valid():
#             form.save()
#             response = {'valid': 'success', 'message': 'Berhasil memperbarui data.'}
#         else:
#             response = {'valid': 'error', 'message': form_validation_error(form)}
#         return JsonResponse(response)

#     def delete(self, pk=None):
#         data = Jabatan.objects.get(id=pk)
#         data.delete()
#         return redirect('jabatan')

#     def get_create_form(self, pk=None):
#         form = JabatanForm()
#         if pk:
#             form = JabatanForm(instance=self.get_object(pk))
#         return render_to_string('partial/modal_form.html', {'form': form, 'data': 'office'})
    
#     def get_del_modal(self, pk=None):
#         id_ = pk
#         if pk:
#             id_ = self.get_object(pk)
#         return render_to_string('partial/modal_del.html', {'data': id_, 'page': 'office'})

#     def get_object(self, pk):
#         data = Jabatan.objects.get(id=pk)
#         return data
    

# @method_decorator(login_required(login_url='login'), name='dispatch')
# class OrderView(View):
#     context = {}

#     def get(self, request, pk=None, action=None):
#         if is_ajax(request):
#             self.context['template'] = self.get_create_form(pk)

#         return JsonResponse(self.context)

#     def post(self, request, pk=None, action=None):
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             item = render_to_string('partial/row_item.html', {'order': order})

#             response = {'valid': 'success', 'message': 'order created successfully.', 'item': item}
#         else:
#             response = {'valid': 'error', 'message': form_validation_error(form)}
#         return JsonResponse(response)

#     def put(self, request, pk=None, action=None):
#         order = self.get_object(pk)
#         form = OrderForm(QueryDict(request.body), instance=order)
#         if form.is_valid():
#             order = form.save()
#             item = render_to_string('partial/row_item.html', {'order': order})

#             response = {'valid': 'success', 'message': 'order updated successfully.', 'item': item}
#         else:
#             response = {'valid': 'error', 'message': form_validation_error(form)}

#         return JsonResponse(response)

#     def get_create_form(self, pk=None):
#         form = OrderForm()
#         if pk:
#             form = OrderForm(instance=self.get_object(pk))
#         return render_to_string('partial/modal_form.html', {'form': form, 'data': 'orders'})

#     def get_object(self, pk):
#         order = Order.objects.get(id=pk)
#         return order