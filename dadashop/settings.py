"""
Django settings for dadashop project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APPEND_SLASH = False

# Quick-start development setings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5gn^o9a6jgrk!6g%o1cye_84)=5l^5al^dcu42oe6@#(%c=!(g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# 将Django默认的认证系统模型改为我们自己定义


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'goods',
    'order',
    'carts',
    'dtoken',
    'corsheaders',
    'haystack',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dadashop.urls'

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

WSGI_APPLICATION = 'dadashop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dadashop',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )


# 配置redis数据库相关设置：
CACHES = {
    "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        },
    "verify_email": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },

    "cart": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/4",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        },
    
    "goods": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/5",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}


CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)


CORS_ALLOW_HEADERS = (
'XMLHttpRequest',
'X_FILENAME',
'accept-encoding',
'authorization',
'content-type',
'dnt',
'origin',
'user-agent',
'x-csrftoken',
'x-requested-with',
'Pragma',
'HTTP_AUTHORIZATION'
)

# Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'elasticstack.backends.ConfigurableElasticSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'dadashp',
    },
}
# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# 搜索的每页大小（根据需求自行修改或添加）
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 9


# 配置相关的邮箱参数
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
# 发用邮件的邮箱
EMAIL_HOST_USER = '249155836@qq.com'
# 邮箱中的授权密码
EMAIL_HOST_TLS = False
EMAIL_HOST_PASSWORD = 'zptybotokwnwbihe'
# 收件人看到的邮箱发件人
EMAIL_FROM = 'DADASHOP<249155836@qq.com>'


# 线上微博第三方登陆的配置信息
# 微博开发者平台注册应用ID
WEIBO_CLIENT_ID = '2987431629'
# # 微博开发者平台注册的应用的密钥
WEIBO_CLIENT_SECRET = 'fe3c4fe60da7f2de3413522c1551b7d2'
# 需要在高级应用中配置的正常请求之后的回调地址
# 此处修改为线上状态为DEBUG == False

if DEBUG == True:
    REDIRECT_URI = 'http://127.0.0.1/html/dadashop/templates/callback.html'
else:
    REDIRECT_URI = 'http://114.116.244.115:7000/dadashop/templates/callback.html'

#容联云SDK参数
#主账号
SCCOUNTSID= '8a216da86cdb6950016ce026845d02a1'
#主账号Token
ACCOUNTTOKEN= '297b78d42a2640aa90f50eb29465a7b0'
#应用Id
APPID='8a216da86cdb6950016ce026858f02a8'
#请求地址，格式如下，不需要http://
SERVERIP='app.cloopen.com'
#端口
SERVERPORT='8883'
#REST版本号
SOFTVERSION='2013-12-26'

# 显示商品图片配置
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# redis相关配置
# 官网定义的变量名:
# https://docs.celeryproject.org/en/latest/userguide/configuration.html#task-result-backend-settings
BROKER_URL = 'redis://127.0.0.1/14'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1/15'

STATIC_ROOT = '/tedu/dadashop/django_static'

# alipayURL测试
IP_URL = "127.0.0.1"
# alipayURL正式
# IP_URL = "114.116.244.115"

# 线上商城回调地址
# http://114.116.244.115/dadashop/templates/callback.html

if DEBUG == True:
    # 后端测试用图片接口
    PIC_URL = "http://127.0.0.1:8000" + MEDIA_URL
    ACTIVE_HOST = 'http://127.0.0.1'
else:
    # 线上图片接口
    PIC_URL = 'http://114.116.244.115:7001'+ MEDIA_URL
    ACTIVE_HOST = 'http://114.116.244.115:7000'
