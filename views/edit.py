from django.urls import reverse_lazy
from django.contrib.auth.views import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from auth2.views.generic import MessageRequiredEditView
from auth2.forms.main import UserEditForm, GroupCreationForm
from auth2.views.mixins import StaffUserMixin

User = get_user_model()


class UserEditView(StaffUserMixin, LoginRequiredMixin, PermissionRequiredMixin, MessageRequiredEditView):
    model = User
    form_class = UserEditForm
    success_url = reverse_lazy('auth2:user_list')
    success_message = 'User updated successfully.'
    error_message = 'An error occurred while processing.'
    permission_required = 'auth2.change_user'
    permission_denied_message = 'We are sorry, but you do not have the permission to view this page.'


class GroupEditView(StaffUserMixin, LoginRequiredMixin, PermissionRequiredMixin, MessageRequiredEditView):
    model = Group
    form_class = GroupCreationForm
    success_url = reverse_lazy('auth2:group_list')
    success_message = 'Group updated successfully.'
    error_message = 'An error occurred while processing.'
    permission_required = 'auth.change_group'
    permission_denied_message = 'We are sorry, but you do not have the permission to view this page.'
