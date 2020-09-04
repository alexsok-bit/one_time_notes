from subprocess import call
from urllib.parse import urlparse
from urllib.parse import urljoin

from django.conf import settings
from django.http import HttpResponseRedirect
from django.views import View


class IndexPage(View):
    upload_to = "url2pdf"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.upload_to = settings.MEDIA_ROOT.joinpath(self.upload_to)
        self.upload_to.mkdir(parents=True, exist_ok=True)

    def get(self, request, url, *args, **kwargs):
        file_path = self.cast_file_path(url)
        self.make_pdf(url, file_path)
        redirect_to = self.cast_file_url(file_path)
        return HttpResponseRedirect(redirect_to)

    def cast_file_path(self, url):
        filename = "{url.hostname}{url.path}.pdf".format(url=urlparse(url)).replace("/", "_")
        return self.upload_to.joinpath(filename)

    def cast_file_url(self, file_path):
        upload_url = urljoin(settings.MEDIA_URL, self.upload_to.name)
        return f"{upload_url}/{file_path.name}"

    def make_pdf(self, url, output_path):
        return call(f"wkhtmltopdf {url} {output_path}".split()) == 0
