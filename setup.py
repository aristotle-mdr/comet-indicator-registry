import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-aristotle-comet-indicator-registry',
    version='0.1',
    packages=['comet'],
    include_package_data=True,
    license='BSD Licence',
    description='The Comet Indicator Registry is an extension for the Aristotle Metadata Registry to support the specialised needs of health management registries.',
    long_description=README,
    url='http://github.com/LegoStormtroopr/comet-indicator-registry/',
    author='Samuel Spencer',
    author_email='sam@sqbl.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires = [
        'django-aristotle-metadata-registry'
    ]
)
