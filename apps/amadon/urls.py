from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^amadon$', views.index),
    url(r'^amadon/purchase', views.purchase),
    url(r'^amadon/checkout', views.checkout)
]