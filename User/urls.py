from django.urls import path

from .import views

urlpatterns=[
    path('',views.login,name='login'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contact'),
    path('home',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('lcancer',views.lungcancer,name='lcancer'),
    path('diabetes',views.diabetes,name='diabetes'),
    path('bcancer',views.breastcancer,name='bcancer'),
    path('lungpredict',views.Predictlung,name='lungpredict'),
    path('breastpredict',views.predictbreast,name='breastpredict'),
    path('predictdiabetes',views.Predictdiabetes,name='diabetespredict'),
]