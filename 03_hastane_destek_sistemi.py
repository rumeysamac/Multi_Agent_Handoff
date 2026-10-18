from dotenv import load_dotenv
import os
from agents import Agent, Runner

load_dotenv()

dahiliye_agent = Agent(
    name="dahiliye_uzmani",
    instructions="Dahiliye (İç Hastalıkları) ile ilgilen. Ateş, öksürük, tansiyon ve halsizlik durumlarında destek ver."
)

dis_hekimi_agent = Agent(
    name="dis_hekimi_uzmani",
    instructions="Diş sağlığı, dolgu, diş çekimi ve ağız/çene ağrıları konusunda yardımcı ol."
)

goz_agent = Agent(
    name="goz_uzmani",
    instructions="Göz sağlığı, bulanık görme, katarakt ve göz muayeneleri konularında bilgi ver."
)


danisma_agent = Agent(
    name="hastane_danismani",
    instructions=(
        "Hastanın şikayetini analiz et. "
        "Ateş, öksürük veya dahili şikayetler için dahiliye_uzmani'na, "
        "Diş ve ağız ağrıları için dis_hekimi_uzmani'na, "
        "Göz problemleri için goz_uzmani'na yönlendir."
    ),
    handoffs=[dahiliye_agent, dis_hekimi_agent, goz_agent]
)


def hastane_talebini_islemle(sikayet: str):
    print(f"\n--- Gelen Hasta Şikayeti: '{sikayet}' ---")
    
   
    result = Runner.run_sync(danisma_agent, sikayet)
    
    
    print(f"[LOG] Devralan Poliklinik/Agent: ---> {result.last_agent.name} <---")
    print(f"Cevap: {result.final_output}")


hastane_talebini_islemle("Dün geceden beri sağ azı dişim zonkluyor.")
hastane_talebini_islemle("Tansiyonum 16'ya çıktı, başım çok dönüyor.")
hastane_talebini_islemle("Bilgisayara bakarken gözlerim çok sulanıyor ve batıyor.")