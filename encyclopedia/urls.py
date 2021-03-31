from django.template.defaulttags import url
from django.urls import path, re_path

from . import views
from . import util
from random import choice

urlpatterns = [ path("", views.index, name="index"),

    path('<title>', views.edit, name="edit"),
path('edit/<str:entry>',views.edited,name="edited"),

    path("index/", views.index, name="index"),
    path("random/", views.random, name="random"),
path("search/", views.search, name="search"),

    path("create_np/",views.create_np,name="create_np"),

path("get_np/", views.get_np, name="get_np")
    ,path('wiki/<entry>', views.detail, name="detail"),



]
# for item in util.list_entries():
#     path(item,views.)