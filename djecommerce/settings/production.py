from .base import *

SECRET_KEY = 'kym*cd$co*+idvf%n(3wk3yp5b2gm!in2q$l^ehstf@gz99sf@'
DEBUG = config('DEBUG', cast=bool)
# ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']
ALLOWED_HOSTS = ["*"]
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': ''
    }
}

STRIPE_PUBLIC_KEY = config('pk_test_0kKPA2HvrhSijPCVD7iUXqvF00SFzZ2dU9')
STRIPE_SECRET_KEY = config('sk_test_JDlNFJu5gbmxCm5rkINKrzfe00QkkpKz2C')