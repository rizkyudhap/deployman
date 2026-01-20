import questionary

def main_menu():
    resource_type = questionary.select(
        "Mau generate resource apa?",
        choices=["Deployment", "Service", "Pod"]
    ).ask()

    answers = {}

    if resource_type == "Deployment":
        answers["name"] = questionary.text("Nama deployment:").ask()
        answers["namespace"] = questionary.text(
            "Namespace:",
            default="default"
        ).ask()
        answers["replicas"] = int(questionary.text(
            "Jumlah replicas:",
            default="1"
        ).ask())
        answers["image"] = questionary.text("Docker image:").ask()
        answers["container_port"] = int(questionary.text(
            "Container port:",
            default="80"
        ).ask())

    elif resource_type == "Service":
        answers["name"] = questionary.text("Nama service:").ask()
        answers["type"] = questionary.select(
            "Service type:",
            choices=["ClusterIP", "NodePort"]
        ).ask()
        answers["port"] = int(questionary.text("Service port:").ask())
        answers["target_port"] = int(questionary.text("Target port:").ask())

    elif resource_type == "Pod":
        answers["name"] = questionary.text("Nama pod:").ask()
        answers["image"] = questionary.text("Docker image:").ask()

    return resource_type.lower(), answers
