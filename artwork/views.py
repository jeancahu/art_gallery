from django.shortcuts import render

# Create your views here.
def artwork(request, coll_numb):
    print(coll_numb)
    return render(request, "artwork.html")
