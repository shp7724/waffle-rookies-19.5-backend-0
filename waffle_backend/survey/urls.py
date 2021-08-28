from django.urls import include, path

from survey import views

urlpatterns = [
    path('results/', views.get_survey_results, name="get_surveys"),
    path('results/<survey_id>/', views.get_survey, name="get_survey"),
    path('os/', views.list_all_os, name="list_all_os"),
    path('os/<os_id>', views.get_os, name="get_os"),
]
