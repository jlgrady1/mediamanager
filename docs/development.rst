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
