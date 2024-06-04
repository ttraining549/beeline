from django.urls import path
from . import views


urlpatterns = [
    # Vacancy API
    path('vacancies/', views.VacancySerializerListView.as_view(),
         name='vacancy_list_api'),
    path('vacancies/<int:pk>/', views.VacancySerializerDetailView.as_view(),
         name='vacancy_detail_api'),
    # Category API
    path('vacancy-categories/', views.CategorySerializerListView.as_view(),
         name='category_list_api'),
    path('vacancy-categories/<int:pk>/',
         views.CategorySerializerDetailView.as_view(),
         name='category_detail_api'),
]
