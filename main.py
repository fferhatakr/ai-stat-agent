import pandas as pd
import os
from agent.stat_agent import run_agent

def main():
    # Dosya yolunu kontrol edelim
    dosya_adi = "healthcare-dataset-stroke-data.xlsx"
    
    if os.path.exists(dosya_adi):
        print(f"📂 '{dosya_adi}' okunuyor ve derinlemesine analiz ediliyor...")
        df = pd.read_excel(dosya_adi)
        
        inme_df = df[df['stroke'] == 1]  
        
        
        full_analysis_results = {
            'n': len(df),
            'stroke_rate': round(df['stroke'].mean() * 100, 2),
            'age_inme': round(inme_df['age'].mean(), 1) if not inme_df.empty else 0,
            'gender_dist': inme_df['gender'].value_counts().to_dict() if not inme_df.empty else {},
            'bmi_inme': round(inme_df['bmi'].mean(), 1) if 'bmi' in df.columns and not inme_df.empty else "Bilinmiyor",
            'glucose_inme': round(inme_df['avg_glucose_level'].mean(), 1) if not inme_df.empty else 0,
            'ht_rate': round(inme_df['hypertension'].mean() * 100, 2) if not inme_df.empty else 0,
            'heart_rate': round(inme_df['heart_disease'].mean() * 100, 2) if not inme_df.empty else 0,
            'work_impact': inme_df['work_type'].value_counts().idxmax() if not inme_df.empty else "Bilinmiyor",
            'residence_impact': inme_df['Residence_type'].value_counts().to_dict() if not inme_df.empty else {},
            'marriage_impact': inme_df['ever_married'].value_counts().to_dict() if not inme_df.empty else {},
            'smoking_impact': inme_df['smoking_status'].value_counts().to_dict() if not inme_df.empty else {}
        }
        
        print("✅ Analiz tamamlandı, profesör raporu yazıyor...")
        
        # Şimdi ajanı çağırıyoruz
        rapor = run_agent(full_analysis_results)
        
        print("\n" + "="*60)
        print("🩺 KLİNİK KONSÜLTASYON RAPORU")
        print("="*60 + "\n")
        print(rapor)
        
    else:
        print(f" Hata: '{dosya_adi}' bulunamadı. Lütfen dosyanın main.py ile aynı yerde olduğundan emin olun.")

if __name__ == "__main__":
    main()