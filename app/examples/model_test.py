from app.client.models import CreateTemplateRequest

request = CreateTemplateRequest(
    image="ubuntu:24.04",
    cpu=2000,
    memory=2048,
)

print(request)

print()

print(
    request.model_dump(
        by_alias=True,
        exclude_none=True,
    )
)