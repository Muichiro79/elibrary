from django.shortcuts import render, redirect
from .forms import ContactForm

def homepage(request):
    return render(request, 'core/home.html')

def about_page(request):
    return render(request, 'core/about.html')

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # or send email
            return redirect('contact')  # Refresh/redirect after submission
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})
