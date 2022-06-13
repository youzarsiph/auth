from django.contrib import messages
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render


class DashboardMixin(LoginRequiredMixin, PermissionRequiredMixin):
    pass


class MessageMixin:
    """
    Base mixin class to add success and error messages.
    """
    success_message = str()
    error_message = str()


class MessageMixinCreateView(MessageMixin):
    """
    A mixin for CreateView to set success and error messages.
    """

    def post(self, request, *args, **kwargs):
        try:
            response = super(MessageMixinCreateView, self).post(request, *args, **kwargs)
            messages.success(request, self.success_message)
            return response
        except Exception as exception:
            if settings.DEBUG:
                self.error_message += '\n' + str(exception)
            messages.error(request, self.error_message, extra_tags=('danger', ))
            return render(
                request,
                self.get_template_names(),
            )


class MessageMixinUpdateView(MessageMixin):
    """
    A mixin for UpdateView to set success and error messages.
    """

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, self.success_message)
        return super().post(request, *args, **kwargs)


class MessageMixinDeleteView(MessageMixin):
    """
    A mixin for DeleteView to set success and error messages.
    """

    def post(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return self.delete(request, *args, **kwargs)


class SuperUserMixin(UserPassesTestMixin):
    """
    Verify that the current user is super user.
    """

    def test_func(self):
        return self.request.user.is_superuser


class StaffUserMixin(UserPassesTestMixin):
    """
    Verify that the current user is staff.
    """

    def test_func(self):
        return self.request.user.is_staff


class TemplateNameMixin:
    """
    A mixin to set the template_name and it's extension.
    """
    app_name = 'auth2'
    parent_dir = ''
    extension = ''

    def get_template_names(self):
        template = self.app_name + '/views/' + self.parent_dir + self.model._meta.verbose_name.title().lower()
        template += self.extension
        return [template]
