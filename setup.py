#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "Django-EditArea",
    version = "1.0",
	py_modules=['editarea'],
    author = "Aditya Bhargava",
    author_email = "aditya@wefoundland.com",
    description = "A Django application that contains a widget to render a form field as an EditArea editor.",
    long_description = """
    Django-EditArea is a widget for Django. It adds HTML syntax highlighting to
    TextField fields on the admin side. 
	
	Django-EditArea is based on EditArea, so it has a whole bunch of features:
	
	* Real-time syntax highlighting
	* Search and replace (with regular expressions too!)
	* Auto-indenting
	* Line numbering
	* Full screen mode
	* Very easy to add to a new site or an existing one - no complicated setup""",
    license = "LGPL License",
    keywords = "django widget editarea syntax highlight highlighting",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms = ['any'],
    url = "http://www.wefoundland.com/project/Django-EditArea",
    download_url = "http://www.wefoundland.com/project/Django-EditArea/Django-EditArea-1.0.tar.gz",
)
