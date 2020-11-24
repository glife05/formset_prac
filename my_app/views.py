from django.shortcuts import render,redirect
from django.forms import modelformset_factory
from .models import Programmer,Language

# Create your views here.
def index(request):
    qs=Programmer.objects.all()
    context={"qs":qs,}
    return render(request,'pages/index.html',context)


def listing(request,programmer_id):
    programmer=Programmer.objects.get(pk=programmer_id)
    LanguageFormset=modelformset_factory(Language,fields=('name',))

    if request.method=='POST':
        formset=LanguageFormset(request.POST,queryset=Language.objects.filter(programmer__id=programmer.id))
        if formset.is_valid():
            #formset.save()
            instances=formset.save(commit=False)
            for instance in instances:
                instance.programmer_id=programmer.id
                instance.save()
            return redirect('index')    

    formset=LanguageFormset(queryset=Language.objects.filter(programmer__id=programmer.id))
    context={"formset":formset,}
    return render(request,'pages/listing.html',context)

