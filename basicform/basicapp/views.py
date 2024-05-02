from django.shortcuts import render
from .forms import NewUserForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


# def form_name_view(request):
#
#     if request.method == 'POST':
#         form = FormName(request.POST)
#         if form.is_valid():
#             print("Validation Successful")
#             print('NAME '+form.cleaned_data['name'])
#             print('EMAIL '+form.cleaned_data['email'])
#             print('TEXT '+form.cleaned_data['text'])
#     form = FormName()
#     return render(request, 'form_page.html', {'form': form})
def user(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Eror form invalid')

    return render(request, 'user.html')