from django.urls import path
from . import views

urlpatterns = [
    path('logout',views.logout),
    path('tasks',views.tasks),
    path('bills', views.bills),
    path('reminders', views.reminders),
    path('addtask', views.addtask),
    path('addbill',views.addbill),
    path('addreminder', views.addreminder),
    path('edittask/<int:id>',views.edittask),
    path('dotask/<int:id>',views.dotask),
    path('undotask/<int:id>',views.undotask),
    path('paybill/<int:id>',views.paybill),
    path('editbill/<int:id>',views.editbill),
    path('editreminder/<int:id>',views.editreminder),
    path('removereminder/<int:id>',views.removereminder),
    path('deletebill/<int:id>',views.deletebill),
    path('deletetask/<int:id>',views.deletetask),
]