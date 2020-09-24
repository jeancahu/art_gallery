from django.shortcuts import render

# Create your views here.
def collection(request, coll_numb):
    print(coll_numb)
    context = {
        'number': coll_numb,
    }

    return render(request, "collection.html", context)
