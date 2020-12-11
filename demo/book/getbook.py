from . import models

def get_book(request):
  identity = request.GET.get('identity')
  return models.Book.objects.filter(identity=identity)
