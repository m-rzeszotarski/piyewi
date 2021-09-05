from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Yerba, Piwo, Wino, Kawa
from strona.forms import YerbaForm, PiwoForm, WinoForm, KawaForm

def glowna(request):
    return render(request, 'strona/glowna.html')

##yerba

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

@login_required
def yerba_zatwierdzenie(request, pk):
    yerba = get_object_or_404(Yerba, pk=pk)
    yerba.zatwierdzenie()
    return redirect('recenzje_list')

##piwo

def piwo_list(request):
    piwos = Piwo.objects.all()
    return render(request, 'strona/piwo_list.html', {'piwos': piwos})

def piwo_detail(request, pk):
    piwo = get_object_or_404(Piwo, pk=pk)
    return render(request, 'strona/piwo_detail.html', {'piwo': piwo})

def piwo_new(request):
    if request.method == "POST":
        form = PiwoForm(request.POST)
        if form.is_valid():
            piwo = form.save(commit=False)
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

@login_required
def piwo_zatwierdzenie(request, pk):
    piwo = get_object_or_404(Piwo, pk=pk)
    piwo.zatwierdzenie()
    return redirect('recenzje_list')

## wino

def wino_list(request):
    winos = Wino.objects.all()
    return render(request, 'strona/wino_list.html', {'winos': winos})

def wino_detail(request, pk):
    wino = get_object_or_404(Wino, pk=pk)
    return render(request, 'strona/wino_detail.html', {'wino': wino})

def wino_new(request):
    if request.method == "POST":
        form = WinoForm(request.POST)
        if form.is_valid():
            wino = form.save(commit=False)
            wino.data = timezone.now()
            wino.save()
            return redirect('wino_detail', pk=wino.pk)
    else:
        form = WinoForm()
    return render(request, 'strona/wino_edit.html', {'form': form})

@login_required
def wino_edit(request, pk):
    wino = get_object_or_404(Wino, pk=pk)
    if request.method == "POST":
        form = WinoForm(request.POST, instance=wino)
        if form.is_valid():
            wino = form.save(commit=False)
            wino.data = timezone.now()
            wino.save()
            return redirect('wino_detail', pk=wino.pk)
    else:
        form = WinoForm(instance=wino)
    return render(request, 'strona/wino_edit.html', {'form': form})

@login_required
def wino_remove(request, pk):
    wino = get_object_or_404(Wino, pk=pk)
    wino.delete()
    return redirect('wino_list')

@login_required
def wino_zatwierdzenie(request, pk):
    wino = get_object_or_404(Wino, pk=pk)
    wino.zatwierdzenie()
    return redirect('recenzje_list')

## kawa

def kawa_list(request):
    kawas = Kawa.objects.all()
    return render(request, 'strona/kawa_list.html', {'kawas': kawas})

def kawa_detail(request, pk):
    kawa = get_object_or_404(Kawa, pk=pk)
    return render(request, 'strona/kawa_detail.html', {'kawa': kawa})

def kawa_new(request):
    if request.method == "POST":
        form = KawaForm(request.POST)
        if form.is_valid():
            kawa = form.save(commit=False)
            kawa.data = timezone.now()
            kawa.save()
            return redirect('kawa_detail', pk=kawa.pk)
    else:
        form = KawaForm()
    return render(request, 'strona/kawa_edit.html', {'form': form})

@login_required
def kawa_edit(request, pk):
    kawa = get_object_or_404(Kawa, pk=pk)
    if request.method == "POST":
        form = KawaForm(request.POST, instance=kawa)
        if form.is_valid():
            kawa = form.save(commit=False)
            kawa.data = timezone.now()
            kawa.save()
            return redirect('kawa_detail', pk=kawa.pk)
    else:
        form = KawaForm(instance=kawa)
    return render(request, 'strona/kawa_edit.html', {'form': form})

@login_required
def kawa_remove(request, pk):
    kawa = get_object_or_404(Kawa, pk=pk)
    kawa.delete()
    return redirect('kawa_list')

@login_required
def kawa_zatwierdzenie(request, pk):
    kawa = get_object_or_404(Kawa, pk=pk)
    kawa.zatwierdzenie()
    return redirect('recenzje_list')

## panel recenzji

@login_required
def recenzje_list(request):
    yerbas = Yerba.objects.all()
    piwos = Piwo.objects.all()
    winos = Wino.objects.all()
    kawas = Kawa.objects.all()

    return render(request, 'strona/recenzje_list.html', {'yerbas' : yerbas, 'piwos' : piwos, 'winos' : winos, 'kawas': kawas})