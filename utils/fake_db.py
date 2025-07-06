import asyncio

class FakeDatabase:
    def __init__(self):
        self.connected = False

    async def connect(self):
        await asyncio.sleep(1)
        self.connected = True
        print("✅ Подключено к фейковой базе данных")

    async def disconnect(self):
        await asyncio.sleep(1)
        self.connected = False
        print("🛑 Отключено от фейковой базы данных")

async def connect(self):
    print("🔥 FakeDatabase.connect() called")
    self.connected = True

async def disconnect(self):
    print("🧊 FakeDatabase.disconnect() called")
    self.connected = False