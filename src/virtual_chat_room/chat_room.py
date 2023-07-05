```python
import asyncio
from aiohttp import web
from src.openai_integration import generateResponse

class ChatRoom:
    def __init__(self):
        self.users = {}  # To store active users

    async def handle_message(self, request):
        data = await request.json()
        user_id = data['user_id']
        message = data['message']

        # Generate response using OpenAI Integration
        response = generateResponse(message)

        # Send response back to user
        self.users[user_id].send(response)

        return web.Response()

    async def handle_connect(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        user_id = request.match_info['user_id']
        self.users[user_id] = ws

        async for msg in ws:
            if msg.type == web.WSMsgType.text:
                await self.handle_message({'user_id': user_id, 'message': msg.data})
            elif msg.type == web.WSMsgType.error:
                print('ws connection closed with exception %s' % ws.exception())

        print('websocket connection closed')
        del self.users[user_id]
        return ws

    def setup_routes(self, app):
        app.router.add_route('GET', '/connect/{user_id}', self.handle_connect)

    def start(self):
        app = web.Application()
        self.setup_routes(app)
        web.run_app(app)

if __name__ == "__main__":
    chat_room = ChatRoom()
    chat_room.start()
```