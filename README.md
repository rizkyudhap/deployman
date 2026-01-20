# Kubernetes YAML Generator (CLI)

Program CLI untuk menghasilkan file YAML Kubernetes secara otomatis
(Deployment, Service, dan Pod) berdasarkan input user.

## Fitur
- Generate Deployment YAML
- Generate Service YAML
- Generate Pod YAML
- Validasi input dasar
- Output siap digunakan dengan `kubectl apply -f`

## Cara Menjalankan
```bash
python3 -m venv venv
source venv/bin/activate

### Windows (Git Bash)
source venv/Scripts/activate

pip install -r requirements.txt
python main.py
