from __future__ import annotations

from typing import TYPE_CHECKING, Any

from app.client.models import (
    CreateSandboxRequest,
    SandboxResponse,
)

if TYPE_CHECKING:
    from app.client.client import CubeSandboxClient


class SandboxesClient:
    """
    Wrapper around the CubeSandbox Sandbox API.
    """

    def __init__(self, client: CubeSandboxClient):
        self.client = client

    def create(
        self,
        request: CreateSandboxRequest,
    ) -> SandboxResponse:

        response = self.client.post(
            "/sandboxes",
            json=request.model_dump(
                by_alias=True,
                exclude_none=True,
            ),
        )

        return SandboxResponse.model_validate(response["data"])
    
    def get(
        self,
        sandbox_id: str,
    ) -> SandboxResponse:

        response = self.client.get(
            f"/sandboxes/{sandbox_id}"
        )

        return SandboxResponse.model_validate(response)

    def list(self) -> list[SandboxResponse]:
        sandboxes_data = self.client.get("/sandboxes")
        return [SandboxResponse.model_validate(sandbox) for sandbox in sandboxes_data]

    def delete(
        self,
        sandbox_id: str,
    ):
        return self.client.delete(
            f"/sandboxes/{sandbox_id}",
        )