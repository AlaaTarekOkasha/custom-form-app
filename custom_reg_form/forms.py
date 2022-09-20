from .models import ExtraInfo
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
import logging


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['day_of_birth'].required = True
        self.fields['month_of_birth'].required = True
        self.fields['country_of_origin'].required = True
        self.fields['country_codes'].required = True
        self.fields['phone_number'].required = True
        

    class Meta(object):
        model = ExtraInfo
        fields = ('day_of_birth', 'month_of_birth', 'country_of_origin','country_codes','phone_number',)
        labels = {'day_of_birth': _("Day"), 'month_of_birth': _("Month"), 'country_of_origin': _("Country of Origin"),'country_codes': _("Country Code"),'phone_number': _("Phone number"),}
        help_text = {'day_of_birth': _("Please enter your day of birth"), 'month_of_birth': _("Please enter your month of birth"), 'country_of_origin': _("Please enter your Country of Origin"),'country_codes': _("Please enter your Country Code"),'phone_number': _("Please enter your phone number"),}
