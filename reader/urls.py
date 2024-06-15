from django.urls import path

from . import views

app_name = 'reader'
urlpatterns = [path('', views.IndexView.as_view(), name="index"),]

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
]