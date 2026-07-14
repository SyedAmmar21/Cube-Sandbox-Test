from __future__ import annotations

from typing import TYPE_CHECKING, Any
from app.client.models import CreateTemplateRequest
if TYPE_CHECKING:
    from app.client.client import CubeSandboxClient


class TemplatesClient:
    """
    Wrapper around the CubeSandbox Template API.
    """

    def __init__(self, client: CubeSandboxClient):
        self.client = client

    def list(self) -> list[dict[str, Any]]:
        return self.client.get("/templates")

    def get(self, template_id: str) -> dict[str, Any]:
        return self.client.get(f"/templates/{template_id}")

    def create(
        self,
        request: CreateTemplateRequest,
    ):
        return self.client.post(
            "/templates",
            json=request.model_dump(
                by_alias=True,
                exclude_none=True,
            ),
        )

    def delete(self, template_id: str):
        return self.client.delete(f"/templates/{template_id}")