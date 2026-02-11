# 🎓 AI Stat Agent - Akademik Araştırma Asistanı

Bu proje, klinik veri setlerini (özellikle inme/stroke verileri) otomatik olarak analiz edip, elde edilen istatistiksel özetleri yapay zeka yardımıyla akademik bir yayın stratejisine dönüştüren bir asistan uygulamasıdır. 

Sistem, verileri okuyup oranları (yaş ortalaması, BMI, inme oranı vb.) hesaplar ve **Groq API** üzerinden çalışan Llama 3 modeline göndererek Q1 seviyesinde bir dergi editörü/mentorü gözüyle detaylı, patofizyolojik ve otoriter bir klinik rapor sunar.

## 🚀 Özellikler

- **Otomatik Veri Analizi:** Excel (`.xlsx`) formatındaki klinik verileri okur ve eksik verileri tolere ederek inme grubuna ait istatistikleri (ortalama, yüzde dağılımı vb.) çıkarır.
- **Yapay Zeka Destekli Raporlama:** Hastalık risk faktörlerini hücresel ve klinik düzeyde yorumlayan, makale hipotezi kuran ve hasta simülasyonları oluşturan gelişmiş bir prompt mühendisliği içerir.
- **Çift Kullanım Seçeneği:** Proje hem terminal üzerinden (`main.py`) tek tıkla çalıştırılabilir hem de **Streamlit** kullanılarak hazırlanan web arayüzü (`app.py`) üzerinden görsel olarak kullanılabilir.

## 📁 Proje Yapısı

```text
AI_STAT_AGENT/
├── agent/
│   └── stat_agent.py       # Yapay zeka promptunun ve Groq API çağrısının yapıldığı dosya
├── analysis/
│   └── statistics.py       # Gelecekteki gelişmiş veri analiz fonksiyonları için ayrılmış modül
├── app.py                  # Streamlit web arayüzü dosyası
├── main.py                 # Terminal üzerinden hızlı test için ana çalıştırma dosyası
├── healthcare-dataset-stroke-data.xlsx  # Test için kullanılan örnek klinik veri seti
└── requirements.txt        # Projenin çalışması için gereken Python kütüphaneleri
```

# 🛠️ Kurulum Adımları

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

---

## 1. Repoyu Bilgisayarınıza İndirin (Clone)
```bash
git clone https://github.com/KULLANICI_ADIN/ai-stat-agent.git
cd ai-stat-agent
```

## 2. Sanal Ortam (Virtual Environment) Oluşturun ve Aktif Edin

**Windows için:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux için:**
```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Gerekli Kütüphaneleri Kurun
```bash
pip install -r requirements.txt
```

**(Not: Eğer requirements.txt dosyanız yoksa manuel olarak pip install pandas openpyxl groq streamlit komutunu çalıştırabilirsiniz.)**

## 4. API Anahtarı (Önemli) 
**Sistemin yapay zeka cevapları üretebilmesi için bir Groq API anahtarına ihtiyacı vardır. Geliştirme aşamasında API key kod içerisinde tanımlanmıştır ancak güvenliğiniz için Groq Console üzerinden kendi anahtarınızı alıp kod içerisindeki (app.py ve stat_agent.py) API_KEY değişkenine entegre etmeniz önerilir.**


## 💻 Kullanım

Projeyi iki farklı şekilde çalıştırabilirsiniz:

**Seçenek 1: Terminal Üzerinden Hızlı Analiz Sadece konsol çıktısı görmek istiyorsanız:**
```bash
python main.py
```
**Seçenek 2: Görsel Web Arayüzü (Streamlit) Grafiksel arayüzü başlatmak ve tarayıcı üzerinden Excel yükleyerek raporu indirmek için:**
```bash
streamlit run app.py
```
👥 Geliştiriciler
Ferhat