from . import models
from django.http import HttpResponse
def get_book(request):
  identity = request.GET.get('identity')
  return HttpResponse('get book identity %s', identity)
  # return models.Book.objects.filter(identity=identity)
