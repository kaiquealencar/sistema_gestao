from django import forms

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for name, field in self.fields.items():
          widget = field.widget

          if isinstance(widget, forms.CheckboxInput):
              widget.attrs["class"] = "form-check-input"
          elif isinstance(widget, forms.Select):
              widget.attrs["class"] = "form-select"
          elif isinstance(widget, forms.Textarea):
              widget.attrs.update({
                  "class": "form-control",
                  "placeholder": field.label
              })
          else:
              css = "form-control"
              if self.is_bound and self.errors.get(name):
                  css += " is-invalid"
              widget.attrs.update({
                  "class": css,
                  "placeholder": field.label
              })
              
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
      
              
    