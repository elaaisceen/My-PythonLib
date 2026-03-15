# 🎓 My FastAPI Application (FastAPI)

Bu proje, FastAPI kullanılarak geliştirilmiş basit bir asistan uygulamasıdır. Proje, modern web standartlarına uygun, hızlı ve otomatik dökümantasyon desteği sunan bir backend yapısına sahiptir.

## 🚀 Özellikler

* **FastAPI Framework:** Yüksek performanslı ve asenkron destekli yapı.
* **Otomatik Swagger UI:** `/docs` adresi üzerinden API test imkanı.
* **Hızlı Geliştirme:** Uvicorn `--reload` özelliği ile anlık kod takibi.

## 🛠️ Kurulum

1. **Projeyi Klonlayın veya İndirin:**
   ```bash
   git clone <proje-adresi>
   cd <proje-klasoru>

**2.Sanal Ortam (Virtual Environment) Oluşturun ve Aktifleştirin:**
    ```bash
    python -m venv venv
    # Windows için:
    .\venv\Scripts\activate

**3.Gerekli Kütüphaneleri Kurun:**
    ```bash
    pip install fastapi uvicorn

🏃 Uygulamayı Çalıştırma
Terminalinize aşağıdaki komutu yazarak sunucuyu başlatabilirsiniz:
    ```bash
    uvicorn main:app --reload

Sunucu başladıktan sonra tarayıcınızdan şu adrese giderek API'yi test edebilirsiniz:
👉 http://127.0.0.1:8000/docs

📌 API Uç Noktaları (Endpoints)

<table border="1">
  <thead>
    <tr>
      <th>Metot</th>
      <th>Uç Nokta</th>
      <th>Açıklama</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GET</td>
      <td>/check</td>
      <td>Sistem durumunu kontrol eder (Success döner).</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/docs</td>
      <td>İnteraktif Swagger dökümantasyonunu açar.</td>
    </tr>
  </tbody>
</table>
	
