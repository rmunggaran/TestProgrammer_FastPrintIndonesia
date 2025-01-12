from datetime import datetime
import sys
import os
import django
import hashlib
import requests
import hashlib

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "produk_project.settings")
django.setup()

from produk.models import Produk, Kategori, Status

def fetch_and_save_products():
    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
    username = "tesprogrammer120125C11"

    date = datetime.now()
    password = f"bisacoding-12-01-25"
    password_md5 = hashlib.md5(password.encode()).hexdigest()  

    print(f"Username: {username}")
    print(f"Password (MD5): {password_md5}")

    session = requests.Session()

    headers = {
        'X-Credentials-Username': username,
        'X-Credentials-Password': password_md5
    }
    data = {
        'username': username,
        'password': password_md5  
    }

    response = session.post(url, headers=headers,data=data)

    if response.status_code == 200:
        data = response.json()
        
        if data['error'] == 0:
            products = data['data']
            for item in products:
                kategori, _ = Kategori.objects.get_or_create(nama_kategori=item['kategori'])
                status, _ = Status.objects.get_or_create(nama_status=item['status'])
                
                Produk.objects.update_or_create(
                    id=item['id_produk'],
                    defaults={
                        'nama_produk': item['nama_produk'],
                        'harga': item['harga'],
                        'kategori': kategori,
                        'status': status
                    }
                )
            print("Data berhasil disimpan ke database.")
        else:
            print(f"Error dalam respons API: {data['ket']}")
    else:
        print(f"Failed to fetch data: {response.status_code}")
        print("Response Body:", response.text)

    # print(f"Response Status Code: {response.status_code}")

    # print(f"Response Body: {response.text}")

    # print(f"Response Headers: {response.headers}")

    # print(f"Cookies: {response.cookies}")

fetch_and_save_products()


