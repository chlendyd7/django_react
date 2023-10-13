from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post

# Create your views here.
# def post_detail(request: HttpRequest, pk : int) -> HttpResponse:
#     response = HttpResponse()
#     response.write("Hello World")
#     response.write("Hello World")
#     response.write("Hello World")
#     return response

# post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')


def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")

def post_detail(request: HttpRequest, pk:int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    return render(request, 'instagram/post_detail.html', {
        'post' : post
    })