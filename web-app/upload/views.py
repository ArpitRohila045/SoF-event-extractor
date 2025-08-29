from django.shortcuts import render, redirect
from .forms import SoFDocumentForm
from .models import SoFDocument

def upload_sof(request):
    if request.method == 'POST':
        form = SoFDocumentForm(request.POST, request.FILES)

        if form.is_valid():
            document = form.save(commit=False)  # Don't save yet
            document.user = request.user  # Set the user
            
            uploaded_file = request.FILES['file']
            
            document.file = uploaded_file
            document.file_type = uploaded_file.content_type  # or use extension
            document.save()

            return redirect('upload_success')
    else:
        form = SoFDocumentForm()
        return render(request, 'upload/upload_sof.html', {'form': form})


def upload_success(request):
    return render(request, 'upload/sucess_sof.html')
