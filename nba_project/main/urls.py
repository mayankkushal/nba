from django.urls import path

from nba_project.main.views import (
    MainView,
    MainUpdateView,
    AnswersView
)

app_name = "main"
urlpatterns = [
    path("", view=MainView.as_view(), name="index"),
    path("update", view=MainUpdateView.as_view(), name="update"),
    path("view", view=AnswersView.as_view(), name="view"),
]
	