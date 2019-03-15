.. django-email-foundation documentation master file, created by
   sphinx-quickstart on Mon Mar 11 23:49:58 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=======================
django-email-foundation
=======================

Description
===========

This is a Django package that helps you build email templates for your email engine sender (we recommend you use `django-yubin`_).
It uses the `zurb foundation for emails`_ templates and *node* packages such as *inky* or *panini*.

.. _django-yubin: https://github.com/APSL/django-yubin
.. _zurb foundation for emails: https://foundation.zurb.com/emails/docs/

It provides you with some commands and functionality to integrate *zurb foundation for emails* in your django project.

* *install_requires*: A command to install the required node packages, such as *inky*, *panini*, *gulp*, etc in your project.
* *create_basic_structure*: It creates an essential tree structure in your project, that contains the basic layout and folders
  such as *pages*, *helpers* and *partials*, used by panini_.
* *email_builder*: Starts a *gulp* process that watches your source templates, builds them and finally copies them to your target email folder. It compiles  the sources using panini_ and inky_ for the best compatibility with the major email's client.

It also gives you a django view to preview the generated templates. For the preview, you can use a custom fixed context for each template, and this is very useful because it allows designers to edit the layouts.

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

