from django.urls import path
from . import views

app_name = 'RTApp'

urlpatterns = [
    path('std', views.SeleceStdView, name = 'std'),
    path('std/<str:std_id>/sec', views.SectionView, name= 'single-std'),


    path('detail', views.recentDetail, name = 'detail')
]

