from django.contrib import messages
from django.http import Http404, HttpResponsePermanentRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from django.views.generic import CreateView

from .models import SnippetItem


@method_decorator(csrf_exempt, name="dispatch")
class IndexPage(CreateView):
    """Страница создания заметки"""
    template_name = "dropnote/index.html"
    model = SnippetItem
    fields = ["text"]

    def put(self, request, *args, **kwargs):
        self.template_name = "dropnote/snippet.html"
        response = self.post(request, *args, **kwargs)
        if self.object:
            response_data = self.request.build_absolute_uri(self.object.get_absolute_url())
        else:
            response_data = response.context_data["form"].errors.as_text()
        return self.render_to_response({"object": {"text": response_data}}, content_type="text/plain")

    def get_form_class(self):
        form_class = super().get_form_class()
        if self.request.method.lower() in ["put"]:
            form_class.base_fields["text"].disabled = True
            self.initial = {"text": self.request.body.decode()}
        return form_class


@method_decorator(csrf_exempt, name="dispatch")
class ViewPage(DetailView):
    """Страница просмотра"""
    template_name = "dropnote/view.html"
    content_type = "text/html"
    model = SnippetItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # добавляем в контекст абсолютный урл на заметку
        context["snippet_url"] = self.request.build_absolute_uri(self.object.get_absolute_url())
        return context

    def post(self, request, **kwargs):
        """Запрос сюда приходит от JS, когда пользователь решил увидеть содержимое."""
        self.object = self.get_object()
        self.object.delete()
        context = self.get_context_data(object=self.object)
        self.template_name = "dropnote/snippet.html"
        return self.render_to_response(context, content_type="text/plain")

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            # вместо отображения страницы с 404, лучше покажем уведомление.
            messages.add_message(request, messages.WARNING, 'Note not found!', extra_tags="alert-warning",)
            return HttpResponsePermanentRedirect(reverse("dropnote:index"))
