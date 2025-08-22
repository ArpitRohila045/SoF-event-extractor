from django.shortcuts import render, redirect
from .forms import SoFDocumentForm


def upload_sof(request):
    if request.method == 'POST':
        form = SoFDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = SoFDocumentForm()
    return render(request, 'upload/upload_sof.html', {'form': form})


def upload_success(request):
    return render(request, 'upload/upload_success.html')
