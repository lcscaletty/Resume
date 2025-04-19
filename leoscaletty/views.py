#views
from django.shortcuts import render, redirect
from .models import Header, Bullet, moreInfo
from .forms import BulletForm
from django.contrib.auth.decorators import login_required

def home(request):
    headers = Header.objects.prefetch_related('bullet_set')
    bullets = Bullet.objects.prefetch_related('moreinfo_set')
    moreInfos = moreInfo.objects.all()
    context = {
        "test": "This is a test",
        "headers": headers,
        "bullets": bullets,
        "moreInfos": moreInfos,
    }
    return render(request, "leoscaletty/home.html", context)

@login_required
def add_bullet(request):
    if request.method == 'POST':
        form = BulletForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')   
    else:
        form = BulletForm()
    return render(request, 'leoscaletty/add_bullet.html', {'form': form})
