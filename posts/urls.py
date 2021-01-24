from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='index'),
   path('test/', views.test, name='test'),
   path('<int:id>/', views.nav, name='nav'),
   path('navbar/', views.createpost, name='createpost'),
   # path('navbar.html', views.home, name='home'),   
]

