from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Profile, Person


class IndexView(generic.ListView):
    template_name = 'src/index.html'

    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Person.objects.all()
