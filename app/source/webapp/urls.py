from django.urls import path

from webapp.views.action import action_view
from webapp.views.create_cat import create_view

urlpatterns = [
    path("", create_view),
    path("action/", action_view)
]