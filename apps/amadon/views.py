# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    print "hit index post"

    context = {
        "somekey": "somedata"
    }

    return render(request,"amadon/index.html", context)


def purchase(request):

    if request.method == "POST":
        product_id  = int(request.POST['product_id'])
        quantity = int(request.POST['quantity'])

        if product_id == 1:
            request.session['amount'] = quantity * 19.99
        elif product_id == 2:
            request.session['amount'] = quantity * 29.99
        elif product_id == 3:
            request.session['amount'] = quantity * 49.99
        else:
            request.session['amount'] = 0
        
        if not 'total' in request.session:
            request.session['total'] = request.session['amount']
            request.session['count'] = quantity
        else:
            request.session['total'] += request.session['amount']
            request.session['count'] += quantity

    return redirect('/amadon/checkout')


def checkout(request):
    print "hit checkout"
    context = {
        "somekey": "somedata",
    }

    return render(request,"amadon/checkout.html",context)