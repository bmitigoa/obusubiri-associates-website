from django.shortcuts import render, redirect
from .forms import InquiryForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def training(request):
    return render(request, 'training.html')


def contact(request):

    if request.method == 'POST':

        form = InquiryForm(request.POST)

        if form.is_valid():

            form.save()

            return render(
                request,
                'contact.html',
                {
                    'form': InquiryForm(),
                    'success': True
                }
            )

    else:

        form = InquiryForm()

    return render(
        request,
        'contact.html',
        {
            'form': form
        }
    )