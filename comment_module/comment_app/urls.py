from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uploadPage', views.upload_page, name='upload_page'),
    path('uploadPost', views.upload_post, name='upload_post'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('send_mail', views.send_email, name='send_email'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

