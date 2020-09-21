import random
import string

from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import UrlForm1, UrlForm2
from .models import Urlhacked


def input(request):
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        # We instantiate an object of the URLsForm class, taking as argument the POST request
        form = UrlForm2(request.POST)
        if form.is_valid():
            original_url = request.POST.get("original_url")
            check = Urlhacked.objects.filter(original_url=original_url).first()
            if check is not None:
                short_url = check.short_url
            # if no short_url found
            else:
                short_url = request.POST.get("short_url")
                form.save()
            short_url = request.META['HTTP_REFERER'] + short_url
            form.data = form.data.copy()
            form.data['short_url'] = short_url
            # marking copy equals True everytime as form is submitted and validating in frontend
            copy = True
            return render(request, "main.html", {'form': form, 'copy': copy})
        else:
            messages.add_message(request, messages.INFO, "URL is invalid please try again")
    random_string = str(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)))

    form = UrlForm1(initial={'short_url': random_string})
    return render(request, "main.html", {'form': form})


def goto(request, short_url):
    try:
        check = Urlhacked.objects.get(short_url=short_url)
    except Urlhacked.DoesNotExist:
        # we raise a 404 Not Found error
        raise Http404('Url does not match to any record in database')
    # but if we have that short_url, we take the corresponding long_url and redirect user to
    return redirect(to=check.original_url)
