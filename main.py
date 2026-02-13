from analysis.simple_analysis import simple_analysis
from src.tools import load_data
from src.config import get_llm
from src.agent_core import run_agent

def main():
    print("--- AI İstatistik Asistanı Başlatılıyor ---")

    try:
        df = load_data("data/inme.xlsx")
        print("✅ Veri başarıyla yüklendi.")
    except Exception as e:
        print(f"❌ Hata: {e}")
        return

    analysis_results = simple_analysis(df)

    llm = get_llm()

    while True:
        print("\n------------------------------------------------")
        user_question = input("❓ Sorunuzu yazın (Çıkmak için 'q' basın): ")

        if user_question.lower() == 'q':
            print("Çıkış yapılıyor...")
            break
        
        print("🤖 Düşünüyor...")
        
        response = run_agent(llm, analysis_results, user_question)

        print(f"\n💡 CEVAP:\n{response.content}")

if __name__ == "__main__":
    main()