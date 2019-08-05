from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('center/<int:project_id>/', views.center, name='center'),
    path('project_detail/', views.project_detail, name='project_detail'),
    path('about/', views.about, name = 'about'),

]

