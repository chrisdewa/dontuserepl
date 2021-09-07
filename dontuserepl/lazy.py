from .uptimerobot import UpTimeRobot
from .keep_alive import keep_alive
from .vars import slug, url

__all__ = (
    'lazy_setup',
)

def lazy_setup(uptimerobot_api_key: str):
    """Sets everything up"""
    prefix = '\033[96mlazy setup:'
    postfix = '\033[0m'
    api = UpTimeRobot(uptimerobot_api_key)
    print(prefix, 'Starting webserver...',postfix)
    keep_alive()
    print(prefix, 'Setting up UpTimeRobot monitor for this slug',postfix)
    api.sync_upsert_monitor(friendly_name=f'Bot:{slug}', url=url)
    print(prefix, 'Lazy Setup complete.', postfix)
