=====
Django Blog
=====
this is a Django app to create blog app and manage them
Quick start
-----------
1. to install ``https://test.pypi.org/project/drf-blog/1.1/``

2. Add "blog" to your INSTALLED_APPS setting like this::
INSTALLED_APPS = [
        ...
        "django_summernote",
        "rest_framework",
        "blog",
  ]
3. Include the Media URL project urls.py like this:

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = "static/"

4. Run ``python manage.py migrate`` to create the Blog models.
