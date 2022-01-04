import json
import requests
from django.core.exceptions import ValidationError
from django.db.models import Count, Min, Max
from django.http import JsonResponse
from django.shortcuts import render
# from requests import JSONDecodeError

from .models import Searched
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


def index(request):

    # Display the main/home page
    return render(request, "index.html")


@csrf_exempt
def search(request, card_id):

    # Add the searched card in db if it's valid
    if request.method == 'POST':
        try:
            # Create an entry in Database for the Card
            Searched.objects.create(card_number=card_id)
            # Get the Card details
            print("card added")
            url = 'https://lookup.binlist.net/' + str(card_id)
            card_details = requests.get(url).json()
            print("card_details", card_details['scheme'],card_details['type'], card_details['bank']['name'])
            return JsonResponse({
                "scheme": card_details['scheme'],
                "type": card_details['type'],
                "bank": card_details['bank']['name']
            }, status=201)

        # Validation error from db
        except ValidationError:
            return JsonResponse({
                "error": f"Card number {card_id} is not a valid."
            }, status=400)

        # # Error in JSON
        # except JSONDecodeError:
        #     return JsonResponse({
        #         "error": f"Card information not found."
        #     }, status=400)


@csrf_exempt
def statistics(request):

    # Group By the card numbers and add latest, oldest timestamp
    result = Searched.objects.values('card_number').annotate(card_count=Count('card_number'),
                                                             latest=Min('time_stamp'),
                                                             oldest=Max('time_stamp')).order_by('-card_count')

    result_json = []
    for r in result:
        result_json.append({r['card_number']: [r['card_count'], r['latest'], r['oldest']]})
    print("result json", result_json)
    # Send Json for the filtered data
    return JsonResponse({
        "result": result_json
    }, status=200)