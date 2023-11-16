from django.shortcuts import render
from .models import Main


def index(request):
    main = Main.objects.order_by('-create_date')
    context = {'main':main}
    return render(request, '../templates/main.html',context)