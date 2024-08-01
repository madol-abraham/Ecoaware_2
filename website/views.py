from django.shortcuts import render, redirect
from .forms import DonationForm, NewsletterSubscriptionForm
from .models import Post

def home(request):
    return render(request, 'index.html')

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def subscribe(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = NewsletterSubscriptionForm()
    return render(request, 'subscribe.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')
