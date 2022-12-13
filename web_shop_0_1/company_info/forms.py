from django import forms

from web_shop_0_1.company_info.models import Messages


class MessagesCreateForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['some_email', 'title', 'message']
