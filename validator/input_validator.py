import re


def validate_name(name):
    pattern = r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$"
    if not re.match(pattern, name):
        raise ValueError(
            f"Nama '{name}' tidak valid untuk Kubernetes resource"
        )


def validate_inputs(resource_type, data):
    validate_name(data["name"])

    if resource_type == "deployment":
        if data["replicas"] < 1:
            raise ValueError("Replicas harus >= 1")

    if resource_type == "service":
        if data["port"] <= 0 or data["target_port"] <= 0:
            raise ValueError("Port harus > 0")
