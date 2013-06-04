import logging

from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from sorter.models import Action, Configuration, MediaFolder, Type
from sorter.forms import SetupForm

# Get an instance of a logger
log = logging.getLogger(__name__)

def home(request): # The home / index view
    context = {}
    # Check for media folders and begin first time setup if they do not exist
    if len(MediaFolder.objects.all()) == 0:
        log.info("No media folders defined. Entering Setup")
        return setup(request)
    current_actions = Action.get_actions_in_progress() # list of running actions
    context['actions'] = current_actions # add actions to context
    scan_folder = get_object_or_404(MediaFolder) # top level media folder
    context['scan_folder'] = scan_folder
    log.debug("home view context:" + str(context))
    return render(request, 'sorter/index.html', context)


def config(request): # The configuration view
    configuration_list = Configuration.objects.all()
    # Filter the display list to only configuration types not media types
    config_type_list = Type.objects.filter(code__startswith='config')
    context = {
               'configuration_list': configuration_list,
               'type_list': config_type_list,
               }
    log.debug("config view context:" + str(context))
    return render(request, 'sorter/configuration.html', context)


def editconfig(request): # The view for handling configuration changes
    newkey = request.POST['newkey']
    newvalue = request.POST['newvalue']
    newtype_id = request.POST['newtype']
    if newkey is not None and newvalue is not None and newtype_id is not None:
        newconfig = Configuration(key=newkey, \
                                  value=newvalue, \
                                  type=Type.objects.get(pk=newtype_id))
        newconfig.save()
    return config(request)

def setup(request):
    context = {}
    if request.method == 'POST': # A form has been submitted
        form = SetupForm(request.POST) # Create a form bound to POST data
        log.debug("setup view form:" + str(form))
        log.debug("is form valid?" + str(form.is_valid()))
        if form.is_valid(): # All validation rules passed, form is valid
            f = form.cleaned_data # Process cleaned data
            media_folder = MediaFolder(folder=f['scan_folder'])
            media_folder.save()
            app_config_type = get_object_or_404(Type, code='config.app') 
            destination_folder = Configuration(key='destination.folder', \
                                               value=f['destination_folder'], \
                                               type=app_config_type)
            destination_folder.save()
            return home(request)
        else: # Form has some errors
            pass
    else: # No form has been submitted this is a view action
        form = SetupForm() # Create an empty form
    context['form'] = form
    log.debug("setup view context:" + str(context))
    return render(request, 'sorter/setup.html', context)

def scan(request, folder_id):
    context = {}
    log.debug("Starting scan of folder: " + folder_id)
    return home(request)

