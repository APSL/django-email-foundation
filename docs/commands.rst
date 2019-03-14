========
Commands
========

There are available three important commands that you can use.

email_builder
-------------

This command lunch a *gulp* process and watch your source files for compile it using panini + inky.

How execute it::

    ./manage.py email_builder

If you run this command at first time and you does not have configuret your project yet, you will see something like that::

    → ./manage.py email_builder
    Oops! Something was wrong...
      - Some required modules are not installed in "node_modules". Please run "./manage.py install_requires"
      - Is necessary to define the DEF_TEMPLATES_SOURCE_PATH in your settings
      - The templates directory must have a valid structure. It must contain the pages, layouts, partials and helpers folders. You can run ".manage.py create_basic_structure" for create its and add a basic layout.
      - Is necessary to define the DEF_TEMPLATES_TARGET_PATH in your settings

This is because the command make some checks before run. For example, checks that you already have the required node
packages, or defined the required constants in your settings, etc.

If everything it's ok, you'll see something like that:

.. image:: _static/email_builder.png

install_requires
----------------

It install the required node packages, such as *gulp*, *panini* or *inky* using *npm* or *yarn*, depends on your configuraiton.

How execute it::

    ./manage.py install_requires

Remember that this command will create the *node_modules* folder, the *package.json* file and *yarn.lock* or *package.lock*.
If already exists, the command will only update the folders or the locked files.

If you don't want to add this folders and files in your repository, don't forget to add it in the *.gitignore* file.

create_basic_structure
----------------------

It creates a basic tree sctructure in your templates source path like the follow::

    templates_sources
    ├── assets
    │   └── scss
    │       ├── app.scss
    │       ├── _settings.scss
    │       └── template
    │           └── _template.scss
    ├── helpers
    ├── layouts
    │   └── default.html
    ├── pages
    └── partials

It allows you to start on create your self templates inside the *pages* folder. Take a look to the official documentation_.
We recomend you to use the inky_ template language for make more easy your live ;).

.. _documentation: https://foundation.zurb.com/emails/docs/
.. _inky: https://foundation.zurb.com/emails/docs/inky.html

