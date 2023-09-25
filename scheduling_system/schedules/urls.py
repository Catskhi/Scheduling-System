from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from schedules import views

urlpatterns = [
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('changes/', views.ChangesList.as_view()),
    path('changes/<int:pk>/', views.ChangesList.as_view()),
    path('technicals/', views.TechnicalList.as_view()),
    path('technicals/<int:pk>/', views.TechnicalDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)