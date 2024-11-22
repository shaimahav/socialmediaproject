from django.urls import path
from user import views
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('',views.index,name='index'),
   path('login/',views.user_login,name='login'),
   path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
   path('password_change/',auth_views.PasswordChangeView.as_view(template_name='user/password_change_form.html'),name='passwordchange'),
   path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'),name='password_change_done'),
   path('password_reset/',auth_views.PasswordResetView.as_view(template_name='user/password_reset_form.html'),name='password_reset'),
   path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
   path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
   path('reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),
   path('register/',views.register,name='register'),
   path('edit',views.edit,name='edit'),
]
