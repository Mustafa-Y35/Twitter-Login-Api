# Flask Kimlik Doğrulama Sistemi

Bu proje, Flask ile geliştirilmiş kullanıcı kimlik doğrulama sistemidir. Kullanıcılar, kullanıcı adı ve şifre ile giriş yapabilir ve çıkış yapabilir.

## Kurulum
1. `git clone https://github.com/kullanici-adi/proje-adi.git`
2. `cd proje-adi`
3. `pip install -r requirements.txt`
4. `python create_db.py`
5. `python add_user.py`
6. `python views.py` (Flask uygulamasını başlat)

## Kullanım
- `GET /`: Giriş sayfası
- `POST /login`: Kullanıcı giriş işlemi
- `GET /logout`: Kullanıcı çıkışı
- `POST /logout`: API çıkış işlemi
- `GET /current-user`: Mevcut kullanıcı bilgisi

## Dosya Yapısı
- `app.py`: Ana Flask uygulaması
- `create_db.py`: Veritabanı oluşturma scripti
- `add_user.py`: Varsayılan kullanıcı ekleme scripti
- `views.py`: Flask view'ları
- `templates/`: HTML şablonları
  - `index.html`: Giriş sayfası
- `static/`: Statik dosyalar
  - `css/`: CSS dosyaları
    - `style.css`: Giriş sayfası stil dosyası

## Lisans

Bu proje açık kaynaklıdır ve [MIT Lisansı](LICENSE) altında dağıtılmaktadır.
