from django.shortcuts import render

# Create your views here.
def collection(request, number):
    print(number)
    context = {
        'number': number,
    }

    return render(request, "collection.html", context)
