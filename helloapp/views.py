from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_hello(request):
    html_content = """
        <!DOCTYPE html>
        <html lamg="ja">
        <head>
            <meta charset="UTF-8">
            <title>Hello Django</title>
        </head>
        <body>
            <p>ハロー、Django！</p>
            <a href="/menu/">メニューに戻る</p>
        </body>
        <html>
        """
    
    return HttpResponse(html_content)

