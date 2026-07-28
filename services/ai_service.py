from google import genai
from config.settings import settings

class AIService:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.system_prompt = (
            "You are NexapTrade AI, an expert trading assistant specializing in Cryptocurrency, "
            "Forex, and Technical Analysis. Respond concisely, professionally, using bold Markdown formatting. "
            "Never offer guaranteed profit claims. Always adhere to risk management principles."
        )

    async def ask_assistant(self, user_query: str) -> str:
        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"{self.system_prompt}\n\nUser Question: {user_query}"
            )
            disclaimer = "\n\n⚠️ *Disclaimer: Not financial advice. Trading involves substantial risk.*"
            return response.text + disclaimer
        except Exception as e:
            return f"❌ AI Assistant service currently unavailable: {str(e)}"

ai_service = AIService()
