# 📊 AI-Stat-Agent v2.0

Bu proje, ham Excel verilerini otonom bir şekilde analiz edebilen, veri manipülasyonu yapabilen ve kullanıcıyla mesleki bağlamda (Doktor, Yazılımcı, Polis vb.) iletişim kurabilen **Ajan tabanlı bir Yapay Zeka** asistanıdır.

v1.0 sürümündeki statik API çağrısı yapısı, v2.0 ile yerini **Agentic Workflow (Ajan İş Akışı)** mimarisine bırakmıştır.


## 🌟 v2.0 ile Gelen Majör Yenilikler

* **Otonom Akıl Yürütme (Reasoning):** Ajan artık sadece metin üretmiyor; soruları yanıtlamak için arka planda Python (Pandas) kodları yazar, çalıştırır ve kesin sonuçları kullanıcıya sunar.
* **Dinamik Persona (Bukalemun Modu):** Kullanıcının uzmanlık alanına göre (Sağlık, Hukuk, Teknik) terminolojisini ve analiz derinliğini otomatik olarak optimize eder.
* **Veri Geliştirme (Feature Engineering) Önerileri:** Veri kalitesini artırmak için eksik veri yönetimi ve yeni özellik oluşturma stratejileri sunar.
* **Hata Toleranslı Çıktı Yönetimi:** "Output Parsing" hatalarını kendi kendine tespit edip düzelten bir yapıya sahiptir.

## 🛠️ Teknoloji Yığını (Tech Stack)

* **LLM Orchestration:** LangChain
* **Model:** Llama-3.1-8b-instant (via Groq Cloud)
* **Veri İşleme:** Pandas, Openpyxl
* **Dil:** Python 3.x
* **Ortam Yönetimi:** Dotenv, Virtualenv

## 🚀 Kurulum ve Kullanım

1.  **Bağımlılıkları Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Yapılandırma:** `.env` dosyanıza `GROQ_API_KEY` bilginizi ekleyin.
3.  **Başlatma:**
    ```bash
    python main.py
    ```

---

## 👨‍💻 Geliştirici Notu
Bu proje, bir Bilgisayar Mühendisliği öğrencisinin **LLM'leri otonom araçlarla (Tool Calling) birleştirme** ve gerçek dünya verileri (Sağlık/İnme verisi) üzerinde anlamlı içgörüler üretme yolculuğudur. Proje, statik modellerin ötesine geçerek 'karar verebilen' sistemler inşa etme vizyonuyla geliştirilmiştir.

