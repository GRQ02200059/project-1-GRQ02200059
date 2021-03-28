from django.template.defaulttags import url
from django.urls import path, re_path

from . import views
from . import util
from random import choice

urlpatterns = [ path("", views.index, name="index"),
path('edit/<entry><edited>',views.edited,name="edited")
,
    path('detail/<title>', views.edit, name="edit"),
    path("index/", views.index, name="index"),
    path("random/", views.random, name="random"),
path("search/", views.search, name="search"),

    path("create_np/",views.create_np,name="create_np"),

path("get_np/", views.get_np, name="get_np")
    ,path('<entry>', views.detail, name="detail"),



]
# for item in util.list_entries():
#     path(item,views.)