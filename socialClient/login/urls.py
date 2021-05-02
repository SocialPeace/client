from django.urls import path, include
from .import views

urlpatterns = [ 
    path('login/',views.login,name='login'), 
    path('logout/',views.logout,name='logout'),
    path('accounts/',include('allauth.urls')),
    path('',views.loading,name='loading'), 
]