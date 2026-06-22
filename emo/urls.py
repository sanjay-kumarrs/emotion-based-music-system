"""emo_player URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.main,name="main"),
    path('login_code', views.login_code,name="login_code"),
    path('logout', views.logout,name="logout"),
    path('adminhome', views.adminhome,name="adminhome"),
    path('manageplaylist',views.manageplaylist,name="manageplaylist"),
    path('editplaylist/<int:id>',views.editplaylist,name="editplaylist"),
    path('editplylistcode',views.editplylistcode,name="editplylistcode"),
    path('sendreply/<int:id>',views.sendreply,name="sendreply"),
    path('viewcomplaints',views.viewcomplaints,name="viewcomplaints"),
    path('viewrating',views.viewrating,name="viewrating"),
    path('viewuser',views.viewuser,name="viewuser"),
    path('addplaylist',views.addplaylist,name="addplaylist"),
    path('playlistcode',views.playlistcode,name="playlistcode"),
    path('viewusersrch',views.viewusersrch,name="viewusersrch"),
    path('viewcomplaints_search',views.viewcomplaints_search,name="viewcomplaints_search"),
    path('viewrating_search',views.viewrating_search,name="viewrating_search"),
    path('manageplaylist_search',views.manageplaylist_search,name="manageplaylist_search"),
    path('deleteplaylist/<int:id>',views.deleteplaylist,name="deleteplaylist"),
    # path('managebooks',views.managebooks,name="managebooks"),
    # path('addbooks',views.addbooks,name="addbooks"),
    # path('editbooks/<int:id>',views.editbooks,name="editbooks"),
    # path('editbookscode',views.editbookscode,name="editbookscode"),
    # path('managebook_search',views.managebook_search,name="managebook_search"),
    # path('deletebooks/<int:id>',views.deletebooks,name="deletebook"),
    # path('managebook_search',views.managebook_search,name="managebook_search"),
    path('view_profile',views.view_profile,name="view_profile"),
    path('edit_profile',views.edit_Profile,name="edit_profile"),
    path('delete_user/<id>',views.delete_user,name="edit_profile"),
    


    path('add_reply',views.add_reply,name="add_reply"),


    path('chatwithuser',views.chatwithuser,name="chatwithuser"),
    path('reply_app',views.add_reply,name="reply_app"),
    path('send_addplaylist_app',views.send_addplaylist_app,name="send_addplaylist_app"),
    path('send_Rating_app',views.send_Rating_app,name="send_Rating_app"),
    path('viewplaylist',views.viewplaylist,name="viewplaylist"),
    path('send_complaint_app',views.send_complaint_app,name="send_complaint_app"),
    path('delete_comp',views.delete_comp,name="delete_comp"),
    path('view_comp',views.view_comp,name="view_comp"),




    path('registration',views.registration,name="registration"),
    path('rplaylist',views.rplaylist,name="rplaylist"),
    path('login_code1',views.login_code1,name="login_code1"),
    path('in_message2',views.in_message2,name="in_message2"),
    path('view_message2',views.view_message2,name="view_message2"),
    path('capture',views.capture,name="capture"),
    path('viewplaylist_emo',views.viewplaylist_emo,name="viewplaylist_emo"),
]
