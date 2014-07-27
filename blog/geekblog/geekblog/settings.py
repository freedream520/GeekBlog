# -*- coding: utf-8 -*-
# Django settings for geekblog project.
import os
import re
from django.utils.translation import ugettext_lazy as _

from blogcore import CORE_LOCALE_PATH
from utils import FreeConfigParser

DEBUG = True
TEMPLATE_DEBUG = DEBUG

LANGUAGE_CODE = None
LANGUAGES = (
    ('zh-cn', u'简体中文'),
    ('en-us', 'English'),
)

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOG_ROOT = None
SITE_DOMAIN = None
MONGODB_CONF = None
UPLOAD_FILE_ROOT = '/var/app/enabled/blog-webfront/static/'

EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_SUBJECT_PREFIX = '[GeekBlog] '

EMAIL_HOST_USER = None
EMAIL_HOST_PASSWORD = None
SERVER_EMAIL = None

DUOSHUO_SECRET = None    # 多说分配的token
DUOSHUO_SHORT_NAME = None    # 多说上注册的二级域名


def _load_config(section, config_files):
    global DEBUG, LOG_ROOT, MONGODB_CONF, LANGUAGE_CODE, UPLOAD_FILE_ROOT, \
            SITE_DOMAIN, DATABASES, DUOSHUO_SECRET, DUOSHUO_SHORT_NAME, EMAIL_HOST_USER, \
            EMAIL_HOST_PASSWORD, SERVER_EMAIL

    cp = FreeConfigParser()
    cp.read(config_files)

    DEBUG = cp.getboolean(section, 'debug')
    LOG_ROOT = cp.get(section, 'log_root')
    MONGODB_CONF = cp.get(section, 'mongodb_conf')
    LANGUAGE_CODE = cp.get(section, 'language_code')
    UPLOAD_FILE_ROOT = cp.get(section, 'upload_file_root')
    SITE_DOMAIN = cp.get(section, 'file_storage_domain_conf')
    DUOSHUO_SECRET = cp.get(section, 'duoshuo_secret')
    DUOSHUO_SHORT_NAME = cp.get(section, 'duoshuo_short_name')
    EMAIL_HOST_USER = cp.get(section, 'email_host_user')
    EMAIL_HOST_PASSWORD = cp.get(section, 'email_host_password')
    SERVER_EMAIL = EMAIL_HOST_USER
    blog_db_conf = re.split(r'[@:/]', cp.get(section, 'blog_db_conf'))
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'USER': blog_db_conf[0],
            'PASSWORD': blog_db_conf[1],
            'HOST': blog_db_conf[2],
            'PORT': blog_db_conf[3],
            'NAME': blog_db_conf[4],
        },
    }

_load_config('blog', [os.path.join(SITE_ROOT, "geekblog.cfg")])

WEBSITE_NAME = u'降龙'
WEBSITE_DESC = u'记录生活与工作的点滴，分享旅行与技术的乐趣'
SAYING = u'一切都会过去！'    # u'不相信自己的人，连努力的价值都没有。'
WEBSITE_URL = 'http://xianglong.me/'

LIST_PER_PAGE = 8

ADMINS = (
    ('WuXianglong', 'wuxianglong098@gmail.com'),
)

MANAGERS = ADMINS

# date and datetime field formats
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.xianglong.me', '115.28.143.213']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = UPLOAD_FILE_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = UPLOAD_FILE_ROOT

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/var/app/enabled/blog-webfront/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ohdnmz&jf#^d-#47a2o$0m^yz@j3^r^cyf8n5r6#-np5=%8e37'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'geekblog.geekblog.context_processors.urlname',
    'geekblog.geekblog.context_processors.website_meta',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'geekblog.geekblog.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'geekblog.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, "templates"),
)

LOCALE_PATHS = (
    os.path.join(SITE_ROOT, "locale"),
    os.path.join(SITE_ROOT, "jsi18n", "locale"),
)
LOCALE_PATHS += CORE_LOCALE_PATH

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'ueditor',
    'duoshuo',
    'jsi18n',
    'blog',
    'catearticles',
    'usermanagement',
)
# should declare this after 'INSTALL_APPS'.
AUTH_USER_MODEL = 'usermanagement.CustomUser'

LEFT_NAV_MODELS = {
    'blog': {
        'order': 1,
        'title': _('content management'),
        'models': [
            'catearticles.*',
            'blogcore.models.blog.Category',
            'blogcore.models.blog.Tag',
            'blogcore.models.blog.Link',
            'blogcore.models.blog.Slider',
            'blogcore.models.blog.Photo',
            'blogcore.models.blog.Comment',
        ],
        'app_label_order': {
            'catearticles': 1,
            'blog': 2,
        }
    },
    'auth': {
        'order': 2,
        'title': _('system management'),
        'models': [
            'usermanagement.*',
            'django.contrib.admin.models.LogEntry',
        ],
        'app_label_order': {
            'usermanagement': 1,
            'admin': 2,
        }
    },
}

ADMIN_LIST_PER_PAGE = 20

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOG_FILE = os.path.join(LOG_ROOT, 'info.log')
LOG_ERR_FILE = os.path.join(LOG_ROOT, 'error.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        'detail': {
            'format': '%(levelname)s %(asctime)s %(name)s [%(module)s.%(funcName)s] %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'formatter': 'detail',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': LOG_FILE,
        },
        'err_file': {
            'level': 'ERROR',
            'formatter': 'detail',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': LOG_ERR_FILE,
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'geekblog': {
            'handlers': ['console', 'file', 'err_file'] if DEBUG else ['file', 'err_file'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
