import os

__all__ = (
    'url',
    'owner',
    'slug'
)

slug = os.getenv("REPL_SLUG")
owner = os.getenv('REPL_OWNER')
url = f'https://{slug}.{owner}.repl.co'
