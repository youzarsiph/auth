from django.contrib.auth.views import get_user_model
from auth2.forms.base import StyledModelForm

User = get_user_model()


class UserEditForm(StyledModelForm):
    class Meta:
        model = User
        fields = ('user_permissions', 'groups', 'is_active', 'is_staff', 'is_superuser',)
