import streamlit as st
import pandas as pd
from groq import Groq
import os

st.set_page_config(page_title="Akademik Araştırma Asistanı", page_icon="🎓", layout="wide")

# CSS KISMI 
st.markdown("""
<style>
    div.stButton > button:first-child {
        background-color: #28a745 !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        border: 2px solid #1e7e34 !important;
    }
    .akademik-rapor {
        background-color: #ffffff !important;
        padding: 35px;
        border-radius: 12px;
        border-left: 8px solid #2c3e50; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        font-family: 'Times New Roman', serif; 
        color: #111111 !important; /* Ana metin rengi siyah/koyu gri */
    }
    .akademik-rapor h1, .akademik-rapor h2, .akademik-rapor h3 {
        color: #2c3e50 !important;
        font-size: 26px !important;
        border-bottom: 1px solid #ddd;
        padding-bottom: 10px;
        background-color: transparent !important;
    }
    /* Rapor içindeki tüm yazı, liste, kalın yazı renklerini siyaha zorluyoruz */
    .akademik-rapor p, .akademik-rapor li, .akademik-rapor span, .akademik-rapor strong, .akademik-rapor b {
        font-size: 19px !important;
        line-height: 1.8 !important;
        color: #111111 !important; 
        background-color: transparent !important; /* Mavi arka plan oluşmasını engeller */
    }
</style>
""", unsafe_allow_html=True)

# API'ye istek atan fonksiyon
def run_academic_agent(full_stats):
    api_key = "BURAYA_KENDI_GROQ_API_ANAHTARINI_YAZ" 
    client = Groq(api_key=api_key)

    
    prompt = f"""
    SİSTEM VE KESİN KURALLAR:
    Sen uluslararası alanda saygı gören, otoriter, Q1 dergilerde editörlük yapan sert bir "Klinik Araştırma Mentoru"sun.
    Karşındaki hekime net, spesifik, hemen aksiyon alınabilir ve derin bir klinik/patofizyolojik vizyon katan tavsiyeler vereceksin.
    
    USLÜP VE DİL UYARISI: Pısırık, yuvarlak ve tekrarlayan cümlelerden nefret edersin. "Yapabiliriz, edebiliriz, incelenebilir, belirlemek" gibi zayıf kelimeleri KESİNLİKLE KULLANMA. Metni uzatmak için ASLA aynı bağlaçları, benzer cümle yapılarını veya "verilerin derinlemesine analizini yapmak gerekmektedir" gibi klişe dolgu cümlelerini tekrar etme! Her cümlen taze bir bilgi, yeni bir klinik çıkarım veya keskin bir eleştiri taşımalıdır.
    
    DETAYLANDIRMA STRATEJİSİ (ÇOK ÖNEMLİ): Her başlık altında hekimin ufkunu açacak DOYURUCU paragraflar yaz. Ancak metni boş lafla sakız gibi uzatma. Paragrafları doldurmak için SADECE elimizdeki verilerin (Yaş, BMI, Glikoz, HT, vb.) klinikte hücresel, endokrin ve kardiyovasküler düzeyde birbirini nasıl tetiklediğini (neden-sonuç ilişkisini, patofizyolojik mekanizmaları) otoriter bir dille anlat. Sahte istatistik veya hayali ilaç uydurmak yasaktır; eldeki sınırlı veriden maksimum klinik, hücresel ve anatomik çıkarımı yap.

    📊 KLİNİK VERİ SETİ ÖZETİ:
    --------------------------------------------------
    - Toplam Hasta Sayısı: {full_stats['n']}
    - İnme (Stroke) Prevalansı: %{full_stats['stroke_rate']}
    - İnme Grubunda Ortalama Yaş: {full_stats['age_inme']}
    - İnme Grubunda Ortalama BMI: {full_stats['bmi_inme']}
    - İnme Grubunda Ortalama Glikoz: {full_stats['glucose_inme']}
    - İnme Grubunda Hipertansiyon: %{full_stats['ht_rate']}
    - İnme Grubunda Kalp Hastalığı: %{full_stats['heart_rate']}
    - Baskın İş Tipi: {full_stats['work_impact']}
    - İkamet Tipi Dağılımı: {full_stats['residence_impact']}
    - Medeni Durum Dağılımı: {full_stats['marriage_impact']}
    - Sigara Kullanım Dağılımı: {full_stats['smoking_impact']}
    --------------------------------------------------

    GÖREV (Her maddeyi en az 5-6 özgün cümlelik, hücresel ve veriye dayalı derin analizlerle, otoriter bir dille yaz):

    1. Makale ve Bilimsel Yayın Yazmak (Spesifik Hipotez Ver):
    - KESİNLİKLE zayıf araştırma amaçları yazma. 
    - Verideki değişkenleri (Örn: Yaş, Glikoz, İkamet) çaprazlayarak test edilebilir, cesur ve spesifik bir HİPOTEZ CÜMLESİ kur. 
    - Sadece hipotezi verip bırakma; bu hipotezin NEDEN Q1 dergilerde ses getireceğini, elimizdeki %{full_stats['stroke_rate']} inme oranı ve {full_stats['glucose_inme']} glikoz ortalaması gibi verilerin endotel hasarı veya koagülasyon kaskadındaki rolüyle destekleyerek argümanlaştır.
    
    2. Yeni Araştırma Projesi:
    - Bu veri setinin sınırlarını aşacak, gelecekte yapılacak prospektif bir çalışmanın tam adını ve temel araştırma sorusunu yaz. Bu yeni çalışmanın literatürdeki hangi devasa boşluğu dolduracağını klinik bir vizyonla tartış.

    3. Hastaları Doğru Teşhis ve Tedavi Etmek (Klinik Kırmızı Alarm):
    - Poliklinik kapısından giren hangi profildeki hasta acil inme riski altındadır? Verilerimizdeki %{full_stats['ht_rate']} HT ve %{full_stats['heart_rate']} Kalp Hastalığı oranlarını kullanarak hedef hasta profilini çiz. Bu hastaya poliklinikte hemodinamik ve metabolik açılardan neden standart dışı, daha agresif yaklaşılması gerektiğini detaylandır.

    4. Hasta Simülasyonu (Canlı Klinik Senaryo):
    - Verilerimizdeki inme grubunun ortalama değerlerini (Yaş: {full_stats['age_inme']}, BMI: {full_stats['bmi_inme']}, Glikoz: {full_stats['glucose_inme']}, vs.) tek bir hayali hastada topla. 
    - Bu hastaya bir isim ver. 
    - Polikliniğe geliş şikayetini, anamnezini ve ilk muayene bulgularını bu verilere dayanarak, hekime gerçekten nöroloji acilinde hissettirecek dramatik ve gerçekçi bir senaryo şeklinde yaz.

    5. Tıbbi Eğitim ve Öğretim Yapmak:
    - Asistanlara sunmak üzere "Tipik bir inme vakası" kurgula. Elimizdeki yaş/BMI verilerinin bu vakada mikrovasküler düzeyde nasıl birleştiğini asistanlara amfide ders verir gibi sert ve otoriter bir şekilde anlat.

    6. Konferans ve Seminer Sunumu:
    - Verilerimizden en şaşırtıcı istatistiği seç ve yaklaşan bir kongre için dinleyicileri uyanık tutacak "Çarpıcı ve Provokatif bir Sunum Başlığı" öner. Bu başlığın altını salondaki hekimlere tam olarak hangi verilerle ve hangi klinik uyarılarla dolduracağını açıkla.

    7. Hasta Kayıt Yönetimi:
    - {full_stats['n']} hastanın verisinde hastane otomasyonuna (EHR) girilirken en çok hangi parametrelerin zorunlu alan yapılması gerektiğini klinik bir gerekçeyle vurgula. Veri eksikliğinin hastaneye maliyetini ve geliştirilecek yapay zeka/makine öğrenmesi (AI/ML) modellerinin doğruluk payını nasıl çökerteceğini acımasızca anlat.

    8. Bilgi Güncelleme:
    - Verimizdeki Glikoz ({full_stats['glucose_inme']}) ortalamasının, güncel inme koruyucu hekimlik kılavuzlarındaki hedeflerden ne kadar saptığını ve bu kronik hiperglisemi tablosunun hekimin günlük pratiğinde ne anlama geldiğini yorumla.

    9. Veri Setinin Eksikleri (Acımasız Limitasyon Eleştirisi):
    - Bu makalenin Q1 bir dergiden anında red yemesine sebep olacak en büyük 3 eksik değişkeni (veri setimizde OLMAYAN: Örn. HbA1c, LDL, Görüntüleme vb.) yaz. Neden bu eksiklerin modeli zayıflattığını metodolojik olarak derinlemesine ve çok sert bir dille eleştir.
"""

    try:
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.75, 
        )
        return completion.choices[0].message.content
    except Exception as e:
        return "Hata oluştu: " + str(e)


# Arayüz Başlıkları
st.title("🎓 Akademik Araştırma & Yayın Danışmanı")
st.write("Veri setinizden akademik değer üreten yapay zeka asistanı.")

# Dosya yükleme alanı
uploaded_file = st.sidebar.file_uploader("Klinik Veri Setini Yükle (Excel)", type=["xlsx"])

if uploaded_file != None:
    # Dosyayı pandas ile oku
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    
    # İnme olan hastaları ayır 
    if 'stroke' in df.columns: 
        inme_df = df[df['stroke'] == 1]
    else:
        
        inme_df = pd.DataFrame()    # Eğer stroke kolonu yoksa boş dataframe oluştur
    if len(inme_df) > 0:    # Eğer inme hastası varsa analiz işlemlerini yap
        
        # Değişkenleri hesaplıyoruz
        toplam_hasta = len(df)
        
        inme_orani = df['stroke'].mean() * 100
        inme_orani = round(inme_orani, 2)
        
        ortalama_yas = inme_df['age'].mean()
        ortalama_yas = round(ortalama_yas, 1)
        
        glikoz_seviyesi = inme_df['avg_glucose_level'].mean()
        glikoz_seviyesi = round(glikoz_seviyesi, 1)
        
        hipertansiyon_orani = inme_df['hypertension'].mean() * 100
        hipertansiyon_orani = round(hipertansiyon_orani, 2)
        
        kalp_hastaligi_orani = inme_df['heart_disease'].mean() * 100
        kalp_hastaligi_orani = round(kalp_hastaligi_orani, 2)
        
        # Kolon kontrolleri
        if 'bmi' in df.columns:
            bmi_degeri = round(inme_df['bmi'].mean(), 1)
        else:
            bmi_degeri = "Bilinmiyor"
            
        if 'work_type' in inme_df.columns:
            is_tipi = inme_df['work_type'].value_counts().idxmax()
        else:
            is_tipi = "Bilinmiyor"
            
        if 'Residence_type' in inme_df.columns:
            ikamet_tipi = inme_df['Residence_type'].value_counts().to_dict()
        else:
            ikamet_tipi = "Bilinmiyor"
            
        if 'ever_married' in inme_df.columns:
            medeni_durum = inme_df['ever_married'].value_counts().to_dict()
        else:
            medeni_durum = "Bilinmiyor"
            
        if 'smoking_status' in inme_df.columns:
            sigara_durumu = inme_df['smoking_status'].value_counts().to_dict()
        else:
            sigara_durumu = "Bilinmiyor"

        # Sözlüğü oluşturuyoruz
        full_stats = {
            'n': toplam_hasta,
            'stroke_rate': inme_orani,
            'age_inme': ortalama_yas,
            'bmi_inme': bmi_degeri,
            'glucose_inme': glikoz_seviyesi,
            'ht_rate': hipertansiyon_orani,
            'heart_rate': kalp_hastaligi_orani,
            'work_impact': is_tipi,
            'residence_impact': ikamet_tipi,
            'marriage_impact': medeni_durum,
            'smoking_impact': sigara_durumu
        }
        
        st.sidebar.success("Veriler Başarıyla Analiz Edildi.")
        
        # Buton
        basildi_mi = st.button("✅ YAPAY ZEKA DANIŞMANLIĞINI BAŞLAT", use_container_width=True)
        
        if basildi_mi == True:
            st.write("Uzman AI verileri inceliyor ve yayın stratejisi geliştiriyor. Lütfen bekleyin...")
            
            rapor = run_academic_agent(full_stats)
            
            # Çıktıyı div içinde gösteriyoruz
            st.markdown("### 📝 VERİLER SONUCUNDA HEKİME SUNULAN ÖNERİLER")
            st.markdown(f'<div class="akademik-rapor">\n\n{rapor}\n\n</div>', unsafe_allow_html=True)
            
            st.download_button("📥 Akademik Raporu İndir", data=rapor, file_name="Akademik_Yol_Haritasi.txt")
            
    else:
        st.error("Veri setinde analiz edilecek inme vakası bulunamadı.")
else:
    st.info("👈 Analize başlamak için lütfen klinik verilerinizi içeren Excel dosyasını soldaki menüden yükleyin.")