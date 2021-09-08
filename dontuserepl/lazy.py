from .uptimerobot import UpTimeRobot
from .keep_alive import keep_alive
from .vars import slug, url

__all__ = (
    'lazy_setup',
)

def pprint(msg):
    prefix = '\033[96mlazy setup:'
    postfix = '\033[0m'
    print(prefix, msg, postfix)

def lazy_setup(uptimerobot_api_key: str):
    """Sets everything up"""
    api = UpTimeRobot(uptimerobot_api_key)
    pprint('Starting webserver...')
    keep_alive()
    pprint('Setting up UpTimeRobot monitor for this slug')
    created = api.sync_upsert_monitor(friendly_name=f'Bot:{slug}', url=url)
    pprint('New monitor set' if created else 'Monitor for this slug already existed.')
    pprint('Lazy Setup complete.')
