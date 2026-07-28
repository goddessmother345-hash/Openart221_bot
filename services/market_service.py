import aiohttp
from typing import Dict, Any, Optional

class MarketService:
    COINGECKO_BASE = "https://api.coingecko.com/api/v3"
    ALTERNATIVE_ME = "https://api.alternative.me/fng/"
    FRANKFURTER_BASE = "https://api.frankfurter.app"

    @staticmethod
    async def get_crypto_prices(ids: str = "bitcoin,ethereum,solana,ripple,binancecoin,cardano,dogecoin,the-open-network") -> Optional[Dict[str, Any]]:
        url = f"{MarketService.COINGECKO_BASE}/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    return await resp.json()
        return None

    @staticmethod
    async def get_forex_rates(base: str = "USD") -> Optional[Dict[str, Any]]:
        url = f"{MarketService.FRANKFURTER_BASE}/latest?from={base}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    return await resp.json()
        return None

    @staticmethod
    async def get_fear_and_greed() -> Optional[Dict[str, Any]]:
        async with aiohttp.ClientSession() as session:
            async with session.get(MarketService.ALTERNATIVE_ME) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data["data"][0] if "data" in data else None
        return None
