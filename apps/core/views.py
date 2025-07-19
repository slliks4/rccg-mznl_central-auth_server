# views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
@permission_classes([AllowAny])
def api_endpoints(request) -> Response:
    """
    📖  API MVP Endpoints
    This returns, for each route, its URL, HTTP method, expected request body,
    and example successful response. Update this in lock-step with any changes.
    """

    data = {
        'auth/token': {
            'url':      reverse('token_obtain_pair', request=request),
            'method':   'POST',
            'request':  {'email': 'user@example.com', 'password': '••••••••'},
            'response': {'access': '<jwt>', 'refresh': '<jwt>'},
        },
        'auth/token/refresh': {
            'url':      reverse('token_refresh', request=request),
            'method':   'POST',
            'request':  {'refresh': '<jwt>'},
            'response': {'access': '<new_jwt>'},
        },
        'auth/token/verify': {
            'url':      reverse('token_verify', request=request),
            'method':   'POST',
            'request':  {'token': '<jwt>'},
            'response': {},
        },
        'auth/register/confirm': {
            'url':      reverse('registration_confirm', request=request),
            'method':   'POST',
            'request':  {
                'email': 'user@example.com',
                'password': '',    # optional if third‑party auth
                'confirm_password': ''  # optional if third‑party auth
            },
            'response': {
                'id': 60,
                'email': 'user@example.com',
            },
        },
        'account/me': {
            'url':      reverse('user-detail', request=request),
            'method':   'GET',
            'response': {
                'id': 60,
                'email': 'user@example.com',
                'is_staff': False,
                'is_active': True,
                'profile': {
                    'phone': '+1234555678',
                    'is_phone_verified': False,
                }
            },
        },
    }
    return Response(data)
