from django.urls import path
from . import views
urlpatterns=[
    path('',views.user_login),
    path('register',views.register),
    path('user_home',views.user_home),
    path('upload_image',views.upload_image),
    path('images',views.images),
    path('logout',views.shop_logout),    
    path('note',views.note),
    path('upload_note',views.upload_note),
    path('delete_note/<id>',views.delete_note),
    path('delete_img/<id>',views.delete_img),
    path('upload_vid',views.upload_vid),
    path('video',views.video),
    path('delete_video/<id>',views.delete_video), 
    path('upload_aud',views.upload_aud),
    path('audio',views.audio),
    path('delete_aud/<id>',views.delete_aud), 


    ]