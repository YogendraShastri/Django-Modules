# Django-Modules
All New Modules I tried on Django

First of all need to install Django & Django-admin (pip3 install)

## first create a PROJECT :
Create Project using django-admin account
```python
django-admin startproject mysite
```

The project folder will be created with the files :
```python
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

## create an app for the PROJECT:
```python
python manage.py startapp myapp
```

The app folder will be created with the proper files :
```python
myapp/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

After this we need to create on urls.py file at myapp ,so that we can rediret our app specific urls,(templates etc)
```python
cd myapp
```
Flow
**touch urls.py --> insert --> save it**

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

[ Note :- here we redirect the home location to search at views.py for the index function ] 

But First we need to tell our project that where to tranfer when any request come for the app :
so at mysite, edit urls.py -->

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
```

Now we need to create functi at **views.py** : 

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
    
We need to tell django which app to use for the deployment : 

Go to **mysite --> apps.py**

```python
class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

```

take classname from the file : copy it and paste in mysite --> settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyAppConfig',
]
```  
    
**Save** it.

Now we can run our server for testing : with any specified port ->
```python
python3 manage.py runserver 8080
```

without port also it will work :
```python
python3  manage.py runserver
```


## For configuring  Templates and Static folder :

* Create templates & static folders where manage.py files is present, and add there location to --> settings.py file.

* add this to bottom
```python
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```
* and Modify the templates as well :

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "templates", ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

add your html files on templates and images, js, css, etc on static folder.

edit your **views.py** according to your templates

```python
from django.http import HttpResponse, render

def index(request):
    return render(request, 'index.html')
```
