
from django.urls import path,include
from . import views
from .router import library_router
urlpatterns = [
    path('br/',include(library_router.urls)),

]
