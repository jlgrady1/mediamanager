"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from sorter.models import Type, Status, MediaFile, Action, DownloadFolder, \
                          Configuration

import sorter.files
from django.db.utils import IntegrityError

class TypeMethodTests(TestCase):
    def test_save(self):
        type = Type(code='mytestcode')
        type.save()
        self.assertIsNotNone(type.date_created)
        self.assertEqual(type.date_created, type.date_updated)
        newtestcode = 'newtestcode'
        type.code = newtestcode
        type.save()
        self.assertNotEqual(type.date_created, type.date_updated)
        self.assertGreater(type.date_updated, type.date_created)
        dbtype = Type.objects.get(pk=1)
        self.assertEqual(dbtype.code, newtestcode)

class StatusMethodTests(TestCase):
    def test_save(self):
        status = Status(code='mystatus')
        status.save()
        self.assertIsNotNone(status.date_created)
        self.assertEqual(status.date_created, status.date_updated)
        newstatuscode = 'newstatuscode'
        status.code = newstatuscode
        status.save()
        self.assertNotEqual(status.date_created, status.date_updated)
        self.assertGreater(status.date_updated, status.date_created)
        dbstatus = Status.objects.get(pk=1)
        self.assertEqual(dbstatus.code, newstatuscode)

class MediaFileMethodTests(TestCase):
    def test_save(self):
        type = Type(code='video')
        type.save()
        status = Status(code='convert')
        status.save()
        mf = MediaFile(type=type, status=status, \
                       filepath='/fakefilepath/myfile.mkv')
        mf.save()
        self.assertIsNotNone(mf.date_created)
        self.assertEqual(mf.date_created, mf.date_updated)
        newfilepath = '/fakefilepath/myfile.mp4'
        mf.filepath = newfilepath
        mf.save()
        self.assertNotEqual(mf.date_created, mf.date_updated)
        self.assertGreater(mf.date_updated, mf.date_created)
        dbmf = MediaFile.objects.get(pk=1)
        self.assertEqual(dbmf.filepath, newfilepath)
        self.assertEqual(dbmf.type, type)
        self.assertEqual(dbmf.status, status)

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
    def test_save(self):
        type = Type(code='video')
        type.save()
        status = Status(code='rename')
        status.save()
        mf = MediaFile(type=type, status=status, \
                       filepath='/fakefilepath/myfile.mkv')
        mf.save()
        command = '/usr/bin/mycommand'
        completion = 50
        description = 'run some command'
        action = Action(mediafile = mf, command = command, \
                        completion = completion, description = description)
        action.save()
        self.assertIsNotNone(action.date_created)
        self.assertEqual(action.date_created, action.date_updated)
        newcompletion = 75
        action.completion = newcompletion
        action.save()
        self.assertNotEqual(action.date_created, action.date_updated)
        self.assertGreater(action.date_updated, action.date_created)
        dbaction = Action.objects.get(pk=1)
        self.assertEqual(dbaction.completion, newcompletion)
        status2 = Status(code='convert')
        status2.save()
        duplicate_path_mf = MediaFile(type=type, status=status2, \
                       filepath='/fakefilepath/myfile.mkv')
        self.assertRaises(IntegrityError, lambda: duplicate_path_mf.save())

class DownloadFolderMethodTests(TestCase):
    def test_save(self):
        top_folder = DownloadFolder(folder = '/path/to/my/folder')
        top_folder.save()
        self.assertIsNotNone(top_folder.date_created)
        self.assertEqual(top_folder.date_created, top_folder.date_updated)
        self.assertEqual(top_folder.level, 0)
        child_folder1 = DownloadFolder(folder = '/path/to/my/folder/child', \
                                       parent = top_folder)
        child_folder1.save()
        self.assertEqual(child_folder1.level, 1)
        child_folder2 = DownloadFolder( \
                folder = '/path/to/my/folder/child/child2', \
                parent = child_folder1)
        child_folder2.save()
        self.assertEqual(child_folder2.level, 2)
        new_folder = '/changedpath/to/my/folder'
        top_folder.folder = new_folder
        top_folder.save()
        self.assertNotEqual(top_folder.date_created, top_folder.date_updated)
        self.assertGreater(top_folder.date_updated, top_folder.date_created)
        dbdf = DownloadFolder.objects.get(pk=1)
        self.assertEqual(dbdf.folder, new_folder)
        db_child1 = DownloadFolder.objects.get(pk=2)
        self.assertEqual(db_child1.parent, dbdf)

class ConfigurationMethodTests(TestCase):
    def test_save(self):
        config = Configuration(key="mykey", value="myvalue")
        config.save()
        self.assertIsNotNone(config.date_created)
        self.assertEqual(config.date_created, config.date_updated)
        newvalue = 'newvalue'
        config.value = newvalue
        config.save()
        self.assertNotEqual(config.date_created, config.date_updated)
        self.assertGreater(config.date_updated, config.date_created)
        dbconfig = Configuration.objects.get(pk=1)
        self.assertEqual(dbconfig.value, newvalue)