import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from app.website.models import Cat

# Load all context functions
path = os.getcwd()
for entry in os.scandir(os.path.join(path, "app", "website", "actions")):
    if entry.is_file():
        name = entry.name.split(".")[0]
        exec(
            f"from app.website.actions.{name} import get_context as get_{name}_context"
        )


def home(request):
    return render(request, "base.html", get_home_context())


def about_us(request):
    return render(request, "base.html", get_about_us_context())


def cats_list(request):
    return render(request, "base.html", get_cats_context())


def cat_single(request, cat_slug):
    return render(request, "base.html", get_cat_single_context(slug=cat_slug))


@login_required(login_url="login")
def cat_new(request):
    return render(request, "base.html", get_cat_new_context())


def login(request):
    return render(request, "base.html", get_login_context())


@login_required(login_url="login")
def profile(request):
    return render(request, "base.html", get_profile_context())


def contact(request):
    return render(request, "base.html", get_contact_context())


def robots(request):
    return render(
        request,
        "txts/robots.txt",
        content_type="text/plain",
        context={"DOMAIN": settings.DOMAIN},
    )


def sitemap(request):
    return render(
        request,
        "txts/sitemap.txt",
        content_type="text/plain",
        context={
            "DOMAIN": settings.DOMAIN,
            "cats": Cat.objects.all(),
        },
    )


def security(request):
    return render(request, "txts/security.txt", content_type="text/plain")


def humans(request):
    return render(request, "txts/humans.txt", content_type="text/plain")


def page_not_found(request, exception):
    return render(request, "base.html", {"page": "pages/404.html"})


def page_server_error(request):
    return render(request, "base_simple.html", {"page": "pages/500.html"})
