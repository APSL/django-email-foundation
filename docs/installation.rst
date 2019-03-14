============
Installation
============

You can found the package in the `PyPI`_ and install it using `pip`::

    pip install django-email-foundation

You can also download the .zip distribution file and unpack it or download the sources. Inside is a script
named ``setup.py``. Enter this command::

   python setup.py install

...and the package will be installed automatically.

.. _PyPI: https://pypi.org/project/django-email-foundation/
.. _`pip`: https://pip.pypa.io/en/stable/

Configuration
=============

In your Django project's settings, add the package in your *INSTALLED_APPS*::

    INSTALLED_APPS = (
        ...
        'django_email_foundation',
    )

Also it's necessary to add the *def* urls in your project, editing your main *urls.py* and adding::

    urlpatterns = [
        ...
        path('def/', include('django_email_foundation.urls')),
    ]


Following is a list of all available settings which can be added to your Django settings configuration. Notice you that
all constants starts by *DEF* (Django Email Foundation).

Required settings
=================

These settings are required and necessaries for use any *def* command.

**DEF_TEMPLATES_SOURCE_PATH**

It's the relative path from your root project where are your email sources templates. For example, if you have the
follow folder's tree::

    my_projcet
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

The constance's values must be::

    DEF_TEMPLATES_SOURCE_PATH = 'emails_app/templates_sources'

**DEF_TEMPLATES_TARGET_PATH**

The path where store the compiled email templates. For example, from the previous example::

    DEF_TEMPLATES_TARGET_PATH = 'emails_app/templates/emails_app'

Optional settings
=================

The optional settings can be used if you does not want to use the default values.

**DEF_NPM_OR_YARN**

Allows you to set which node package's system use for install the dependencies. By default is **yarn** but you can
replace by **npm**.

**DEF_NODE_MODULES_PATH**

The path where the node packages will be installed. The *node_modules* folder, where by default is your project root folder.
It's not necessary to define thde *nod_modules* folder. For example::

    DEF_NODE_MODULES_PATH = '/home/my-user/workspace/my-project'

**DEF_IGNORE_FILES**

A list (or touple) of files taht will not been builded with *panini* when the *email_builder* command be runing.
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


You only want to compile the *body.html* file but not the other two. Altough you want to move it to the destination folder.

**DEF_RUNSERVER_HOST**

By default *http://localhost:8000*. Change it if you run your project in another host or port.

**DEF_CONTEXT_JSON_FILE**

Another usefull functionality is to use a custom context for each email template, only for previews. This constant
allows you define where is this file.

Take a look the documentation about the custom context.
