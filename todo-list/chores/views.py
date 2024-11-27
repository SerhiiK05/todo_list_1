from http.client import HTTPResponse

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from chores.forms import TagCreationForm, TaskCreationForm
from chores.models import Tag, Task


# Create your views here.
@login_required
def index(request: HttpRequest) -> HTTPResponse:
    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()
    num_visits = request.session.get("num_visits", 0) + 1
    request.session["num_visits"] = num_visits

    context = {
        "num_tags": num_tags,
        "num_tasks": num_tasks,
        "num_visits": num_visits + 1,
    }

    return render(request, "chores/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    template_name = "chores/tag_list.html"
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagCreationForm
    success_url = reverse_lazy("chores:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("chores:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("chores:tag-list")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10

    class Meta:
        queryset = Tag.objects.prefetch_related("tags")
        fields = ("content", "datetime", "deadline", "complete", "tags")
        template_name = "chores/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy("chores:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("chores:task-list")
    fields = ("content", "deadline", "complete", "tags")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("chores:task-list")


@login_required
def toggle_task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if task.complete:
        task.complete = False
    else:
        task.complete = True
    task.save()
    return HttpResponseRedirect(reverse("chores:task-list"))
