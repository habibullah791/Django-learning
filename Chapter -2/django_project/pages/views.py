from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("<h1>My First Heading</h1>")
