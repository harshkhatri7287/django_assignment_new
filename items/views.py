from django.shortcuts import render, redirect, get_object_or_404
from .decorators import superuser_check
from .forms import ShopForm
from .models import ShoppingItem
from django.contrib import messages
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import ShoppingItem

@receiver(pre_save, sender=ShoppingItem)
def call(sender, instance, **kwargs):
    print("Object is not saved yet!")
    print(f"Name of the  product: {instance.name}")

@receiver(post_save, sender=ShoppingItem)
def call(sender, instance, **kwargs):
    print("Object is saved!")

def index(request):
    datadict = {}
    datalist = ShoppingItem.objects.all()
    datadict['datalist'] = datalist
    return render(request, 'items/index.html', datadict)

def delete_view(request, item_name):
    data = {}
    obj = get_object_or_404(ShoppingItem, name=item_name)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Product deleted succesfully.")
        return redirect('/home')
    data["obj"] = obj
    return render(request, 'items/delete.html', data)


@superuser_check
def create_view(request):
    context = {}
    form = ShopForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Product added succesfully.")
        return redirect('/home')
    context['form'] = form
    return render(request, 'items/create_view.html', context)

def update_view(request, item_name):
    context = {}
    obj = get_object_or_404(ShoppingItem, name=item_name)
    form = ShopForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Product updated succesfully!!")
        return redirect('/home')
    context['form'] = form
    return render(request, 'items/update.html', context)