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
### Inisialisasi Git pada Folder
```bash
git init

### Inisialisasi Git pada Folder
```bash
git pull https://github.com/rizkyudhap/deployman.git

### Beri Permission pada file
```bash
chmod +x ./start.sh

### Jalankan Program
```bash
./start.sh

pip install -r requirements.txt
python main.py
