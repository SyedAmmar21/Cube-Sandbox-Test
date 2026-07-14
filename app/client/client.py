from __future__ import annotations

from typing import Any

import requests
from app.client.templates import TemplatesClient

class CubeSandboxClient:
    """
    Base HTTP client for the CubeSandbox REST API.
    """

    def __init__(
        self,
        base_url: str = "http://127.0.0.1:13000",
        timeout: int = 30,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        self.session = requests.Session()

        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )
        self.templates = TemplatesClient(self)

    def get(self, endpoint: str, **kwargs) -> Any:
        response = self.session.get(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs,
        )

        response.raise_for_status()

        if response.content:
            return response.json()

        return None

    def post(self, endpoint: str, **kwargs):
        response = self.session.post(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs,
        )

        if not response.ok:
            print(f"Status: {response.status_code}")
            print(response.text)

        response.raise_for_status()

        return {
            "status_code": response.status_code,
            "data": response.json() if response.content else None,
        }

    def delete(self, endpoint: str, **kwargs) -> Any:
        response = self.session.delete(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs,
        )

        response.raise_for_status()

        if response.content:
            return response.json()

        return None