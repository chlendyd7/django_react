from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def post_detail(request: HttpRequest, pk : int) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello World")
    response.write("Hello World")
    response.write("Hello World")
    return response

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")