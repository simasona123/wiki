import re
from django.shortcuts import render
from .forms import Search, New_Page, Edit
from . import util
import markdown2


def index(request):
    search = Search()
    total = 0  # total key dictionary
    for key in request.GET:
        total += 1
    if total == 0:
        return render(request, "encyclopedia/index.html", {
            'entries': util.list_entries(),
            'search': search,
        })
    else:
        title = request.GET.get('title')
        list_title = []
        for i in util.list_entries():
            x = re.search(f"^{title}", i, flags=re.IGNORECASE)
            print(list_title)
            if x:
                list_title.append(i)
        return render(request, "encyclopedia/index.html", {
            'entries': list_title,
            'search': search,
        })


def entry(request, title):
    search = Search()
    if len(request.GET) >= 1:
        title = request.GET.get('title')
        list_title = []
        for i in util.list_entries():
            x = re.search(f"^{title}", i, flags=re.IGNORECASE)
            print(list_title)
            if x:
                list_title.append(i)
        return render(request, "encyclopedia/index.html", {
            'entries': list_title,
            'search': search,
        })
    return render(request, "encyclopedia/entry.html", {
        'title': title,
        'entry': markdown2.markdown(util.get_entry(title)),
        'search': search,
    })


def newpage(request):
    search = Search()
    form = New_Page()
    if request.method == 'POST':
        form = New_Page(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            util.save_entry(form['title'], form['text'])
            return render(request, 'encyclopedia/index.html', {
                'form': form,
                'entries': util.list_entries()
            })
    return render(request, 'encyclopedia/new.html', {
        'form': form,
        'search': search,
    })


def edit(request, title):
    entry = util.get_entry(title)
    form = Edit(initial=({'text': entry}))

    if request.method == 'POST':
        form = Edit(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            util.save_entry(title, form['text'])
            return render(request, 'encyclopedia/entry.html', {
                'form': form,
                'entry': markdown2.markdown(util.get_entry(title)),
                'title': title,
            })

    return render(request, 'encyclopedia/edit.html', {
        'form': form,
        'title': title,
    })
