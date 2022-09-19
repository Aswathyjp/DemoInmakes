from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [

    path('',views.home,name='home'),
    path('movie/<int:movie_id>',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:movie_id>',views.update,name='update'),
    path('delete/<int:movie_id>',views.delete,name='delete')
]