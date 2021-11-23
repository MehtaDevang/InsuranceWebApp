from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse, HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from .lib import *
from rest_framework.permissions import IsAuthenticated, AllowAny
import json
# Create your views here.

# @api_view(['GET', 'POST'])
@csrf_exempt
@permission_classes((AllowAny,))
def getPolicy(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        print("this is the id", id)
        if id is None or id == '':
            return JsonResponse({
                'message' : 'Policy Number or Customer Id was not provided'
            }, status=200)

        policy_details = get_policy_details(id)
        print("this is policy details : ", policy_details)
        if policy_details is None or len(policy_details) < 1:
            return JsonResponse({
                'message' : 'No policy matching with the provided id was found.'
            })

        return JsonResponse({
            'policy_id' : policy_details['Policy_id'].values[0],
            'purchase_date' : policy_details['Date of Purchase'].values[0],
            'customer_id' : policy_details['Customer_id'].values[0],
            'fuel' : policy_details['Fuel'].values[0],
            'vehicle_segment' : policy_details['VEHICLE_SEGMENT'].values[0],
            'premium' : policy_details['Premium'].values[0],
            'bodily_injury_liability' : policy_details['bodily injury liability'].values[0],
            'personal_injury_protection' : policy_details['personal injury protection'].values[0],
            'property_damage_liability' : policy_details['property damage liability'].values[0],
            'collision' : policy_details['collision'].values[0],
            'comprehensive' : policy_details['comprehensive'].values[0],
            'gender' : policy_details['Customer_Gender'].values[0],
            'income_group' : policy_details['Customer_Income group'].values[0],
            'region' : policy_details['Customer_Region'].values[0],
            'marital_status' : policy_details['Customer_Marital_status'].values[0]
        })

