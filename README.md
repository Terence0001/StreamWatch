# StreamWatch

### Projet de surveillance vidéo boosté à l'IA

Il utilisera le framework [streamlit](https://streamlit.io/) et un modèle IA [YOLOv8](https://ultralytics.com/yolov8)

---

### Créer un fichier gitignore à la racine du projet avec le nom suivant

```sh
.gitignore
```

---

### Puis y ajouter le contenu suivant

```sh
runs/
*.pt
.venv/
```

### Créer un environnement virtuel

```sh
python -m venv .venv
```

### Activer l'environnement virtuel

```sh
.venv\Scripts\activate.bat
```

### Désactiver l'environnement virtuel (Si besoin)

```sh
deactivate
```

### Commande pour lancer le serveur Streamlit

```sh
streamlit run picture_pred.py
```

### Commande pour arrêter le serveur Streamlit

```sh
ctrl + c
```

---
