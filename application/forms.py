from django import forms


class AvailabilityForm(forms.Form):
    Tables = (

        ('Single', 'Single'),
        ('Small', 'Two-Seats'),
        ('Medium', 'Four-Seats'),
        ('Large', 'Six-Seats'),

    )
    table_category = forms.TypedChoiceField(choices=Tables,  required=True)
    check_in = forms.DateField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
