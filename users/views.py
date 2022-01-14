import json
import requests

from django.shortcuts import redirect, render
from django.http      import JsonResponse
from django.views     import View

from grade_settings import STIBEE_API_KEY, STIBEE_URL, GRADE_LIST_ID, timeout
from users.models   import GradeUser


class MailSubscribeView(View):
    def post(self, request):
        try:
            data    = json.loads(request.body)
            email   = data['email']

            headers = {
                'AccessToken'  : STIBEE_API_KEY,
                'Content-Type' : 'application/json; charset=utf-8'
            }

            json_data = {
                'eventOccuredBy' : 'SUBSCRIBER',
                'confirmEmailYN' : 'N',
                'subscribers'    : [
                    {
                        'email' : email
                    }
                ]
            }

            if GradeUser.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE':'existing_grade_user'}, status=400)

            requests.post(STIBEE_URL.format(listId=GRADE_LIST_ID), headers=headers, json=json_data, timeout=timeout)

            GradeUser.objects.create(
                email=email
            )

            return JsonResponse({'MESSAGE': 'grade_user_registered'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)


