from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('train/', train_view, name='train'),
    # re_path(r'^.*\.*', pages, name='pages'),
]