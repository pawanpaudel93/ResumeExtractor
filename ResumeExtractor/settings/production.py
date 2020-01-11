import dj_database_url
from decouple import config
from .base import MIDDLEWARE

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

# for hosting media files
# Do not change any of these names
B2_BUCKET_NAME = config('HB2_B2_BUCKET_NAME')
B2_BUCKET_ID = config('HB2_B2_BUCKET_ID')
B2_ACCOUNT_ID = config('HB2_B2_ACCOUNT_ID')
B2_APPLICATION_KEY = config('HB2_B2_APP_KEY')
DEFAULT_FILE_STORAGE = 'django_b2storage.backblaze_b2.B2Storage'
