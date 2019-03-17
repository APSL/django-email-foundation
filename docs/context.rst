==============
Custom context
==============

Another important functionality of this package, is to use a custom context to preview your template.

For example, imagine you have this text in your template placed at *example_folder/body.html*::

    Hello \{{ name }}!


.. note:: Notice that the brackets need to be escaped because we are using *inky* and it conflicts with *jinja2*.
 We must translate our *jinja2* tags to the built-in django template.

In your foundation source templates, it's automatically created a *data* folder width a *context.json* file inside.
In this file, you can define a custom context for your templates, where the first key it's your template folder name,
and the second, the filename. For example::

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
