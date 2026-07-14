from rich import print

from app.client.client import CubeSandboxClient


client = CubeSandboxClient()

health = client.health()

print(health)