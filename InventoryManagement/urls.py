from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.landingpage, name="landingpage"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('inventory/<category>', views.inventory, name="inventory"),
    path('inventory/<category>/addrecord', views.addrecord, name="addrecord"),
    path('inventory/<category>/deleterecord/',
         views.deleterecord, name="deleterecord"),
    path('inventory/<category>/deleterecord/<c_id>',
         views.deleteconfirm, name="deleteconfirm"),
    path('inventory/<category>/editrecord/<c_id>',
         views.editrecord, name="editrecord"),
    path('inventory/<category>/renamecategory/',
         views.renamecategory, name="renamecategory"),
    path('inventory/<category>/removecategory/',
         views.removecategory, name="removecategory"),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutpage, name="logout"),
    path('register/', views.register, name="register"),
    path('contact/', views.contact, name="contact"),
    path('search_result/', views.search, name="search"),
    path('updatepassword/', views.UpdatePassword, name="UpdatePassword"),
    path('settings/', views.settings, name="settings"),
    path('about/', views.about, name="about"),



    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),

]
