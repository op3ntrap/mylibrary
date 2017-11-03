from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^account_management', views.account_management_view, name='account_management'),
    url(r'^base', views.view_base_template, name='base_template_preview'),
    url(r'^sign_up', views.sign_up, name='sign_up'),
    url(r'^login', auth_views.LoginView.as_view(template_name='UserManager/login.html',
                                                extra_context={'next': 'http://127.0.0.1:8000/'}), name="login"),
    url(r'^logout', auth_views.LogoutView.as_view(template_name='UserManager/logout.html'), name="logout"),
    url(r'^passwordresetdone',
        auth_views.PasswordResetDoneView.as_view(template_name='UserManager/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^passwordresetcomplete',
        auth_views.PasswordResetCompleteView.as_view(template_name='UserManager/password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^passwordresetconfirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='UserManager/password_reset_confirm.html',
                                                    success_url='http://127.0.0.1:8000/'),
        name='password_reset_confirm'),
    url(r'^passwordreset', auth_views.PasswordResetView.as_view(template_name='UserManager/password_reset.html',
                                                                email_template_name='UserManager/password_reset_email_template.html',
                                                                subject_template_name='UserManager/password_reset_email_template_subject.txt', ),
        name="password_reset"),
    url(r'^profile', views.profile_view, name='profile'),

]
