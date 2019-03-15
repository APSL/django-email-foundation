.. django-email-foundation documentation master file, created by
   sphinx-quickstart on Mon Mar 11 23:49:58 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=======================
django-email-foundation
=======================

Description
===========

It's a Django package that help you to build email templates for your email engine sender (we recommend you `django-yubin`_).
It use the `zurb foundation for emails`_ templates and *node* packages such as *inky* or *panini*.

.. _django-yubin: https://github.com/APSL/django-yubin
.. _zurb foundation for emails: https://foundation.zurb.com/emails/docs/

This gives you some commands and functionality for integrate *zurb foundation for emails* in your django project.

* *install_requires*: A command for install the required node packages, such as *inky*, *panini*, *gulp*, etc in your project.
* *create_basic_structure*: It creates in your project an essential tree folder which contains the basic layout and folders
  such as *pages*, *helpers* and *partials*, used by panini_.
* *email_builder*: Run a *gulp* process for watch your source templates, build and move to your target email folder. It compiles
  the sources using panini_ and inky_ for the best compatibility with the major email's client.

Also give you a django view for preview the build templates and use a custom fixed context for each one, useful for your
designers may to edit the layouts.

.. _panini: https://www.npmjs.com/package/panini
.. _inky: https://www.npmjs.com/package/inky

Index
=====

.. toctree::

   installation
   commands
   preview
   context
   contributing

