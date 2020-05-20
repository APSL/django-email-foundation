try:
    from django.urls import path
except ImportError:
    # Support for Django 1.9.x
    from django.conf.urls import url

from django_email_foundation.views import TemplatesPreviewIndex, TemplatePreview

app_name = 'django_email_foundation'

try:
    urlpatterns = [
        path('', TemplatesPreviewIndex.as_view(), name='index'),
        path('preview/<str:folder>/<str:file>/', TemplatePreview.as_view(), name='preview'),
    ]
except NameError:
    # Path not imported, use url instead for Django 1.9.x
    urlpatterns = [
        url(r'^$', TemplatesPreviewIndex.as_view(), name='index'),
        url(r'^preview/(?P<folder>[0-9A-Za-z\._-]+)/(?P<file>[0-9A-Za-z\._-]+)/', TemplatePreview.as_view(),
            name='preview'),
    ]
