# InternTrack API

Staj ve iş başvurularını takip eden bir REST API.

## Problem
Bilgisayar mühendisliği öğrencileri staj ve iş başvurularını çoğu zaman Excel tablolarında veya notlarda dağınık biçimde tutuyor. Hangi şirkete ne zaman başvurulduğu, hangi başvurunun mülakat aşamasında olduğu ya da reddedildiği kolayca kaybolabiliyor.

## Kimin için?
Staj veya ilk iş arayan bilgisayar mühendisliği öğrencileri ve yeni mezunlar.

## Çözüm
InternTrack API ile kullanıcı başvurularını (şirket, pozisyon, tarih, durum) tek yerde kaydedebilir, durumlarını güncelleyebilir ve duruma göre filtreleyebilir.

## Pano
Proje panosu: https://github.com/users/Melih-Eserler/projects/1

## Teknolojiler
Python, FastAPI, Uvicorn, Pydantic

## Çalıştırma adımları

Gereksinim: Python 3.10 veya üstü.

```bash
git clone https://github.com/Melih-Eserler/intern-track-api.git
cd intern-track-api
python -m venv venv
```

Sanal ortamı etkinleştirin:

- Windows (PowerShell): `venv\Scripts\Activate.ps1`
- Mac/Linux: `source venv/bin/activate`

Paketleri kurup uygulamayı başlatın:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Uygulama `http://127.0.0.1:8000` adresinde çalışır. Etkileşimli arayüz: **http://127.0.0.1:8000/docs**

> Not: Veriler bellekte tutulur. Uygulama yeniden başlatıldığında kayıtlar sıfırlanır, bu yüzden denemeye önce POST ile kayıt ekleyerek başlayın.

## İki özelliği deneme

Tarayıcıda `http://127.0.0.1:8000/docs` sayfasını açın.

### Özellik 1: Başvuru ekleme ve listeleme (#1)

1. **POST /applications** → *Try it out*, gövdeye şunu yazıp *Execute* edin:
   ```json
   {
     "company": "Aselsan",
     "position": "Yazılım Stajyeri",
     "applied_date": "2026-11-17"
   }
   ```
   Beklenen: `201` ve yanıtta `"id": 1`, `"status": "basvuruldu"`.
2. **GET /applications** → *Try it out* → *Execute*. Beklenen: `200` ve eklenen kayıt listede.
3. POST'ta `company` alanını silip gönderin. Beklenen: `422`.

### Özellik 2: Durum güncelleme ve filtreleme (#2)

1. Önce yukarıdaki gibi en az bir kayıt ekleyin (id 1).
2. **PATCH /applications/{application_id}/status** → `application_id` = `1`, gövde:
   ```json
   { "status": "mulakat" }
   ```
   Beklenen: `200`, yanıtta `"status": "mulakat"`.
   Geçerli durumlar: `basvuruldu`, `mulakat`, `reddedildi`, `kabul`.
3. Gövdeye `{ "status": "xyz" }` yazın. Beklenen: `422`. `application_id` = `999` verin. Beklenen: `404`.
4. **GET /applications** → `status` alanına `mulakat` yazıp *Execute* edin. Beklenen: yalnızca durumu mülakat olan kayıtlar.

## Planlanan işler
Silme, istatistik özeti, otomatik testler ve Docker desteği panoda "Todo" sütununda planlanmıştır.