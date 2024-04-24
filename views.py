from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseNotFound


# Create your views here.
monthly_challenges = {
    "january": "this is work!",
    "february": "walkout",
    "march": "goint to buy",
    "april": "out of office",
    "may": "ingenzi janu",
    "june": "hello world",
}


def monthly_challenges_by_number(request, month):
    return HttpResponse(month)


def mounthly_challenges(request, month):
    try:
        challenges_text = monthly_challenges[month]
        return HttpResponse(challenges_text)
    except:
        HttpResponseNotFound("this month not supported")
