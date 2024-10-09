from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def affiliate(request):
    return render(request, 'affiliate.html')

def articles(request):
    return render(request, 'articles.html')

def blog(request):
    return render(request, 'blog.html')

def contacts(request):
    return render(request, 'contacts.html')

def contest(request):
    return render(request, 'contest.html')

def faq(request):
    return render(request, 'faq.html')

def forgot(request):
    return render(request, 'forgot.html')

def how(request):
    return render(request, 'how.html')

def index_2(request):
    return render(request, 'index-2.html')

def index2(request):
    return render(request, 'index2.html')

def invest(request):
    return render(request, 'invest.html')

def privacy(request):
    return render(request, 'privacy.html')

def profile(request):
    return render(request, 'profile.html')

def reports(request):
    return render(request, 'reports.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def token(request):
    return render(request, 'token.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)