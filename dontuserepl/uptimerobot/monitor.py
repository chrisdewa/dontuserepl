
__all__ = (
    'Monitor',
)

class Monitor:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('friendly_name')
        self.url = data.get('url')
    
    def __repr__(self) -> str:
        return f'Monitor(name={self.name}, url={self.url})'

    def __str__(self) -> str:
        return 'monitor: ' + self.name



