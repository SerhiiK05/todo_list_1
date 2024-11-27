from django.urls import path

from chores.views import (
    TaskListView,
    TagListView,
    index,
    TaskUpdateView,
    TaskDeleteView,
    TaskCreateView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    toggle_task_complete,
)

app_name = "chores"

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(),
         name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(),
         name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(),
         name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(),
         name="tag-delete"),
    path("task/<int:pk>/toggle/", toggle_task_complete, name="task-toggle"),
]
