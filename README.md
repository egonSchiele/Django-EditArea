# Django-EditArea

Django-EditArea is a widget for Django. It adds syntax highlighting to `TextField` fields on the admin side. 

**This project is looking for a new maintainer! Please let me know if you'd like to maintain the project.**


# Features

Django-EditArea is based on EditArea, so it has a whole bunch of features:

* Real-time syntax highlighting
* Search and replace (with regular expressions too!)
* Auto-indenting
* Line numbering
* Full screen mode
* Works alongside popular javascript libraries
* Can be used as a widget in forms
* Very easy to add to a new site or an existing one -- no complicated setup

# Screenshot
![django-editarea screenshot](http://static.adit.io/images/django_editarea.png)

# Installation

Place `editarea.py` in your Python path. The easiest way to do this is to run `setup.py` by using:

	python setup.py install


Place the editarea folder inside a folder called 'js' in the media root of your project. You can override this location by setting the `EDITAREA_JS_FOLDER` variable (see below).

# Usage

Django-EditArea is designed to be easy to use. It defines a new type of field: `EditAreaField`. `EditAreaFields` are exactly the same as `TextFields`, except that they automatically provide html syntax highlighting.
To use Django-EditArea, first import it in `models.py`. Then, use `EditAreaField` instead of `TextField` for attributes where you want syntax highlighting.
If you are working on an existing project, you can just replace all `TextField` fields with `EditAreaField` fields. Since `EditAreaField` inherits from `TextField`, you won't lose anything.

# Example

Here's a simple model that has an EditAreaField field:

	from django.db import models
	import editarea
	
	# Create your models here.
	class Page(models.Model):
		name    = models.CharField(max_length=128)
		content = editarea.EditAreaField()
	

# Overriding the js folder

Normally, you need to put the included editarea folder inside a folder called 'js' inside your media root. If you want to put the editarea folder in a different location, add a variable `EDITAREA_JS_FOLDER` to `settings.py` that contains the absolute url to the location. Example:

	EDITAREA_JS_FOLDER = "/path/to/my/project/app/media/scripts/"

**Dont forget the trailing slash.**

This should be the path to the folder that contains the editarea folder. i.e. dont include `/editarea/` at the end unless the folder containing the editarea folder is also called editarea.

# Credits

Django-EditArea copyright (c) [Aditya Bhargava](http://adit.io)

EditArea copyright (c) [Christophe Dolivet](http://cdolivet.com)

# Contributors
Marcin Biernat

# License
LGPL
