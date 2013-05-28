############
Requirements
############

The current requirements for Media Manager are:

* Django >= 1.5
* Celery >= 2.2.8
* RabbitMQ >= 3.1

-----------------------
Installing Requirements
-----------------------

RabbitMQ requires EPEL repository to be set up. To install the EPEL Repo grab
the latest 
`EPEL Repo rpm <http://fedora-epel.mirror.lstn.net/6/i386/repoview/epel-release.html>`_
and install it.::

    wget http://fedora-epel.mirror.lstn.net/6/i386/epel-release-6-8.noarch.rpm
    sudo yum install pel-release-6-8.noarch.rpm

Next install the latest RabbitMQ-Server::

    sudo yum install rabbitmq-server

Install python pip for python packages::

    sudo yum install python-pip

Install celery from pip, no the EPEL repo. It can be installed with::

    sudo pip-python install celery

