import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zejq&n^*9%d1)ab0m^!7k0!uxyi03dp$2+dlf($1$p56!r0+*q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'pipeline',
    # apps
    'integrity',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'reactintegrify.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'reactintegrify.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'reactintegrify/static'),
    os.path.join(BASE_DIR, 'bower_components'),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# PIPELINE = {
#     'PIPELINE_ENABLED': True,
#     'JAVASCRIPT': {
#         'stats': {
#             'source_filenames': (
#                 'bower_components/bootstrap/dist/js/bootstrap.min.js',
#             ),
#             'output_filename': 'js/stats.js',
#         }
#     }
# }
PIPELINE = {
    'PIPELINE_ENABLED': True,
    'JAVASCRIPT': {
        'custom_js': {
            'source_filenames': (
              'js/set_csrf.js',
              'js/utils.js',
            ),
            'output_filename': 'js/bundled/bundled.js',
        }
    },
    # 'STYLESHEETS': {
    #     'bower_installed_css': {
    #         'source_filenames': (
    #             'bower_components/bootstrap/dist/css/bootstrap*.min.css',
    #             'bower_components/bootstrap/dist/css/bootstrap*.css.map',
    #         ),
    #         'output_filename': 'css/booststrap_all.css',
    #         # 'extra_context': {
    #         #     'media': 'screen,projection',
    #         # },
    #     },
    # },
}
# PIPELINE['YUGLIFY_BINARY'] = os.path.join(BASE_DIR, 'node_modules/yuglify/bin yuglify')
# PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE['UGLIFYJS_BINARY'] = os.path.join(BASE_DIR, 'bower_components/uglify-js/bin/uglifyjs')
# YUGLIFY_BINARY = os.path.join(BASE_DIR, 'node_modules/yuglify/bin yuglify')
# ' bower_components/uglify-js/bin/uglifyjs'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
