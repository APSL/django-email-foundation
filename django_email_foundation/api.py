import os
import subprocess
from shutil import which, copyfile, copytree
from typing import Union, List, Dict, Optional

from django.urls import reverse
from django_email_foundation import settings


class Checks:
    FOLDERS = ('pages', 'layouts', 'partials', 'helpers', 'assets')

    CHECKS = (
        ('npm_or_yarn_installed', 'The "npm" or "yarn" is not installed or is not in your $PATH'),
        ('required_node_packages', 'Some of the required modules are not installed in "node_modules". Please run '
                                   '"./manage.py install_requires"'),
        ('templates_source_path', 'It is necessary to define DEF_TEMPLATES_SOURCE_PATH in your settings'),
        ('templates_dir_structure', 'The templates directory must have a valid structure. It must contain the pages,'
                                    ' layouts, partials and helpers folders. You can run '
                                    '".manage.py create_basic_structure" to build this structure, '
                                    'and to add a basic layout '),
        ('templates_target_path', 'It is necessary to define DEF_TEMPLATES_TARGET_PATH in your settings'),
    )

    def npm_or_yarn_installed(self) -> bool:
        """
        It checks if the npm or yarn is installed in your system path.
        :return:
        """
        return bool(which(settings.DEF_NPM_OR_YARN))

    def required_node_packages(self) -> bool:
        """
        Iterate the required node packages list and check if are installed in your node_modules folder.
        :return:
        """
        for required_package in settings.DEF_NODE_PACKAGES_REQUIRED:
            name = required_package.split('@')[0]
            if not os.path.isdir('{}/node_modules/{}'.format(settings.DEF_NODE_MODULES_PATH, name)):
                return False
        return True

    def templates_source_path(self) -> bool:
        """
        Check if you have the source path in your settings.
        :return:
        """
        return bool(settings.DEF_TEMPLATES_SOURCE_PATH)

    def templates_target_path(self) -> bool:
        """
        Check if you have the target path in your settings.
        :return:
        """
        return bool(settings.DEF_TEMPLATES_TARGET_PATH)

    @staticmethod
    def get_right_path(path: str) -> str:
        """
        In some cases we could have the manage.py inside the distinct folder where are gulpfile. It's could
        cause problems. We must to detect and return the right source path
        :return:
        """
        current_split = os.getcwd().split('/')
        sources_split = path.split('/')

        if current_split[-1] == sources_split[0]:
            return '/'.join(sources_split[1:])

        return path

    @staticmethod
    def get_templates_source_path() -> str:
        return Checks.get_right_path(settings.DEF_TEMPLATES_SOURCE_PATH)

    @staticmethod
    def get_templates_target_path() -> str:
        return Checks.get_right_path(settings.DEF_TEMPLATES_TARGET_PATH)

    @staticmethod
    def get_context_json_file_path() -> Optional[str]:
        if not settings.DEF_CONTEXT_JSON_FILE:
            return
        return Checks.get_right_path(settings.DEF_CONTEXT_JSON_FILE)

    def exists_folder(self, name: str) -> bool:
        """
        Check if exist the named folder in the source path folder.
        :param name:
        :return:
        """
        full_path = '{}/{}'.format(Checks.get_templates_source_path(), name)
        return os.path.isdir(full_path)

    def templates_dir_structure(self) -> bool:
        """
        Check if you have the right folders inside your source path folder.
        :return:
        """
        for folder in self.FOLDERS:
            if not self.exists_folder(folder):
                return False
        return True

    def start(self) -> List[str]:
        """
        Start to analyze all checks
        :return: A list of error text if exists...
        """
        errors = []
        for method, error_txt in self.CHECKS:
            if not getattr(self, method)():
                errors.append(error_txt)

        return errors


class DjangoEmailFoundation:
    """
    Main API object for manage the library functionality.
    """

    def perform_checks(self) -> Union[bool, List[str]]:
        checks = Checks()
        return checks.start()

    def copy_gulpfile(self):
        """Copy the gulp file to the destination folder, where node_modules is installed"""
        current = os.path.dirname(os.path.realpath(__file__))
        copyfile(os.path.join(current, 'gulpfile.js'),
                 os.path.join(settings.DEF_NODE_MODULES_PATH, 'gulpfile.js'))

    def install_required_packages(self) -> bool:
        """
        Install the foundation noce package and return True if goes right.
        :return: Return the bool success value
        """
        for required_package in settings.DEF_NODE_PACKAGES_REQUIRED:
            command = (
                settings.DEF_NPM_OR_YARN,
                settings.DEF_NPM_YARN_INSTALL_COMMAND,
                required_package,
            )
            pid = subprocess.Popen(command, cwd=settings.DEF_NODE_MODULES_PATH)

            # We wait until installation...
            while True:
                if pid.poll() is not None:
                    break
            exit_code = pid.poll()
            if exit_code != 0:
                return False

        self.copy_gulpfile()

        return True

    @property
    def preview_url(self) -> str:
        host = settings.DEF_RUNSERVER_HOST
        uri = reverse('django_email_foundation:index')
        return '{}{}'.format(host, uri)

    def run_watch(self):
        """
        Run the watch gulp task sending the right parameters, such as where is the source templates, the target, files
        to be ignored, etc.
        :return:
        """
        command = (
            './node_modules/.bin/gulp',
            'watch',
            '--templates_source={}'.format(settings.DEF_TEMPLATES_SOURCE_PATH),
            '--templates_target={}'.format(settings.DEF_TEMPLATES_TARGET_PATH),
            '--ignore_files={}'.format(','.join(settings.DEF_IGNORE_FILES)),
            '--preview_url={}'.format(self.preview_url),
        )
        subprocess.call(command, cwd=settings.DEF_NODE_MODULES_PATH)

    def create_basic_structure(self):
        """
        It creates the basic foundation for emails (or panini) structure in your source path folder.
        :return:
        """
        source_default_templates = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'default_templates')

        for folder in Checks.FOLDERS:
            if self.exists_folder(folder):
                continue

            if os.path.isdir(os.path.join(source_default_templates, folder)):
                copytree(os.path.join(source_default_templates, folder),
                         os.path.join(settings.DEF_TEMPLATES_SOURCE_PATH, folder))
            else:
                os.mkdir(os.path.join(settings.DEF_TEMPLATES_SOURCE_PATH, folder))

    def get_build_files(self) -> Dict[str, List[str]]:
        """
        Read the target folder and return the folders and build files. Useful for send in the preview view context.
        :return:
        """
        response = {}
        for root, dirs, files in os.walk(Checks.get_templates_target_path()):
            folder = root.split('/')[-1]
            if files:
                response[folder] = files
        return response
