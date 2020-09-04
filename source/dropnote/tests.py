import re
import os
from subprocess import check_output

from django.test import TestCase

os.environ.setdefault("DJANGO_HOST", "http://127.0.0.1:8000/")


class TestMakeNote(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.host = os.environ["DJANGO_HOST"]
        if self.host.endswith("/"):
            self.host = self.host[:-1]

    def test_make_note(self):
        output = check_output(f"curl -X PUT -s -d 'Hello' {self.host}/", shell=True)
        self.assertTrue(re.match(b"^" + self.host.encode() + b"/[0-9a-z]{6}/$", output), output)

        snippet_url = output.decode()
        output = check_output(f"curl -X POST -s {snippet_url}", shell=True)
        self.assertEqual(b"Hello\n", output)
