from django.urls import path,include
from .import views

urlpatterns = [
    path('adddata/', views.InsertPageView, name='insertpage'),
    path('insert/', views.Insertdata, name='insert'),
    path('showpage/', views.ShowView, name='showpage'),
    path('editpage/<int:pk>', views.EditPage, name='editpage'),
    path('update/<int:pk>', views.Updatedata, name='update'),
    path('delete/<int:pk>', views.DeleteData, name='delete'),
    path('', views.home, name='home'),
    ]