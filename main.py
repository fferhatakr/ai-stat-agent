import os
import warnings
from src.agent_builder import build_agent

warnings.filterwarnings("ignore")

def main():
    dosya_adi = "inme.xlsx"
    excel_path = os.path.join("data", dosya_adi)
    
    print(f"\n--- Veri Analiz Asistanı Başlatılıyor ({dosya_adi}) ---")
    
    try:
        print("Sistem hazırlanıyor, lütfen bekleyin...")
        my_agent = build_agent(excel_path)
        print("✅ Hazır! Sorularınızı yazabilirsiniz. (Çıkış için 'q' yazın)\n")
        
        while True:
            user_input = input("Siz: ")
            if user_input.lower() in ['q', 'exit', 'cikis']:
                print("Görüşürüz, mesleki hayatında başarılar! 👋")
                break
            
            if not user_input.strip():
                continue

            print("\nYapay Zeka Sizin İçin Düşünüyor...")
            
            try:
                response = my_agent.invoke(user_input)
                
                print(f"\nKişisel Yapay Zeka: {response['output']}\n")
                print("-" * 30)
                
            except Exception as e:
                print(f"\n❌ Bir hata oluştu: {e}\n")
            
    except Exception as e:
        print(f"Başlatma Hatası: {e}")

if __name__ == "__main__":
    main()