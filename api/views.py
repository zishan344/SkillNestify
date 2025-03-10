from django.http import JsonResponse
def home (request):
  " Create a simple home rendering view return welcome to skillNestify."
  return JsonResponse({"message":"Welcome to the skillNestify"})