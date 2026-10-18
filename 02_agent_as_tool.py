from dotenv import load_dotenv
import os
from agents import Agent, Runner

load_dotenv()

recete_agent = Agent(
    name="recete_sorgulayi_agent",
    instructions="Verilen T.C. Kimlik No veya Reçete Kodu ile tanımlı reçete ve ilaç bilgilerini sorgular ve açıklar."
)


danisma_agent = Agent(
    name="hastane_asistani",
    instructions=(
        "Hastaya hastane hizmetleri ve randevular konusunda yardımcı ol. "
        "Hasta reçetesini veya ilaçlarını sorduysa 'recete_sorgula' aracını kullanarak sorgulat "
        "ve sonucu hastaya kibarca ilet."
    ),
    tools=[
        recete_agent.as_tool(
            tool_name="recete_sorgula",
            tool_description="Hastanın reçete kodunu veya T.C. kimlik numarasını alarak kayıtlı ilaçlarını sorgular."
        )
    ]
)


print("--- Agent-as-Tool Testi Başlıyor ---")
result = Runner.run_sync(
    danisma_agent,
    "Reçete kodum REC12345. Reçetemdeki ilaçları öğrenebilir miyim?"
)

print("Cevap:", result.final_output)
print(f"Konuşmayı Bitiren Agent (Kontrol Kimde?): {result.last_agent.name}")