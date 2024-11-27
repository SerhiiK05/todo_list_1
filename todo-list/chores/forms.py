from django import forms

from chores.models import Task, Tag


class TaskCreationForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("content", "deadline", "complete", "tags")
        deadline = forms.DateTimeField(
            widget=forms.TextInput(attrs={"type": "datetime-local"}),
            input_formats=["%Y-%m-%dT   %H:%M"],
        )


class TagCreationForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ("name",)
