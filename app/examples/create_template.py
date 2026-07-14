from app.client.client import CubeSandboxClient
from app.client.models import CreateTemplateRequest

client = CubeSandboxClient()

request = CreateTemplateRequest(
    image="ubuntu:24.04",
    writable_layer_size="1Gi",
)

response = client.templates.create(request)

print(response)