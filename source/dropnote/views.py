from django.contrib import messages
from django.http import Http404, HttpResponsePermanentRedirect
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic import CreateView

from .models import SnippetItem


class IndexPage(CreateView):
    template_name = "dropnote/index.html"
    model = SnippetItem
    fields = ["text"]


class ViewPage(DetailView):
    template_name = "dropnote/view.html"
    content_type = "text/html"
    model = SnippetItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snippet_url"] = self.request.build_absolute_uri(self.object.get_absolute_url())
        return context

    def post(self, request, **kwargs):
        """Ajax"""
        self.object = self.get_object()
        self.object.delete()
        context = self.get_context_data(object=self.object)
        self.template_name = "dropnote/snippet.html"
        return self.render_to_response(context, content_type="text/plain")

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            messages.add_message(request, messages.WARNING, 'Note not found!', extra_tags="alert-warning",)
            return HttpResponsePermanentRedirect(reverse("dropnote:index"))
