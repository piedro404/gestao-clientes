from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .form import PersonForm


@login_required
def persons_list(reguest):
    persons = Person.objects.all()
    return render(reguest, "person.html", {"persons": persons})


@login_required
def persons_new(reguest):
    form = PersonForm(reguest.POST or None, reguest.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("person_list")

    return render(reguest, 'person_form.html', {'form': form})


@login_required
def persons_update(reguest, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(reguest.POST or None, reguest.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect("person_list")

    return render(reguest, "person_form.html", {"form":form})


@login_required
def persons_delete(reguest, id):
    person = get_object_or_404(Person, pk=id)


    if reguest.method == "POST":
        person.delete()
        return redirect("person_list")

    return render(reguest, "person_delete_confirm.html", {"person": person})

