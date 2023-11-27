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
from .models import Main, HOSPITAL_BASIC_INFO, LOCATIONS

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
    return render(request, '../templates/main.html', context)


@api_view(['GET'])
def products(request):
    url = 'kQnQFRU7OHDKRkafFKoYJfu%2B4JJBugnF%2BlwPKX1Gg8IlRPHAJq4%2FUtbVSh2wK7zzmF0xHWronkOI67LCGZM38g%3D%3D'
    # API 데이터를 생성
    params = {
        '주소(시도)' : '서울시',
        '주소(시군구)' : '강남구',
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # 상태 코드에 따라 HTTPError 발생

        data = response.json()

        for item in data['results']:
            your_model_instance = HOSPITAL_BASIC_INFO(
                hpid = item['기관ID'],
                phpid = item['구기관ID'],
                duty_emcls = item['응급의료기관분류'],
                duty_emcls_name = item['응급의료기관분류명'],
                duty_addr = item['주소'],
                duty_name = item['기관명'],
                duty_tel1 = item['대표전화1'],
                duty_tel3 = item['응급실전화'],
                wgs_84_lon = item['병원경도'],
                wgs_84_lat = item['병원위도'],
                center_type = item['응급/외상센터구분'],
            )
            your_model_instance.save()

        return render(request, '../templates/main.html', {'data': data})
    
    except requests.RequestException as e:
        # 요청 실패 처리
        print(f"요청 실패: {e}")
        return render(request, 'error_template.html', {'error_message': '데이터를 가져오는 데 실패했습니다.'})