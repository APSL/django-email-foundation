==============
Custom context
==============

Another important functionality of this package, is to use a custom context for preview your build template.

For example, you have this text in your template place at *example_folder/body.html*::

    Hello \{{ name }}!


.. note:: Notice that we are escaping the brackets because we are using *inky* and there are
   conflicts with *jinja2*. We must to translate our *jinja2* tags to the build django template.

And defined your DEF_CONTEXT_JSON_FILE setting such as::

    DEF_CONTEXT_JSON_FILE = os.path.join(os.getcwd(), 'email_custom_context.json')

And the content::

    {
        "example_folder": {
            "body.html": {
                "name": "Demo Name"
            }
        }
    }

You will see in your preview view::

    Hello Demo Name!


Very useful for your designers may format the template.
