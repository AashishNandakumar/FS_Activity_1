from django.shortcuts import render
from .forms import BookForm


# Create your views here.
def handle_form_view(request):
    context = {}
    form = BookForm()

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "form.html", context)
