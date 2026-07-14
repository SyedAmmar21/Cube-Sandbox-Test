from app.client.client import CubeSandboxClient
from app.client.models import CreateSandboxRequest

client = CubeSandboxClient()

request = CreateSandboxRequest(
    template_id="tpl-76fe1a3e44bd4fdb8696838f",
    timeout=300,
    auto_pause=False,
)

sandbox = client.sandboxes.create(request)

print(sandbox)