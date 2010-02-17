# DjEditArea copyright (c) Aditya Bhargava @ wefoundland.com
# EditArea copyright (c) Christophe Dolivet @ cdolivet.com
# Licensed under the LGPL.

"""
Django-EditArea adds syntax highlighting. Use EditAreaField instead of TextField in your models to add real-time syntax highlighting to that particular field.
"""

from django.conf import settings
from django.forms import *
from django.forms.widgets import flatatt
from django.utils.encoding import smart_unicode
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
    
    Another option that you can specify in settings.py is EDITAREA_DEFAULT_ARGS
    This attribute should be a function that gets 'textarea_id' as an
    only argument and returns a string containing a valid JavaScript 
    code that is used as an argument for editAreaLoader.init inside  
    the template. If it is not defined, then default editarea settings
    will be used. Common example of that would be:
    
    EDITAREA_DEFAULT_ARGS = lambda textarea_id:\
        '{ id: "'+textarea_id+'", syntax: "html", start_highlight: true }'
    
    Note: If this function returns a falsy value, then editAreaLoader.init
    is not called automatically and you should init it inside the template.
    This comes handy when you need to call editAreaLoader.init with options
    depending on other variables than just 'textarea_id'.  
    
    See EditArea documentation for all possible editAreaLoader.init arguments:
        http://www.cdolivet.com/editarea/editarea/docs/
    
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
        textarea_id = self.settings['id'] = "id_{0}".format(name)
        
        try:
            js_url = settings.EDITAREA_JS_FOLDER
        except AttributeError:
            js_url = settings.MEDIA_URL + "js/"
        
        try:
            default_editarea_args =\
                settings.EDITAREA_DEFAULT_ARGS(textarea_id)
        except AttributeError:
            default_editarea_args = '{id : "' + textarea_id + '" }'
            
        editarea_args = default_editarea_args
        init_script = '' if not editarea_args else\
        "<script>"\
            "editAreaLoader.init("+editarea_args+");"\
        "</script>"
            
        return mark_safe(u"""
        <textarea{final_attrs}>{value}</textarea>
        <script src="{js_url}editarea/edit_area_loader.js"></script>
        """.format(final_attrs=flatatt(final_attrs),
                   value=escape(value),
                   js_url=js_url)
        + init_script
        )

# Custom Fields
from django.db import models
class EditAreaField(models.TextField):
    description = "Same as the standard TextField field, but with syntax highlighting."
    def formfield(self, **kwargs):
        defaults = {}
        defaults.update(kwargs)
        defaults['widget'] = EditArea()
        return super(EditAreaField, self).formfield(**defaults)