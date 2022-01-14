import json

from django.shortcuts import render
from django.views     import View
from django.db        import transaction
from django.http      import JsonResponse

from boards.models import Board, Image

class BoardView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            title       = data['title']
            content     = data['content']
            post_type   = data['post_type']
            thumb_img   = data['thumb_img']
            content_img = data['content_img']

            with transaction.atomic():
                board = Board.objects.create(
                    title = title,
                    content = content,
                    type = post_type
                )

                Image.objects.create(
                    img_url  = thumb_img,
                    type     = 'thumb',
                    board_id = board.id
                )

                for img in content_img:
                    Image.objects.create(
                        img_url  = img,
                        type     = 'content',
                        board_id = board.id
                    )

            return JsonResponse({'MESSAGE':'board_created'}, status=201)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

