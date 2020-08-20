from django.shortcuts import render

# Create your views here.

from contact.forms import FlavourSuggestionForm


def suggest(request):
    if request.method == 'POST':
        form = FlavourSuggestionForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return render(request, 'thankyou.html', {
                'contact': contact,
            })
    else:
        form = FlavourSuggestionForm()

    return render(request, 'contact_page.html', {
        'form': form,
    })
