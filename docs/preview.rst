==========================
Previewing build templates
==========================

If everything is ok and the *email_builder* command is up and running, the following view will open:

.. image:: _static/preview.png

.. note:: For the previous screenshot, we have the following source and target templates.

Sources::

    foundation_templates
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
    │   └── account_verification
    │       ├── body.html
    │       ├── body.txt
    │       └── subject.html
    └── partials

Target::

    templates
    └── emails
        └── account_verification
            ├── body.html
            ├── body.txt
            └── subject.html

The preview view contains a list of all build templates. You can click on each one and to see the template rendered using your custom context.
