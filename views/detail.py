from django.contrib.auth.views import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from auth2.views.generic import DetailsView
from auth2.views.mixins import StaffUserMixin

User = get_user_model()


class UserDetailView(StaffUserMixin, LoginRequiredMixin, PermissionRequiredMixin, DetailsView):
    model = User
    # If you want to use auth2.User model you need to change the app_name in this case 'auth' to be 'auth2'
    permission_required = 'auth.view_user'
    permission_denied_message = 'We are sorry, but you do not have the permission to view this page.'


class GroupDetailView(StaffUserMixin, LoginRequiredMixin, PermissionRequiredMixin, DetailsView):
    model = Group
    permission_required = 'auth.view_group'
    permission_denied_message = 'We are sorry, but you do not have the permission to view this page.'
