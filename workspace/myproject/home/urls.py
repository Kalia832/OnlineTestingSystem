from django.urls import path
from home.views import *
app_name='home'
urlpatterns=[ 
    path('',userHome,name='home'),
    path('registrationForm/',registrationForm,name='registrationForm'),
    path('ContactUs/',contactForm,name='contactForm'),
    path('storeUser/',storeUser,name='storeUser'),
    path('LoginForm/',login,name='loginView'),
    path('userHome/',userHome,name='userHome'),
    path('Testpaper/',testPaper,name='testPaper'),
    path('calculateTest',calculateTest,name='calculateTest'),
    path('TestHistory/',testHistory,name='testHistory'),
    path('result',showTestResult,name='result'),
    path('logout/',logOut,name='logOut')
]