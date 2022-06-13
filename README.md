# auth2

### Ready to use authentication and authorization app.

auth2 is extension of django.contrib.auth app. It's based primarily on class-based views and mixins, there is no space
to old-school functions in auth2. It makes easier to manage users and groups by providing easy to use customizable UI.
You can use any UI kit that is compatible with Bootstrap 5.

# Get started

Let's test auth2 in action, we will start by starting a new project then we will clone the auth2 repo using git, so make
sure that you have [Git](https://git-scm.com/) installed on your machine. <br>
auth2 is a Django app, so we need [Python](https://python.org/) and [Django](https://djangoproject.com/) installed on
our machine. Let's start by creating our project:

```shell
django-admin startproject mysite
cd mysite
```

Now, we are going to clone the repo into our project:

```shell
git clone https://github.com/youzarsiph/auth2.git
```

Install auth2, in `mysite/settings.py`:

```python
INSTALLED_APPS = [
    '.apps.Auth2Config',  # Add this line
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Include urls.py, in `mysite/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include  # import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('.urls')),  # Add this line
]
```

We need to create a super user because auth2 views require the user to be a staff with permissions or a super user. Run
the following command and enter your information:

```shell
py manage.py createsuperuser

Username (leave blank to use 'user'): admin
Email address: admin@example.com
Password: **********
Password (again): **********
Superuser created successfully.
```

Run the server:

```shell
python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 05, 2022 - 15:51:43
Django version 3.2.7, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Now, we are ready click the link to open in your browser:
[Open in browser](http://127.0.0.1:8000/accounts/)
