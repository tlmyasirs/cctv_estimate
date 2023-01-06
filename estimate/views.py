from django.shortcuts import render
from .models import Cam, Nvr, Hdd

def ui_ux(request):

    nvrs = Nvr.objects.all()
    cams = Cam.objects.all()
    hdds = Hdd.objects.all()
    return render(request, 'uiux.html', {'nvrs': nvrs, 'cams': cams, 'hdds': hdds})
