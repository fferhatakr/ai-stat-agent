def run_agent(llm, analysis_results, user_question): 

    
    prompt = f"""
    Sen uzman bir veri analistisin. Elinde şu analiz sonuçları var:
    
    {analysis_results}

    Kullanıcı sana şu soruyu sordu: "{user_question}"

    Kurallar:
    - SADECE yukarıdaki verilere dayanarak cevap ver.
    - Bilmediğin veya veride olmayan bir şey sorulursa "Verilerde bu bilgi yok" de.
    - Cevabın net ve kısa olsun.
    """

    response = llm.invoke(prompt)
    return response