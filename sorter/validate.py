import os

from django.core.exceptions import ValidationError

def folder_exists(folder):
    if os.path.exists(folder) is False:
        raise ValidationError(u'Folder %s does not exist' % folder)
    if not os.access(folder, os.R_OK):
        raise ValidationError(u'Cannot read folder %s' % folder)

def folder_writable(folder):
    if not os.access(folder, os.W_OK):
        raise ValidationError(u'Cannot write to folder %s' % folder)
