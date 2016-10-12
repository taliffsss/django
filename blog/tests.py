from django.test import TestCase
from favicon import conf
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage


class FaviconFilePathTest(TestCase):
    def test_favicon_file_path(self):
        """
        Tests that favicon.ico exists in the path specified  in FAVICON_PATH setting
        """
        absolute_path = finders.find('favicon.ico')
        assert staticfiles_storage.exists(absolute_path)
