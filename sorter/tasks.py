import logging
import os

from celery import task

# Get an instance of a logger
log = logging.getLogger(__name__)

@task()
def scan(media_folder):
    folder = media_folder.folder
    log.info(u'starting media scan of %s' % folder)
    contents = os.listdir(folder)
    log.debug("found media files: " + str(contents))
    for file in contents:
        if os.path.isfile(file):
            pass

    return contents
