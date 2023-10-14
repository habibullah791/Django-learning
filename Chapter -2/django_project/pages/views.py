from django.http import HttpResponse

def homePageView(request):
    """
        View function for the home page.

        @desc:    This function takes a request object and returns an HttpResponse
                    containing an HTML heading.

        @params:  - request (HttpRequest): The request object sent by the client.

        @returns:   HttpResponse: An HTTP response containing an HTML heading.

        Example usage:
        In your Django URL configuration, you can map a URL to this view function
        to display the HTML heading on the home page.
    """
    return HttpResponse("<h1>My First Heading</h1>")
