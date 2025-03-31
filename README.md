# Détecteur d’objets IA – Streamlit + YOLOv8

Cette application détecte automatiquement les objets dans une image grâce à un modèle **pré-entraîné YOLOv8**.

- Image chargée par l’utilisateur
- Analyse par le modèle Ultralytics
- Image annotée affichée dans l’interface

---

## ▶DÉMO EN LIGNE (Streamlit Cloud)

À venir : https://ton-utilisateur.streamlit.app

---

## TECH STACK

- Streamlit
- Ultralytics YOLOv8
- GitHub Actions (CI)
- Python 3.10

---

##  GUIDE D’INSTALLATION

### 1. En local

```bash
git clone https://github.com/TonUtilisateur/object-detector-streamlit.git
cd object-detector-streamlit
chmod +x deploy_local.sh
./deploy_local.sh
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