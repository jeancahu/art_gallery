from django.shortcuts import render
from .models import Collection
from artwork.models import Artwork

def collection(request, coll_numb):

    collection = Collection.objects.get(id=coll_numb)

    print(collection.name)

    artworks = Artwork.objects.filter(collection=collection.name)

    print(artworks)

    context = {
        'collection': collection,
        'artworks': artworks,
    }

    return render(request, "collection.html", context)
