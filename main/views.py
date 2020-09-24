from django.shortcuts import render

# Import models
# from .models import
from collection.models import Collection

# Create your views here.
def main(request):

        collections = Collection.objects.all()
        print(collections)

        context = {
                'collections': collections,
        }

        return render(request, "index.html", context)
