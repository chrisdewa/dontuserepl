import aiohttp
from aiolimiter import AsyncLimiter
import asyncio
from .monitor import Monitor

__all__ = (
    'UpTimeRobot',
)

api_version = 'v2'

base_url = f'https://api.uptimerobot.com/{api_version}/'

class UpTimeRobot:
    api_key: str
    max_rate: int

    def __init__(self, api_key, max_rate = 10): 
        self.key = api_key
        self.base_payload = f'api_key={api_key}&format=json'
        self.limiter = AsyncLimiter(max_rate=max_rate)
        self.headers = headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        }
    
    async def get_monitors(self):
        """Returns the monitors set for this account"""
        payload = base_url + 'getMonitors?' + self.base_payload
        async with self.limiter:
            async with aiohttp.ClientSession(headers=self.headers) as cs:
                async with cs.post(payload) as r:
                    data = await r.json()
        if r.status == 200:
            return [Monitor(m) for m in data.get('monitors',[])]
        else:
            raise Exception(f'Something went wrong: {data}')
    
    async def new_monitor(self, friendly_name: str, url: str):
        """Configures a new monitor"""
        post_url = base_url+'newMonitor'
        payload = {
            'api_key': self.key,
            'format': 'json',
            'type': '1',
            'friendly_name': friendly_name,
            'url': url
        }
        async with self.limiter:
            async with aiohttp.ClientSession(headers=self.headers) as cs:
                async with cs.post(post_url, data=payload) as r:
                    data = await r.json()
        if data['stat'] != 'ok':
            raise Exception(f'Something went wrong |[{r.status}] data:{data}')
    
    async def upsert_monitor(self, friendly_name: str, url: str):
        monitors = await self.get_monitors()
        if not any(
            monitor for monitor in monitors
            if monitor.name == friendly_name or monitor.url == url
        ):
            await self.new_monitor(friendly_name, url)
    
    def sync_upsert_monitor(self, friendly_name: str, url: str):
        asyncio.get_event_loop().run_until_complete(self.upsert_monitor(friendly_name, url))
    
    def sync_get_monitors(self):
        return asyncio.get_event_loop().run_until_complete(self.get_monitors())
