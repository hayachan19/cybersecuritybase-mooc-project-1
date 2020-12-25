from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout_view'),
    path('reserve', views.reservation_view, name='reservation_view'),
    path('reserve/<int:user_id>/<int:question_id>/', views.reserve_question, name='reserve_question'),
    path('view/<int:question_id>/', views.answer_view, name='answer_view'),
    path('edit/<int:question_id>/', views.edit_answer_view, name='edit_answer_view'),
    path('search', views.search_view, name='search_view'),
]