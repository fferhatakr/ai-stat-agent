from src.config import get_llm
from src.tools import get_excel_agent

# Bu fonksiyon, diğer dosyalardaki parçaları bir araya getiriyor
def build_agent(excel_file_path):
    
    llm = get_llm()
    agent = get_excel_agent(llm, excel_file_path)
    
    
    if agent is None:
        raise Exception("Hata: Ajan kurulamadı. Lütfen Veri dosyasının yolunu kontrol edin.")
    return agent