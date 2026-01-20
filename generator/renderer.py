import yaml
from pathlib import Path

TEMPLATE_DIR = Path("templates")

def render_yaml(resource_type, data):
    template_file = TEMPLATE_DIR / f"{resource_type}.yaml"

    with open(template_file) as f:
        template = yaml.safe_load(f)

    filled_yaml = fill_template(template, data)

    output_file = f"{resource_type}-{data['name']}.yaml"
    with open(output_file, "w") as f:
        yaml.dump(filled_yaml, f, sort_keys=False)

    print(f"\nYAML berhasil dibuat: {output_file}")

def fill_template(template, data):
    # Deployment
    if template["kind"] == "Deployment":
        template["metadata"]["name"] = data["name"]
        template["metadata"]["namespace"] = data["namespace"]
        template["spec"]["replicas"] = data["replicas"]
        template["spec"]["template"]["spec"]["containers"][0]["image"] = data["image"]
        template["spec"]["template"]["spec"]["containers"][0]["ports"][0]["containerPort"] = data["container_port"]

    # Service
    elif template["kind"] == "Service":
        template["metadata"]["name"] = data["name"]
        template["spec"]["type"] = data["type"]
        template["spec"]["ports"][0]["port"] = data["port"]
        template["spec"]["ports"][0]["targetPort"] = data["target_port"]

    # Pod
    elif template["kind"] == "Pod":
        template["metadata"]["name"] = data["name"]
        template["spec"]["containers"][0]["image"] = data["image"]

    return template
