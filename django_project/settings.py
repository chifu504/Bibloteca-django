import environ
import os
from pathlib import Path



env = environ.Env()


BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',  
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites", 

    #apps de apps externas
    "allauth", 
    "allauth.account", 
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    #apps
    "accounts.apps.AccountsConfig",
    "pages.apps.PagesConfig",
    "books.apps.BooksConfig", 
]

MIDDLEWARE = [
    'books.middleware.PruebaMiddleware', #difinemios que en esta runta tendremos un middleware personalizado
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_project.context_processors.categorias_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'




DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": 5432,
    }
}




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#para archivos estaticos----------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"] 

#modela personalizado-----
AUTH_USER_MODEL = "accounts.CustomUser" 


LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT = "home"  

# django-allauth configuracion ------------------------------
SITE_ID = 1 
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend", #esto es para poder poder cambiar la configuracion ejem iniciar secion con correo
)
ACCOUNT_SESSION_REMEMBER = True 
ACCOUNT_USERNAME_REQUIRED = True 
ACCOUNT_AUTHENTICATION_METHOD = "username" 
# ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True 
# ACCOUNT_EMAIL_VERIFICATION = "mandatory" 
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1 
ACCOUNT_LOGOUT_ON_GET= True 


DEFAULT_FROM_EMAIL = "lolapaluza@gmail.com"



ACCOUNT_FORMS = {
'signup': 'books.forms.MyCustomSignupForm',
}


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" #para recibir correos en la consola


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media" 



