from django.conf.urls import url
from django.contrib import admin

from churchForm import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^person_info/(\d+)/', views.person_info, name='person_info'),
    url(r'^create$', views.create, name='create'),
    url(r'^update/(\d+)/', views.update, name='update'),
    url(r'^delete/(\d+)/', views.delete, name='delete'),
]
