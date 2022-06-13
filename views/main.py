from django.views.generic import TemplateView
from auth2.views.create import *
from auth2.views.detail import *
from auth2.views.edit import *
from auth2.views.delete import *
from auth2.views.list import *
from auth2.views.mixins import DashboardMixin, LoginRequiredMixin, StaffUserMixin


# Create your views here.
class IndexView(StaffUserMixin, LoginRequiredMixin, TemplateView):
    template_name = 'auth2/base/index.html'


class DashboardView(StaffUserMixin, DashboardMixin, TemplateView):
    template_name = 'auth2/base/dashboard.html'
    permission_required = 'auth.view_user'


class ProfileView(StaffUserMixin, LoginRequiredMixin, TemplateView):
    template_name = 'auth2/authentication/profile.html'
