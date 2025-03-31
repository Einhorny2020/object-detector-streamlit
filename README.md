# Détecteur d’objets IA – Streamlit + YOLOv8

Cette application détecte automatiquement les objets dans une image grâce à un modèle **pré-entraîné YOLOv8**.

- Image chargée par l’utilisateur
- Analyse par le modèle Ultralytics
- Image annotée affichée dans l’interface
- http://localhost:8501
---

## TECH STACK

- Ultralytics YOLOv8
- GitHub Actions (CI)
- Python 3.10

---

##  GUIDE D’INSTALLATION

### 1.a En local linux ou mac

```bash
cd object-detector-streamlit
chmod +x deploy_local.sh
./deploy_local.sh
```

### 1.b En local windows
```bash
python -m venv venv
venv\\Scripts\\activate
pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```
### 2. Sur GitHub

1. Crée un dépôt `object-detector-streamlit`
2. Pousse le contenu avec :

```bash
git init
git add .
git commit -m "🎯 Détecteur d’objets Streamlit"
git branch -M main
git remote add origin https://github.com/TonUtilisateur/object-detector-streamlit.git
git push -u origin main
```

### 3. Sur Streamlit Cloud

- Attention sur streamlit : Dans le code on utilise "from ultralytics import YOLO",Or, Ultralytics/YOLOv8 télécharge automatiquement un modèle (yolov8n.pt) au premier lancement, ce que Streamlit Cloud n’autorise pas directement (pas d’écriture disque autorisée à certains endroits, ni de heavy download dynamique).

Une solution rapide serait de : changer l’approche IA pour un modèle d’analyse de contenu image léger et cloud-friendly (comme imageai, torchvision, transformers, ou même OpenAI/CLIP si besoin d’alternatives cloud safe).

Simplement pour le projet je prefere le laisser en local pour bien comprendre le fonctionnement

Si vous opter pour la solution rapide voici les étapes à suivre aprés la modification du code : 

- Va sur https://streamlit.io/cloud
- Clique sur “New app”
- Sélectionne ton repo
- Branche : `main`
- Fichier : `app.py`
- Clique sur “Deploy”

---

## PIPELINE CI/CD

- `flake8` : vérifie la structure du code
- `pytest` : lance les tests unitaires
- Automatique à chaque `push` ou `pull_request`