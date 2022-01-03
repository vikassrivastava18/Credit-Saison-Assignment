import json

from django.core.exceptions import ValidationError
from django.db.models import Count, Min, Max
from django.http import JsonResponse
from django.shortcuts import render
from .models import Searched
from django.views.decorators.csrf import csrf_exempt
# import request


def index(request):

    # Display the main/home page
    return render(request, "index.html")

@csrf_exempt
def search(request, card_id):
    # Add the searched card in db if it's valid
    if request.method == 'POST':
        try:
            card = Searched.objects.create(card_number=card_id)
            card_details = request.get('https://lookup.binlist.net/'+ str(card_id))
            print("card details", card_details)
            return JsonResponse({
                "details": card_details.jsonify()
            }, status=201)
        # Validation error from db
        except ValidationError:
            return JsonResponse({
                "error": f"Card number {card_id} is not a valid."
            }, status=400)


@csrf_exempt
def statistics(request):

    # Group By the card numbers and add latest, oldest timestamp
    result = Searched.objects.values('card_number').annotate(card_count=Count('card_number'),
                                                             latest=Min('time_stamp'),
                                                             oldest = Max('time_stamp')).order_by('-dcount')

    return JsonResponse({
        "result": result.jsonify()
    }, status=200)