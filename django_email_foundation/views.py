import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django_email_foundation import settings
from django_email_foundation.api import DjangoEmailFoundation


class TemplatesPreviewIndex(TemplateView):
    """
    View for show a build templates preview. The user can see his templates and click over one for
    to see the content.
    """
    template_name = 'django_email_foundation/preview.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['destination_template'] = settings.DEF_TEMPLATES_TARGET_PATH
        context['has_permission'] = True
        context['title'] = 'Django Email Foundation Templates Preview'

        engine = DjangoEmailFoundation()
        context['templates'] = engine.get_build_files()

        return context


class TemplatePreview(View):
    """
    For to see a one template content. It render the template using the custom fixed context if exist one.
    """

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        template_folder_name = settings.DEF_TEMPLATES_TARGET_PATH.split('/')[-1]
        template_path = '{}/{}/{}'.format(template_folder_name, kwargs['folder'], kwargs['file'])

        context = self.get_context(kwargs['folder'], kwargs['file'])
        html = render_to_string(template_path, context=context)

        return HttpResponse(html)

    def get_context(self, folder: str, file: str):
        if not settings.DEF_CONTEXT_JSON_FILE:
            return {}
        with open(settings.DEF_CONTEXT_JSON_FILE) as json_file:
            data = json.loads(json_file.read())
            try:
                context = data[folder][file]
            except KeyError:
                context = {}
        return context
