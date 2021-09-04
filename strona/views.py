from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Yerba, Piwo
from strona.forms import YerbaForm, PiwoForm

def glowna(request):
    return render(request, 'strona/glowna.html')

##yerba

def yerba_list(request):
    yerbas = Yerba.objects.all()
    return render(request, 'strona/yerba_list.html', {'yerbas': yerbas})

def yerba_detail(request, pk):
    yerba = get_object_or_404(Yerba, pk=pk)
    return render(request, 'strona/yerba_detail.html', {'yerba': yerba})

@login_required
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

@login_required
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

@login_required
def yerba_remove(request, pk):
    yerba = get_object_or_404(Yerba, pk=pk)
    yerba.delete()
    return redirect('yerba_list')

##piwo

def piwo_list(request):
    piwos = Piwo.objects.all()
    return render(request, 'strona/piwo_list.html', {'piwos': piwos})

def piwo_detail(request, pk):
    piwo = get_object_or_404(Piwo, pk=pk)
    return render(request, 'strona/piwo_detail.html', {'piwo': piwo})

@login_required
def piwo_new(request):
    if request.method == "POST":
        form = PiwoForm(request.POST)
        if form.is_valid():
            piwo = form.save(commit=False)
            piwo.autor = request.user
            piwo.data = timezone.now()
            piwo.save()
            return redirect('piwo_detail', pk=piwo.pk)
    else:
        form = PiwoForm()
    return render(request, 'strona/piwo_edit.html', {'form': form})

@login_required
def piwo_edit(request, pk):
    piwo = get_object_or_404(Piwo, pk=pk)
    if request.method == "POST":
        form = PiwoForm(request.POST, instance=piwo)
        if form.is_valid():
            piwo = form.save(commit=False)
            piwo.autor = request.user
            piwo.data = timezone.now()
            piwo.save()
            return redirect('piwo_detail', pk=piwo.pk)
    else:
        form = PiwoForm(instance=piwo)
    return render(request, 'strona/piwo_edit.html', {'form': form})

@login_required
def piwo_remove(request, pk):
    piwo = get_object_or_404(Piwo, pk=pk)
    piwo.delete()
    return redirect('piwo_list')