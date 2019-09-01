from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreModelForm

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)


def store_create(request):
    form = StoreModelForm()
    if request.method == "POST":
        form = StoreModelForm(request.POST)
        if form.is_valid():
            store = form.save(commit = False)
            store.owner = request.user
            store.save()
            return redirect('list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)


def store_detail(request,store_slug):
    context = {
        "stores": Store.objects.get(slug=store_slug)
    }
    return render(request, 'store_detail.html', context)

