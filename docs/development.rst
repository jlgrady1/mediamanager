===========
Development
===========

This section will provide information on the current development of Media
Manager. Media Manager is currently in development for release 0.5. This
release of the program will include the following functionality:

* Scan a download folder for a set of media files
    * Support for only video files will be included in this version
    * Add the discovered media files to the database
    * Determine a series of actions to be performed on those files
        * Supported actions include:
            * Rename
                * Renaming will be performed using FileBot CLI and the TVDB
            * Convert
                * Conversion will be handled using HandbrakeCLI
                * Conversion settings will be configurable
            * Organize
                * Organization will be handled using a destination folder with
                  a specified folder structure

There is no development or release schedule for this project. This project is
designed to be a hobby project.

The sections below can be used to follow the status of the project

------------------------
Basic Flow of operations
------------------------
# Download Manager scans a folder for new files
# New files are put into the database with the action of pending

^^^^^^^^^^^^
Status Types
^^^^^^^^^^^^
**pending**
    A file has been found in the scan folder, the type has been identified, 
    but no processing has occurred. If a file is not a video file it is
    currently changed to directly to the move status.

**convert**
    The file is being converted from the download video format to the format
    specified in the configuration. If no configuration is specified, the
    conversion will default to (x264,faac,mp4).
    
    *This action is only supported on video files* 

**rename**
    The file is being renamed based looking the filename up in the TVDB. This
    action is automatic. If the action succeed the file is renamed and the
    action transitions to move. If the action fails, the process will try
    looking the file up in the movie db.

    *This action is only supported on video files*

**move**
    The file is being moved from is current location to the destination folder.
    The destination folder is specified by the user in the configuration. There
    is also a temporary file optionally specified in the configuration where
    files are stored while running operations. This will default to 
    <installation_folder>/tmp if this is not defined. There are several
    subfolders used by the manager in the temporary folder which include:

    (.pending, .convert, .originals)

---------------
Completed Tasks
---------------
There are currently no completed tasks.

* Complete database design
* Import Twitter bootstrap into Django for styling

-------------
Current Tasks
-------------
The following tasks are those that are actively being worked.

* Sketch wireframes for dashboard page

------------
Future Tasks
------------
The following are tasks that are planned for later.

* Sketch wireframes for tasks/actions page
* Sketch wireframes for configuration page
* Sketch wireframes for history page
* TBD
