==============
Custom context
==============

Another important functionality of this package, is to use a custom context to preview your templates.

The context file it's stored inside the *data* folder, where are the source templates. It's a python file, named
*context.py* which contain a dictionary, also named *context*.

.. note:: The python dictionary it's more powerful that a json file, for example. It allows you to define date objects, reuse
   another attributes, etc.

The dictionary must contain two leveled keys. The first level it's for the folder name, and the child, for file name.

For example::

    {
        "example_folder": {
            "body.html": {
                "name": "Demo Name"
            }
        }
    }

Now, if in your template, placed in *example_folder/body.html*, contains::

    Hello \{{ name }}!


.. note:: Notice that the brackets need to be escaped because we are using *inky* and it conflicts with *jinja2*.
 We must translate our *jinja2* tags to the built-in django template.

You will see the following result in the template preview view::

    Hello Demo Name!


This is very useful for your designers to work on the template directly.
