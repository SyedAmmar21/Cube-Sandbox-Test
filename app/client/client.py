import requests

from app.config import CUBESANDBOX_URL


class CubeSandboxClient:
    def __init__(self, base_url: str = CUBESANDBOX_URL):
        self.base_url = base_url.rstrip("/")

    def health(self):
        response = requests.get(
            f"{self.base_url}/health",
            timeout=30,
        )

        response.raise_for_status()

        return response.json()