from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from auth2.views.generic import CreationView, MessageRequiredCreationView
from auth2.forms.create import StyledUserCreationForm, GroupCreationForm
from auth2.views.mixins import StaffUserMixin

User = get_user_model()


class RegistrationView(CreationView):
    model = User
    form_class = StyledUserCreationForm
    success_url = reverse_lazy('auth2:profile')


class UserCreationView(StaffUserMixin, LoginRequiredMixin, PermissionRequiredMixin, CreationView):
    model = User
    form_class = StyledUserCreationForm
    success_url = reverse_lazy('auth2:user_list')
    permission_required = 'auth2.add_user'
    permission_denied_message = 'We are sorry, but you do not have the permission to view this page.'


class GroupCreationView(StaffUserMixin, LoginRequiredMixin, PermissionRequiredMixin, MessageRequiredCreationView):
    model = Group
    form_class = GroupCreationForm
    success_url = reverse_lazy('auth2:group_list')
    success_message = 'Group created successfully.'
    error_message = 'An error occurred while processing.'
    permission_required = 'auth.add_group'
    permission_denied_message = 'We are sorry, but you do not have the permission to view this page.'
