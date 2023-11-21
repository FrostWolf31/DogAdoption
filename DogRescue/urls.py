
from django.contrib import admin
from django.urls import path, include
from Main import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main.urls')),
    path('contact.html', views.contact, name='contact'),
    path('index.html', views.Index, name = 'index'),
    path('adopt.html', views.adopt, name = 'adopt'),
    path('pet.html', views.pet, name = 'pet'),
    path('about.html', views.about, name = 'about'),
    path('faq.html', views.faq, name = 'faq'),
    path('dogselect.html', views.select, name ='select')
]
