from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.detail import DetailView

from wiki.forms import EditSessionForm, WikiPageForm
from wiki.models import EditSession, Wiki_page
# Create your views here.

def add_wiki_page(request):
    form = WikiPageForm(request.POST or None)
    if form.is_valid():
        page = form.save(commit=False)
        page.save()
        msg = "wiki page is saved!"
        messages.success(request, msg, fail_silently=True)
        return redirect(page)
    return render(request, 'wiki_page_form.html', {'form': form})

def edit_wiki_page(request, slug):
    page = get_object_or_404(Wiki_page, slug = slug)
    form = WikiPageForm(request.POST or None)
    edit_form = EditSessionForm(request.POST or None)
    if form.is_valid():
        page = form.save()
        if edit_form.is_valid():
            edit = edit_form.save(commit=False)
            edit.page = page
            edit.save()
            msg = "wiki page updated successfully"
            messages.success(request, msg, fail_silently=True)
            return redirect(page)
    return render(request, 'wiki/wiki_page_form.html', 
                            {
                                'form': form,
                                'edit_form': edit_form,
                                'page': page,
                            })


def page_history(request, slug):
    page = get_object_or_404(Wiki_page, slug=slug)
    return render(request, "edit_history.html", {
         "Wiki_page":page,
         "slug": slug,
     })

def front_page(request):
     return render(request, "wiki_page_list.html", {
        "entries": Wiki_page.publish_manager.all,
        "title": "Home",
        "heading": "All Pages"
    })

def wiki_page_details(request, slug):
     return render(request, "page_detail.html", {
         "slug":slug,
     })