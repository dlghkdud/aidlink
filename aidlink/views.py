import requests
import json
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests, json
from django.shortcuts import render
from django.conf import settings
from .models import Main, HOSPITAL_BASIC_INFO
import xml.etree.ElementTree as ET
from django.http import JsonResponse

API_KEY = settings.API_KEY

def index(request):
    main = Main.objects.order_by('-create_date')
    context = {'main':main}
    return render(request, '../templates/main.html',context)

def show_hospitals(request):
    hospitals = HOSPITAL_BASIC_INFO.objects.all()  # 데이터베이스에서 병원 정보 가져오기

    # 병원 정보를 리스트로 만들어서 JSON 형태로 변환
    hospital_data = []
    for hospital in hospitals:
        hospital_info = {
            'latitude': float(hospital.wgs_84_lat),  # 형변환
            'longitude': float(hospital.wgs_84_lon),  # 형변환
            'title': hospital.duty_name
        }
        hospital_data.append(hospital_info)

    # JSON으로 변환한 데이터를 JavaScript로 안전하게 전달하기 위해 escaping 처리
    hospital_data_json = json.dumps(hospital_data)  # JSON 데이터 생성

    print(hospital_data_json)  # 확인용으로 출력

    context = {'hospital_data_json': hospital_data_json}
    return render(request, 'main.html', context)


@api_view(['GET'])
def products(request):
    print("products")
    url = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytListInfoInqire'
    params = {
        'Q0': '서울특별시',
        'Q1': '강남구'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        root = ET.fromstring(response.content)

        hospital_data = []

        for item in root.findall('.//item'):
            data = {
                'latitude': float(item.find('wgs84Lat').text),
                'longitude': float(item.find('wgs84Lon').text),
                'title': item.find('dutyName').text,    #병원명
                'dutyTel1': item.find('dutyTel1').text, #대표번호
                'dutyTel3': item.find('dutyTel3').text, #응급실 번호
                'dutyAddr': item.find('dutyAddr').text  #주소
            }
            hospital_data.append(data)
        return JsonResponse(hospital_data, safe=False)

    except requests.RequestException as e:
        print(f"요청 실패: {e}")
        return render(request, 'error_template.html', {'error_message': '데이터를 가져오는 데 실패했습니다.'})