from app.client.client import CubeSandboxClient

client = CubeSandboxClient()

print(client.get("/health"))