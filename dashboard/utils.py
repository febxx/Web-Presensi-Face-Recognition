import os
import math
from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage

from facerec.main import predict
from web.settings import MEDIA_ROOT

dir_pegawai = os.path.join(MEDIA_ROOT, 'pegawai')
dir_presensi = os.path.join(MEDIA_ROOT, 'presensi')

def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def delete_image(name):
    path = os.path.join(dir_pegawai, name)
    isExist = os.path.exists(path)
    if isExist:
        for image in os.listdir(path):
            imgpath = os.path.join(path, image)
            os.remove(imgpath)
        os.rmdir(path)

def set_pagination(request, items, item_number=5):
    if not items:
        return False, 'These is no items'
    
    params = request.GET
    item_len = len(items)
    page = int(params.get('page')) if 'page' in params else 1
    pages_number = math.ceil(item_len/item_number)
    if page > pages_number or page <= 0:
        return False, 'Page not found'
    
    paginator = Paginator(items, item_number)
    items = paginator.get_page(page)

    url_params = dict()
    for key in params:
        if key != 'page':
            url_params[key] = params[key]
    page_range = None
    if page in range(1, 7) and pages_number >= 7:
        page_range = [i for i in range(1, 8)]
        page_range += ['...']
    elif page >= 7 and (page + 6) < pages_number:
        page_range = ['...']
        page_range += [i for i in range(page - 3, page + 4)]
        page_range += ['...']
    elif page in range(pages_number - 7 if pages_number - 7 > 0 else 1, pages_number + 1):
        page_range = ['...'] if pages_number - 7 > 0 else []
        page_range += [i for i in range(pages_number - 7 if pages_number - 7 > 0 else 1, pages_number + 1)]
    
    context = dict(items=items, page_range=page_range, last=pages_number, url_params=urlencode(url_params))
    items.pagination = render_to_string('partial/pagination.html', context)
    return items, {'current_page': page, 'items': item_len, 'items_on_page': item_number}