==============
Custom context
==============

Another important functionality of this package, is to use a custom context to preview your template.

For example, imagine you have this text in your template placed at *example_folder/body.html*::

    Hello \{{ name }}!


.. note:: Notice that the brackets need to be escaped because we are using *inky* and it conflicts with *jinja2*.
 We must translate our *jinja2* tags to the built-in django template.

Your DEF_CONTEXT_JSON_FILE setting if defined like this::

    DEF_CONTEXT_JSON_FILE = 'emails_app/email_custom_context.json'

.. note:: The paths must be relative from the root project.

And the content::

    {
        "example_folder": {
            "body.html": {
                "name": "Demo Name"
            }
        }
    }

In your preview view, you will then see::

    Hello Demo Name!


This is very useful because it will allow your designers to work on the template directly.
