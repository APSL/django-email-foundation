django-email-foundation
=======================

.. image:: https://travis-ci.org/APSL/django-email-foundation.svg
    :target: https://travis-ci.org/APSL/django-email-foundation

.. image:: https://img.shields.io/pypi/v/django-email-foundation.svg
  :target: https://pypi.python.org/pypi/django-email-foundation

.. image:: https://readthedocs.org/projects/django-email-foundation/badge/?version=latest
  :target: http://django-email-foundation.readthedocs.org/en/latest/?badge=latest
  :alt: Documentation Status

Package that helps you build email templates easier in your projects.

Description
-----------

It's a Django package that helps you to build email templates for your email engine sender (we recommend you to use `django-yubin`_).
It uses the `zurb foundation for emails`_ templates and `node` packages such as `inky` or `panini`.

.. _django-yubin: https://github.com/APSL/django-yubin
.. _zurb foundation for emails: https://foundation.zurb.com/emails/docs/

This gives you some commands and functionality to integrate *zurb foundation for emails* in your Django project.

* *install_requires*: A command for install the required node packages, such as *inky*, *panini*, *gulp*, etc., in your project.
* *create_basic_structure*: It creates in your project an essential folder tree which contains the basic layout and folders
  such as *pages*, *helpers* and *partials*, used by panini_.
* *email_builder*: Run a *gulp* process to watch your source templates, build and move to your target email folder. It compiles
  the sources using panini_ and inky_ for the best compatibility with the major email clients.

Also, it gives you a Django view to preview the build templates and use a custom fixed context for each one, useful for your
designers that may edit the layouts.

.. _panini: https://www.npmjs.com/package/panini
.. _inky: https://www.npmjs.com/package/inky

Documentation
-------------

Please read the full documentation at readthedocs_.

.. _readthedocs: http://django-email-foundation.readthedocs.org/en/latest/

