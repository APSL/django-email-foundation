import os

from django.conf import settings

# Define witch installer application you want to use, "yarn" or "npm".
DEF_NPM_OR_YARN = getattr(settings, 'DEF_NPM_OR_YARN', 'yarn')

# If the installer is "npm", use the "install" command.
DEF_INSTALL_COMMANDS = {
    'npm': 'install',
    'yarn': 'add',
}

DEF_NPM_YARN_INSTALL_COMMAND = DEF_INSTALL_COMMANDS[DEF_NPM_OR_YARN]

# Define where to install the node modules packages (the node_modules folder). By default is at project root.
DEF_NODE_MODULES_PATH = getattr(settings, 'DEF_NODE_MODULES_PATH', os.getcwd())

# A list with a node modules required packages
DEF_NODE_PACKAGES_REQUIRED = (
    'gulp@4.0.0',
    'panini@1.3.0',
    'inky@1.3.6',
    'gulp-open@3.0.1',
    'gulp-debug@4.0.0',
)

# Path for email templates. This settings is required for start run the email builder.
DEF_TEMPLATES_SOURCE_PATH = getattr(settings, 'DEF_TEMPLATES_SOURCE_PATH', None)

# Path where store the compiles templates
DEF_TEMPLATES_TARGET_PATH = getattr(settings, 'DEF_TEMPLATES_TARGET_PATH', None)

# List of ignored templates.
DEF_IGNORE_FILES = getattr(settings, 'DEF_IGNORE_FILES', (
    'subject.html',
    'body.txt',
))

# The default runserver host for preview
DEF_RUNSERVER_HOST = getattr(settings, 'DEF_RUNSERVER_HOST', 'http://localhost:8000')

# Allows to define where is the json file which contain the context for emails.
DEF_CONTEXT_JSON_FILE = getattr(settings, 'DEF_CONTEXT_JSON_FILE', None)
