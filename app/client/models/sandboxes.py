from pydantic import BaseModel, Field


class CreateSandboxRequest(BaseModel):
    template_id: str = Field(
        alias="templateID",
    )

    timeout: int = 300

    auto_pause: bool = Field(
        default=False,
        alias="autoPause",
    )

    allow_internet_access: bool = Field(
        default=True,
        alias="allow_internet_access",
    )

    model_config = {
        "populate_by_name": True,
    }


class SandboxResponse(BaseModel):
    template_id: str = Field(alias="templateID")
    sandbox_id: str = Field(alias="sandboxID")
    client_id: str = Field(alias="clientID")
    envd_version: str = Field(alias="envdVersion")

    domain: str | None = None

    model_config = {
        "populate_by_name": True,
    }