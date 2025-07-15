# apps.account.views
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_user(request):
    return Response({'status': 200})
