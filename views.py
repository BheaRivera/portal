
from django.http import HttpResponse


def home(request):
    return HttpResponse("""
        <h1>Welcome to My Multi-Route Portal!</h1>
        <p>This is my Week 10 Django activity.</p>
        <p><a href="/about/">About My Portal</a></p>
        <p><a href="/greet/Bhea/">Greet Me</a></p>
    """)


def about(request):
    return HttpResponse("""
        <h1>About My Portal</h1>
        <p>This portal is my Week 10 Django activity.</p>
        <p>I am learning URL routing and views in Django.</p>
        <p><a href="/">Back to Home</a></p>
    """)


def greet(request, name):
    return HttpResponse(f"""
        <h1>Hello, {name}!</h1>
        <p>Welcome to my Multi-Route Portal!</p>
        <p><a href="/">Back to Home</a></p>
    """)
