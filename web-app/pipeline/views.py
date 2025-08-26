from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, Http404
from django.core.paginator import Paginator
from django.db.models import Q 
from .forms import SoFDocumentForm
from .models import SoFDocument, SOFData
from .pipeline import Pipeline

@login_required(login_url='login')
def upload_sof(request):
    """Uplaod SoF Document View"""
    if request.method == 'POST':
        form = SoFDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()
            pipeline = Pipeline() 
            return redirect('upload_success')
    else:
        form = SoFDocumentForm()
    return render(request, 'pipeline/upload_sof.html', {'form': form})


def upload_success(request):
    return render(request, 'pipeline/upload_success.html')
