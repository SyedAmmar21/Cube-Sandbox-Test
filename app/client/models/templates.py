from pydantic import BaseModel, Field


class CreateTemplateRequest(BaseModel):
    image: str

    writable_layer_size: str | None = Field(
        default=None,
        alias="writableLayerSize",
    )

    exposed_ports: list[int] | None = Field(
        default=None,
        alias="exposedPorts",
    )

    probe_port: int | None = Field(
        default=None,
        alias="probePort",
    )

    probe_path: str | None = Field(
        default=None,
        alias="probePath",
    )

    cpu: int | None = None
    memory: int | None = None

    env: list[str] | None = None

    allow_internet_access: bool | None = Field(
        default=None,
        alias="allowInternetAccess",
    )

    model_config = {
        "populate_by_name": True,
    }