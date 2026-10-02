class Service:
    def __init__(self):
        self.pending = []

    def run(self, value: str):
        self.pending.append(value)
        batch = self.pending[:8]
        self.pending = self.pending[8:]
        return {
            "batch_size": len(batch),
            "items": [item.upper() for item in batch],
            "flush_reason": "size_or_immediate_demo",
        }
