import pandas as pd
from groq import Groq
import os

API_KEY = "BURAYA_KENDI_GROQ_API_ANAHTARINI_YAZ"

def run_agent(full_stats):
    client = Groq(api_key=API_KEY)

   
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
        return f"Hata: {str(e)}"

if __name__ == "__main__":
    dosya_adi = "healthcare-dataset-stroke-data.xlsx"
    if os.path.exists(dosya_adi):
        df = pd.read_excel(dosya_adi)
        inme_df = df[df['stroke'] == 1]
        
        full_stats = {
            'n': len(df),
            'stroke_rate': round(df['stroke'].mean() * 100, 2),
            'age_inme': round(inme_df['age'].mean(), 1),
            'gender_dist': inme_df['gender'].value_counts().to_dict(),
            'bmi_inme': round(inme_df['bmi'].mean(), 1) if 'bmi' in df.columns else "Bilinmiyor",
            'glucose_inme': round(inme_df['avg_glucose_level'].mean(), 1),
            'ht_rate': round(inme_df['hypertension'].mean() * 100, 2),
            'heart_rate': round(inme_df['heart_disease'].mean() * 100, 2),
            'work_impact': inme_df['work_type'].value_counts().idxmax(),
            'residence_impact': inme_df['Residence_type'].value_counts().to_dict(),
            'marriage_impact': inme_df['ever_married'].value_counts().to_dict(),
            'smoking_impact': inme_df['smoking_status'].value_counts().to_dict()
        }
        
        print("✅ Akademik analiz için veriler hazırlandı. Ajan danışmanlık yapıyor...")
        print(run_agent(full_stats))
    else:
        print("Hata: Dosya bulunamadı.")