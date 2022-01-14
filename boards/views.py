import json

from django.shortcuts import render
from django.views     import View
from django.db        import transaction
from django.http      import JsonResponse

from boards.models import Board, Image

class BoardCreateView(View):
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

class BoardReadView(View):
    def get(self, request, board_id):
        try:
            if not Board.objects.filter(id=board_id).exists():
                return JsonResponse({'MESSAGE':'board_not_exists'}, status=404)

            board        = Board.objects.get(id=board_id)
            thumb_img    = Image.objects.get(board_id=board.id, type='thumb')
            content_imgs = Image.objects.filter(board_id=board.id, type='content')

            results = {
                'title' : board.title,
                'content' : board.content,
                'type' : board.type,
                'thumb_img' : thumb_img.img_url,
                'content_imgs' : [
                    content_img.img_url for content_img in content_imgs
                ]
            }

            return JsonResponse(results, status=200)

        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)

