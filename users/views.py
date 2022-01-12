import json

from django.shortcuts import render
from django.http      import JsonResponse

from grade_settings import STIBEE_API_KEY
from users.models   import GradeUser, PedalUser

class GradeMailSubscribeView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']

            if GradeUser.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE':'existing_user'}, status=400)

            GradeUser.objects.create(
                email=email
            )

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)


