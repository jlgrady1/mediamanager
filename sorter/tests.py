"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import logging
import validate

from django.test import TestCase

from sorter.models import Type, Status, MediaFile, Action, MediaFolder, \
                          Configuration

import sorter.files

from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

# Get an instance of a logger
log = logging.getLogger(__name__)

class TypeMethodTests(TestCase):
    pass

class StatusMethodTests(TestCase):
    pass

class MediaFileMethodTests(TestCase):
    def test_get_filename(self):
        mf = MediaFile(type = Type(code='video'), \
                       status = Status(code='rename'), \
                       filepath ='/fakefilepath/myfile.mkv')
        self.assertEqual(mf.get_filename(), 'myfile.mkv')

    def test_get_extension(self):
        mf = MediaFile(type = Type(code='video'), \
                       status = Status(code='rename'), \
                       filepath ='/fakefilepath/myfile.mkv')
        self.assertEqual(mf.get_extension(), 'mkv')
        mf.filepath ='/fakefilepath/myfile.test.mkv'
        self.assertEqual(mf.get_extension(), 'mkv')

class ActionMethodTests(TestCase):
    pass

class MediaFolderMethodTests(TestCase):
    def test_get_level(self):
        top_folder = MediaFolder(folder = '/path/to/my/folder')
        top_folder.save()
        self.assertEqual(top_folder.get_level(), 0)
        child_folder1 = MediaFolder(folder = '/path/to/my/folder/child', \
                                    parent = top_folder)
        child_folder1.save()
        self.assertEqual(child_folder1.get_level(), 1)
        child_folder2 = MediaFolder( \
                folder = '/path/to/my/folder/child/child2', \
                parent = child_folder1)
        child_folder2.save()
        self.assertEqual(child_folder2.get_level(), 2)
        child_folder3 = MediaFolder( \
                folder = '/path/to/my/folder/child/child3', \
                parent = child_folder1)
        child_folder3.save()
        self.assertEqual(child_folder3.get_level(), 2)


class ConfigurationMethodTests(TestCase):
    pass

class ValidatorsMethodTests(TestCase):
    def test_validate_folder_exists(self):
        missingfolder = '/bogus'
        self.assertRaises(ValidationError, \
                          lambda: validate.folder_exists(missingfolder))

class FormMethodTests(TestCase):
    fixtures = ['type', 'config',]
    def test_setup_form(self):
        folder_name = '/opt'

        bad_form_data = {'scan_folder': '/tmp', \
                         'destination_folder' : '/bogus'}
        response = self.client.post('/setup/', bad_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertRaises(Configuration.DoesNotExist, \
                          lambda: Configuration.objects.get(key='destination.folder'))

        good_form_data = {'scan_folder': folder_name, \
                          'destination_folder' : '/tmp/'}
        response = self.client.post('/setup/', good_form_data)
        self.assertEqual(response.status_code, 200)
        try:
            sf = MediaFolder.objects.get(folder=folder_name)
        except MediaFolder.DoesNotExist:
            log.error(MediaFolder.objects.all())
            self.fail("Scan folder was not saved")
        try:
            df = Configuration.objects.get(key='destination.folder')
            self.assertEqual(df.value, '/tmp', \
                             "Trailing slash not removed from dir")
        except Configuration.DoesNotExist:
            log.error(Configuration.objects.all())
            self.fail("Destination folder was not saved")
        sf.delete()
        df.delete()
