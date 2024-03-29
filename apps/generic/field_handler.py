
import django.forms



class FieldHandler():
    formfields = {}
    def __init__(self, fields):
        for field in fields:
            options = self.get_options(field)
            f = getattr(self, "create_field_for_"+field['type'] )(field, options)
            self.formfields[field['name']] = f

    def get_options(self, field):
        options = {}
        options['label'] = field['label']
        options['help_text'] = field.get("help_text", None)
        options['required'] = bool(field.get("required", 0) )
        return options

    def create_field_for_text(self, field, options):
        options['max_length'] = int(field.get("max_length", "20") )
        return django.forms.CharField(**options)

    def create_field_for_textarea(self, field, options):
        options['max_length'] = int(field.get("max_value", "9999") )
        return django.forms.CharField(widget=django.forms.Textarea, **options)

    def create_field_for_integer(self, field, options):
        options['max_value'] = int(field.get("max_value", "999999999") )
        options['min_value'] = int(field.get("min_value", "-999999999") )
        return django.forms.IntegerField(**options)

    def create_field_for_radio(self, field, options):
        options['choices'] = [ (c['value'], c['name'] ) for c in field['choices'] ]
        return django.forms.ChoiceField(widget=django.forms.RadioSelect,   **options)

    def create_field_for_select(self, field, options):
        options['choices']  = [ (c['value'], c['name'] ) for c in field['choices'] ]
        return django.forms.ChoiceField(  **options)

    def create_field_for_checkbox(self, field, options):
        return django.forms.BooleanField(widget=django.forms.CheckboxInput, **options)

    def create_field_for_image(self, field, options):
        return django.forms.ImageField(widget=django.forms.ImageField, **options)


# Field Loader
# import json
# fields=json.loads(json_fields)

# Creating Actual Fields
# def get_form(jstr):
#     fields=json.loads(jstr)
#     fh = FieldHandler(fields)
#     return type('DynaForm', (django.forms.Form,), fh.formfields )


# import dynaform

# def dform(request):
#     json_form = get_json_form_from_somewhere()
#     form_class = dynaform.get_form(json_form)
#     data = {}
#     if request.method == 'POST':
#         form = form_class(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#     else:
#         form = form_class()

#     return render_to_response( "dform.html", {
#         'form': form,  'data': data,
#     }, RequestContext(request) )