from django.urls import path
from django.contrib.auth import views
from auth2.forms.main import *
from auth2.views.main import *

# To change the app name.
app_name = 'auth2'
urlpatterns = [
    # Main views
    path(
        '',
        IndexView.as_view(),
        name='index'
    ),
    path(
        'dashboard/',
        DashboardView.as_view(),
        name='dashboard'
    ),

    # Authentication
    path(
        'login/',
        views.LoginView.as_view(
            form_class=StyledAuthenticationForm,
            template_name='auth2/authentication/login.html',
            extra_context={
                'signup_form': StyledUserCreationForm()
            }
        ),
        name='login'
    ),
    path(
        'register/',
        RegistrationView.as_view(),
        name='register'
    ),
    path(
        'logout/',
        views.LogoutView.as_view(
            template_name='auth2/authentication/logged_out.html'
        ),
        name='logout'
    ),
    path(
        'profile/',
        ProfileView.as_view(),
        name='profile'
    ),

    # Users
    path(
        'users/create/',
        UserCreationView.as_view(),
        name='create_user'
    ),
    path(
        'users/',
        UserListView.as_view(),
        name='user_list'
    ),
    path(
        'users/<int:id>/',
        UserDetailView.as_view(),
        name='user_detail'
    ),
    path(
        'users/<int:id>/edit/',
        UserEditView.as_view(),
        name='edit_user'
    ),
    path(
        'users/<int:id>/delete/',
        UserDeletionView.as_view(),
        name='delete_user'
    ),

    # Group
    path(
        'groups/create/',
        GroupCreationView.as_view(),
        name='create_group'
    ),
    path(
        'groups/',
        GroupListView.as_view(),
        name='group_list'
    ),
    path(
        'groups/<int:id>/',
        GroupDetailView.as_view(),
        name='group_detail'
    ),
    path(
        'groups/<int:id>/edit/',
        GroupEditView.as_view(),
        name='edit_group'
    ),
    path(
        'groups/<int:id>/delete/',
        GroupDeletionView.as_view(),
        name='delete_group'
    ),

    # Password
    path(
        'password/change/',
        views.PasswordChangeView.as_view(
            form_class=StyledPasswordChangeForm,
            template_name='auth2/authentication/change_password.html',
            success_url=reverse_lazy('auth2:change_done')
        ),
        name='change_password'
    ),
    path(
        'password/change/done/',
        views.PasswordChangeDoneView.as_view(
            template_name='auth2/authentication/change_done.html'
        ),
        name='change_done'
    ),
    path(
        'password/reset/',
        views.PasswordResetView.as_view(
            form_class=StyledPasswordResetForm,
            template_name='auth2/authentication/reset_password.html',
            success_url=reverse_lazy('auth2:reset_done')
        ),
        name='reset_password'
    ),
    path(
        'password/reset/done/',
        views.PasswordResetDoneView.as_view(
            template_name='auth2/authentication/reset_done.html'
        ),
        name='reset_done'
    ),
    path(
        'password/reset/confirm/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(
            template_name='auth2/authentication/reset_confirm.html',
            form_class=StyledPasswordResetForm,
            success_url=reverse_lazy('auth2:reset_complete')
        ),
        name='reset_confirm'
    ),
    path(
        'password/reset/complete/',
        views.PasswordResetCompleteView.as_view(
            template_name='auth2/authentication/reset_complete.html',
        ),
        name='reset_complete'
    ),
]
