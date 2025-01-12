Langkah-Langkah Instalasi

1. Kloning Repositori
Unduh kode proyek dari repositori Git:
$ git clone https://github.com/rmunggaran/TestProgrammer_FastPrintIndonesia.git
$ cd <NAMA_FOLDER_PROYEK>

2. Buat Virtual Environment
Buat lingkungan virtual untuk mengisolasi dependensi proyek:
$ python -m venv venv
Aktifkan virtual environment:

Windows:
$ venv\Scripts\activate

Mac/Linux:
$ source venv/bin/activate

3. Instal Dependensi
Instal semua dependensi yang dibutuhkan dari file requirements.txt:
$ pip install -r requirements.txt

4. Konfigurasi Database
Pengaturan Database Lain (Opsional):
Jika Anda ingin menggunakan MySQL sesuaikan bagian DATABASES di settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # atau 'django.db.backends.postgresql'
        'NAME': 'produk',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',  # Untuk MySQL (5432 untuk PostgreSQL)
    }
}

Pastikan Anda sudah menginstal driver database:
Untuk MySQL:
$ pip install mysqlclient

5. Migrasi Database
Jalankan perintah berikut untuk membuat tabel database:
$ python manage.py migrate

7. Jalankan Server Lokal
Jalankan server pengembangan lokal Django:
$ python manage.py runserver
Server akan berjalan di http://127.0.0.1:8000/. Anda dapat membuka URL tersebut di browser untuk mengakses aplikasi.