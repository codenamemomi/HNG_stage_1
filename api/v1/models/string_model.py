from datetime import datetime

class StringRecord:
    def __init__(self, value: str, properties: dict):
        self.id = properties["sha256_hash"]
        self.value = value
        self.properties = properties
        self.created_at = datetime.utcnow()
