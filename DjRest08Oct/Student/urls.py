
from django.urls import path
from . import views

urlpatterns = [
    path('details/',views.Student_Api.as_view()),
    path('details/<int:id>/',views.Student_Api.as_view()),
    path('st_details/',views.Student2Api.as_view()),
    path('st_details/<int:id>/',views.Student2Api.as_view()),
    path('marks/',views.MarkApi.as_view()),
    path('marks/<int:id>/',views.MarkApi.as_view()),

]
