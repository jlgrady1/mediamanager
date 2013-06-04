############
Requirements
############

The current requirements for Media Manager are:

* Django >= 1.5
* Celery >= 2.2.8
* RabbitMQ >= 3.1
* FileBot >= 3.6
* Java Runtime >= 1.6
* pyyaml

-----------------------
Installing Requirements
-----------------------

RabbitMQ requires EPEL repository to be set up. To install the EPEL Repo grab
the latest 
`EPEL Repo rpm <http://fedora-epel.mirror.lstn.net/6/i386/repoview/epel-release.html>`_
and install it.::

    wget http://fedora-epel.mirror.lstn.net/6/i386/epel-release-6-8.noarch.rpm
    sudo yum install epel-release-6-8.noarch.rpm

Next install the latest RabbitMQ-Server::

    sudo yum install rabbitmq-server

Install python pip for python packages::

    sudo yum install python-pip

Install celery from pip, no the EPEL repo. It can be installed with::

    sudo pip-python install celery

Install pyyaml from pip::

    sudo pip-python install pyyaml

FileBot is a program for automatically renaming T.V. shows from various T.V.
databases. The commnad line version is required for Media Manager. The filebot
executable must be in the path or set in the application config.
