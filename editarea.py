# DjEditArea copyright (c) Aditya Bhargava @ wefoundland.com
# EditArea copyright (c) Christophe Dolivet @ cdolivet.com
# Licensed under the LGPL.

"""
Django-EditArea adds syntax highlighting. Use EditAreaField instead of TextField in your models to add real-time syntax highlighting to that particular field.
"""

from django.conf import settings
from django.forms import *
from django.forms.widgets import flatatt
from django.forms.util import smart_unicode
from django.utils.html import escape
from django.utils.simplejson import *
from django.utils.safestring import mark_safe
        
class EditArea(Textarea):
	"""
	EditArea widget. Place the corresponding 'editarea' folder containing
	the editarea JavaScript files in a folder called 'js' in your media root.
	If you would like to put them in another folder, specify a EDITAREA_JS_FOLDER
	variable in settings.py that contains the path to that folder. For example:
	
	EDITAREA_JS_FOLDER = "/path/to/my/project/app/media/scripts/"
	
	*Dont forget the trailing slash.*
	"""

	settings = {}
	def update_settings(self, custom):
	    return_dict = self.settings.copy()
	    return_dict.update(custom)
	    return return_dict
	
	def render(self, name, value, attrs=None):
 		if value is None: value = ''
		value = smart_unicode(value)
		final_attrs = self.build_attrs(attrs, name=name)
		textarea_id = self.settings['id'] = "id_%s" % name
		
		try:
			js_url = settings.EDITAREA_JS_FOLDER
		except AttributeError:
			js_url = settings.MEDIA_URL + "js/"
		
		return mark_safe(u"""
		<textarea%s>%s</textarea>
		<script src="%seditarea/edit_area_loader.js"></script>
		<script>
			editAreaLoader.init({
				id : "%s"		// textarea id
				,syntax: "html"			// syntax to be uses for highgliting
				,start_highlight: true		// to display with highlight mode on start-up
				,min_width: 700
				,min_height: 250
				,word_wrap: true
				});
		</script>
		""" % (flatatt(final_attrs), escape(value),js_url,textarea_id))


# Custom Fields
from django.db import models
class EditAreaField(models.TextField):
	description = "Same as the standard TextField field, but with syntax highlighting."
	def formfield(self, **kwargs):
		defaults = {}
		defaults.update(kwargs)
  		defaults['widget'] = EditArea()
 		return super(EditAreaField, self).formfield(**defaults)