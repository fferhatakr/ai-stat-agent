# 📊 AI-Stat-Agent v3.0

Bu proje, Excel tabanlı veri setlerini analiz edebilen, analiz sonuçlarını yorumlayabilen ve kullanıcıyla mesleki bağlama (Doktor, Yazılımcı, Hukukçu vb.) göre iletişim kurabilen ajan tabanlı hibrit bir **Yapay Zeka** asistanıdır.

v1.0 sürümündeki statik LLM çağrısı yapısı, v2.x ile birlikte yerini modüler **Agentic Workflow (Ajan İş Akışı)** mimarisine bırakmıştır.

Bu sürümde sistem, ham veriyi doğrudan modele vermek yerine önce deterministik analiz yapar, ardından LLM’i yalnızca yorumlama ve bağlamsal üretim katmanında kullanır.


## 🌟 v2.1 ile Gelen Geliştirmeler
### 🔹 Hibrit Analiz Mimarisi (Deterministic + Generative)
* **Deterministic Katman (Python/Pandas)** 
* **Excel veri yükleme**
* **Groupby analizleri**
* **Risk oranı hesaplamaları**

Temel istatistiksel karşılaştırmalar
* **Reasoning Katmanı (LLM)** 
* **Analiz sonuçlarını yorumlama**
* **Risk faktörlerini açıklama**
* **Bağlama uygun çıktı üretme**
* **Araştırma / içgörü önerileri sunma**
Bu yapı sayesinde model ham veri üzerinde spekülasyon yapmaz; analiz edilmiş sonuçlar üzerinden reasoning yapar.

### 🔹 Role-Aware Communication (Dinamik Persona)
Ajan, kullanıcı rolüne göre çıktı dilini adapte eder:
* **Technical Mode:** İstatistiksel ve teknik terminoloji kullanır
* **Non-Technical Mode:** Daha sade, açıklayıcı ve klinik dil kullanır
Aynı analiz, farklı uzmanlık seviyelerine göre farklı biçimde sunulabilir.

### 🔹 Modüler Agent Mimarisi
* **analysis/ →** Deterministic veri analizi
* **agent_core.py →** LLM reasoning katmanı
* **planner.py →** Görev yönlendirme
* **tools.py →** Veri yükleme ve yardımcı fonksiyonlar
* **config.py →** LLM yapılandırması

Bu yapı, sistemi basit bir script olmaktan çıkarıp genişletilebilir bir agent tasarımına dönüştürür.

## 🛠️ Teknoloji Yığını (Tech Stack)

* **Python 3.x**
* **Pandas**
* **Openpyxl**
* **LangChain**
* **Groq Cloud**
* **Llama-3.1-8b-instant**
* **Dotenv**
* **Virtualenv**

## 🚀 Kurulum ve Kullanım

1.  **Bağımlılıkları Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Yapılandırma:** 
`.env` dosyanıza `GROQ_API_KEY` bilginizi ekleyin.
    ```bash
        GROQ_API_KEY=your_key_here
    ```

3.  **Başlatma:**
    ```bash
    python main.py
    ```

---
## Projenin Amacı
Bu proje, LLM’leri doğrudan veri analizi yapan araçlar yerine, analiz edilmiş çıktılar üzerinden karar destek ve bağlamsal yorum üreten bir katman olarak konumlandırma deneyidir.

**Amaç:**

Veri → Deterministic Analiz → LLM Reasoning → Role-Based Sunum
şeklinde çalışan modüler bir ajan pipeline’ı kurmaktır.

## 👨‍💻 Geliştirici Notu
Bu proje, bir Bilgisayar Mühendisliği öğrencisinin:

* **LLM orchestration**
* **Tool–Model ayrımı**
* **Deterministic + Generative hibrit tasarım**
* **Modüler agent mimarisi**
alanlarında kendini geliştirme sürecinin bir parçasıdır.

Amaç, statik metin üreten sistemlerin ötesine geçerek veri temelli, bağlam duyarlı ve kontrollü yapay zeka ajanları tasarlamaktır.

