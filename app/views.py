from django.shortcuts import render, redirect
from django.forms import ModelForm

from app.models import Category

# Create your views here.
def category_list(request):
    return render(request, 'category_list.html', {
        'categories': Category.objects.all()
    })

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/category_list')
    else:
        form = CategoryForm()
        return render(request, 'category_create.html', {
            'form': form
        })