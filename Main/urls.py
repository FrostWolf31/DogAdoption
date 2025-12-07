from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('index.html', views.Index, name='index_html'),
    path('adopt.html', views.adopt, name='adopt'),
    path('pet.html', views.pet, name='pet'),
    path('about.html', views.about, name='about'),
    path('faq.html', views.faq, name='faq'),
    path('dogselect.html', views.select, name='select'),
    path('stories.html', views.story, name='story'),
    path('article1.html', views.article1, name='article1'),
]
