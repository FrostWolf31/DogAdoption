
from django.contrib import admin
from django.urls import path, include
from Main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main.urls')),
    path('contact.html', views.contact, name='contact'),
    path('index.html', views.Index, name='index'),
    path('adopt.html', views.adopt, name='adopt'),
    path('pet.html', views.pet, name='pet'),
    path('about.html', views.about, name='about'),
    path('faq.html', views.faq, name='faq'),
    path('dogselect.html', views.select, name='select'),
    path('stories.html', views.story, name='story'),
    path('article1.html', views.article1, name='article1')
]


if settings.DEBUG:
    # Serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
