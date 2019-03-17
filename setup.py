import re

from setuptools import setup

package = open('django_email_foundation/__init__.py').read()
metadata = dict(re.findall("__([A-Z]+)__ = '([^']+)'", package))
__VERSION__ = metadata['VERSION']

with open('docs/index.rst') as docs_index:
    long_description = docs_index.read()

# Requirements
INSTALL_REQUIRES = (
)

TEST_REQUIREMENTS = (
    'pytest==4.3.1',
    'pytest-flake8==1.0.4',
)

setup(
    name='django-email-foundation',
    version=__VERSION__,
    description='django-email-foundation is a Django package for help you to create emails using '
                'the "zurb foundation" technologies',
    long_description=long_description,
    author='Francesc Arpí',
    author_email='francesc.arpi@gmail.com',
    url='http://github.com/APSL/django-email-foundation',
    install_requires=INSTALL_REQUIRES,
    packages=[
        'django_email_foundation',
    ],
    include_package_data=True,
    # tests
    tests_require=TEST_REQUIREMENTS,
    test_suite='pytest',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
    ]
)
