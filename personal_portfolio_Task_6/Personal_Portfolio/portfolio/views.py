from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

def home(request):
    """Render the home page"""
    return render(request, 'index.html')

def contact(request):
    """Handle contact form submission"""
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Here you can save to database or send email
        # For now, just show success message
        messages.success(request, 'Thank you for your message! I will get back to you soon.')
        return redirect('home')
    
    return redirect('home')