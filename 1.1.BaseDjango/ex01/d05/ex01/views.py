from django.shortcuts import render
from django.http import HttpResponse

navbar_items = [
    {"name": "Django", "url": "http://127.0.0.1:8000/ex01/django"},
    {"name": "Display", "url": "http://127.0.0.1:8000/ex01/display"},
    {"name": "Templates", "url": "http://127.0.0.1:8000/ex01/templates"},
]


def index(request):
    return HttpResponse("Bienvenue dans l'application ex01!")


def django(request):

    contents = [
        {
            "title": "Definition",
            "body": "Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.",
        },
        {
            "title": "History",
            "body": "Django was created in the fall of 2003, when the web programmers at the Lawrence Journal-World newspaper, Adrian Holovaty and Simon Willison, began using Python to build applications. It was released publicly under a BSD license in July 2005. The framework was named after guitarist Django Reinhardt.",
        },
    ]

    context = {"id": "django",
               "title": "Ex01: Django, framework web.",
               "navbar_items": navbar_items,
               "contents": contents}
    return render(request, "base.html", context)


def display(request):

    contents = [
        {
            "title": "How a static web page is displayed with Django?",
            "body": "Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.",
        },
    ]

    context = {"id": "display",
               "title": "Ex01: Display process of a static page.",
               "navbar_items": navbar_items,
               "contents": contents}
    return render(request, "base.html", context)


def templates(request):

    contents = [
        {
            "title": "What is a template?",
            "body": "A template is a text file. It can generate any text-based format (HTML, XML, CSV, etc.). A template contains variables, which get replaced with values when the template is evaluated, and tags, which control the logic of the template.",
        },
        {
            "title": "blocks",
            "body": "Defines a block that can be overridden by child templates."
        },
        {
            "title": "loops for...in",
            "body": "Loops over each item in an array, making the item available in a context variable."
        },
        {
            "title": "if control structure",
            "body": "The {% if %} tag evaluates a variable, and if that variable is “true” (i.e. exists, is not empty, and is not a false boolean value) the contents of the block are output"
        },
        {
            "title": "Display context variables",
            "body": "Django templates allow you to display context variables passed from the view. Context variables can be inserted into the template using the {{ variable_name }} syntax."
        },

    ]

    context = {"id": "templates",
               "title": "Ex01: Template engine.",
               "navbar_items": navbar_items,
               "contents": contents}
    return render(request, "base.html", context)
