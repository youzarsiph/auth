from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import get_user_model
from auth2.forms.base import StyledModelForm

User = get_user_model()


class StyledUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(StyledUserCreationForm, self).__init__(*args, **kwargs)
        for label in self.fields:
            field = self.fields[label]
            try:
                if field.widget.input_type == 'checkbox' or field.widget.input_type == 'radio':
                    field.widget.attrs['class'] = 'form-check-input'
                else:
                    field.widget.attrs['class'] = 'form-control'
                    field.widget.attrs['placeholder'] = field.label
            except Exception:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class GroupCreationForm(StyledModelForm):
    class Meta:
        model = Group
        fields = ('name', 'permissions')
