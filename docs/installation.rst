============
Installation
============

You can find the package on `PyPI`_ and it can then be installed using `pip`::

    pip install django-email-foundation

You can also download the .zip distribution file and unpack it or download the sources. Inside this zip, you can find a script
file named ``setup.py``. Enter this command::

   python setup.py install

...and the package will be installed automatically.

.. _PyPI: https://pypi.org/project/django-email-foundation/
.. _`pip`: https://pip.pypa.io/en/stable/

Configuration
=============

This package has been tested on:

* Python: 3.6.7
* Django: 2.1.7
* npm: 5.8.0
* yarn: 1.13.0
* node: 8.11.4

In your Django project's settings, add the package to your *INSTALLED_APPS*::

    INSTALLED_APPS = (
        ...
        'django_email_foundation',
    )

It is also necessary to add the *def* urls in your project. Edit your main *urls.py* and add::

    urlpatterns = [
        ...
        path('def/', include('django_email_foundation.urls')),
    ]


Below you can seea list of all available settings which can be added to your Django settings configuration. Notice that
these constants start with *DEF* (Django Email Foundation).

Required settings
=================

These settings are required and necessary to use any of the *def* commands.

**DEF_TEMPLATES_SOURCE_PATH**

It refers to the relative path from your root project where your email sources templates are located. For example, if you have the
following folder's tree::

    my_project
    ├── readme.md
    └── src
        ├── emails_app
        │   ├── models.py
        │   ├── templates
        │   │   └── emails_app
        │   ├── templates_sources
        │   │   ├── assets
        │   │   ├── helpers
        │   │   ├── layouts
        │   │   ├── pages
        │   │   └── partials
        │   └── views.py
        └── manage.py

Them the constant should be::

    DEF_TEMPLATES_SOURCE_PATH = 'src/emails_app/templates_sources'


.. note:: The paths must be relative from the root project

**DEF_TEMPLATES_TARGET_PATH**

It refers to the path where the compiled email templates are stored. For example, from the previous example::

    DEF_TEMPLATES_TARGET_PATH = 'src/emails_app/templates/emails_app'

**DEF_STATIC_TARGET_PATH**

Necessary for set where store the static files (images) in to the target path. Example::

    DEF_STATIC_TARGET_PATH = 'src/emails_app/static/emails_app'

Optional settings
=================

The optional settings can be used when you want to override the default values.

**DEF_NPM_OR_YARN**

It allows you to set which node package's system will be used for installing the dependencies. Default optoin is **yarn** but you can replace with **npm**.

**DEF_NODE_MODULES_PATH**

The path where the node packages will be installed. The *node_modules* folder, by default will be created at the project root folder. Do not include *node_modules* in this setting. For example::

    DEF_NODE_MODULES_PATH = '/home/my-user/workspace/my-project'

**DEF_IGNORE_FILES**

A list (or tuple) of files that will not be built with *panini* when the *email_builder* command is running.
However they will be moved at the target folder path.

By default there are two files, *subject.html* and *body.txt*.

For example you could have the following scenario::

    templates_sources
    ├── assets
    ├── helpers
    ├── layouts
    ├── pages
    │   └── user_account_validation
    │       ├── body.html
    │       ├── body.txt
    │       └── subject.html
    └── partials


You may only want to compile the *body.html* file but not the other two. Although you want to move it to the destination folder.

**DEF_RUNSERVER_HOST**

By default *http://localhost:8000*. Change it if your project runs on another host or port.
