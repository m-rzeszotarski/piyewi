from strona.forms import YerbaForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Yerba

def glowna(request):
    return render(request, 'strona/glowna.html')

def yerba_list(request):
    yerbas = Yerba.objects.all()
    return render(request, 'strona/yerba_list.html', {'yerbas': yerbas})

def yerba_detail(request, pk):
    yerba = get_object_or_404(Yerba, pk=pk)
    return render(request, 'strona/yerba_detail.html', {'yerba': yerba})

def yerba_new(request):
    if request.method == "POST":
        form = YerbaForm(request.POST)
        if form.is_valid():
            yerba = form.save(commit=False)
            yerba.autor = request.user
            yerba.data = timezone.now()
            yerba.save()
            return redirect('yerba_detail', pk=yerba.pk)
    else:
        form = YerbaForm()
    return render(request, 'strona/yerba_edit.html', {'form': form})

def yerba_edit(request, pk):
    yerba = get_object_or_404(Yerba, pk=pk)
    if request.method == "POST":
        form = YerbaForm(request.POST, instance=yerba)
        if form.is_valid():
            yerba = form.save(commit=False)
            yerba.autor = request.user
            yerba.data = timezone.now()
            yerba.save()
            return redirect('yerba_detail', pk=yerba.pk)
    else:
        form = YerbaForm(instance=yerba)
    return render(request, 'strona/yerba_edit.html', {'form': form})
