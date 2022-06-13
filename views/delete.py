from django.urls import reverse_lazy
from auth2.views.generic import MessageRequiredDeletionView
from django.contrib.auth.views import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from auth2.views.mixins import StaffUserMixin

User = get_user_model()


class UserDeletionView(StaffUserMixin, LoginRequiredMixin, PermissionRequiredMixin, MessageRequiredDeletionView):
    model = User
    success_url = reverse_lazy('auth2:user_list')
    success_message = 'Account deleted successfully.'
    error_message = 'An error occurred while processing.'
    permission_required = 'auth2.delete_user'
    permission_denied_message = 'We are sorry, but you do not have the permission to view this page.'


class GroupDeletionView(StaffUserMixin, LoginRequiredMixin, PermissionRequiredMixin, MessageRequiredDeletionView):
    model = Group
    success_url = reverse_lazy('auth2:group_list')
    success_message = 'Group deleted successfully.'
    error_message = 'An error occurred while processing.'
    permission_required = 'auth.delete_group'
    permission_denied_message = 'We are sorry, but you do not have the permission to view this page.'
