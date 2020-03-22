
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        print(uploaded_file, uploaded_file.name)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)
