from unicodedata import name
from django.urls import URLPattern, path

from .views import index, blog, detailedView, search

app_name = 'core'
urlpatterns = [
    path('', index),
    path('blog/', blog, name='blog'),
    path('blog/<str:slug>', detailedView, name='detailed-blog'),
    path('search/', search, name='search')
]