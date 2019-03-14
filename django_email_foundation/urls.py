from django.urls import path
from django_email_foundation.views import TemplatesPreviewIndex, TemplatePreview

app_name = 'django_email_foundation'

urlpatterns = [
    path('', TemplatesPreviewIndex.as_view(), name='index'),
    path('preview/<str:folder>/<str:file>/', TemplatePreview.as_view(), name='preview'),
]
