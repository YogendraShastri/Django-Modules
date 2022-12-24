from django.shortcuts import render, redirect
from .models import AlbumPost
from django.core.paginator import Paginator
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages


# Create your views here.
from django.http import HttpResponse


def index(request):
    myposts = AlbumPost.objects.all()
    p = Paginator(myposts, 6)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    print(myposts)
    return render(request, 'index.html', {'page_obj': page_obj})

def upload_page(request):
    return render(request, 'uploads.html')

def upload_post(request):
    if request.method == 'POST':
        #getting the parameters
        album_title = request.POST['a_title']
        album_subtitle = request.POST['a_subtitle']
        album_image = request.POST['a_image']
        album_area = request.POST['a_area']
        whole_post = AlbumPost(album_title=album_title, album_subtitle=album_subtitle, album_image=album_image, album_area=album_area)
        whole_post.save()
        messages.success(request, "Your Album is uploaded successfully")
        return redirect('/uploadPage')
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def send_email(request):
    if request.method == 'POST':
        sender = request.POST.get('Sender', '')
        message = request.POST.get('SenderIssue', '')
        sender_email = 'c0comd3bl0ck8@gmail.com'
        if sender and message and sender_email:
            try:
                send_mail(sender, message, sender_email, ['codingtrialsbyyogi@gmail.com'])
                messages.success(request, "Your Issue send to US successfully")
                return redirect('/contact')
            except BadHeaderError:
                messages.error(request, "Your Issue send to US successfully")
    return HttpResponse('404 - ERROR : Not Valid')