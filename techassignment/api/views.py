from django.shortcuts import render


def index(request):

    # Display the main/home page
    return render(request, "index.html")
