from dotenv import load_dotenv
import os
from agents import Agent, Runner

load_dotenv()

dahiliye_agent = Agent(
    name="dahiliye_uzmani",
    instructions="Dahiliye (İç Hastalıkları) polikliniği ile ilgilen. Ateş, öksürük, halsizlik, şeker ve tansiyon şikayetlerinde yardımcı ol."
)

danisma_agent = Agent(
    name="hastane_danismani",
    instructions="Hastanın şikayetini dinle. Dahiliye ile ilgiliyse dahiliye_uzmani'na yönlendir.",
    handoffs=[dahiliye_agent]
)

result = Runner.run_sync(
    danisma_agent,
    "İki gündür yüksek ateşim var ve öksürüyorum."
)

print("Cevap:", result.final_output)
print(f"Cevabı Veren Agent: {result.last_agent.name}")