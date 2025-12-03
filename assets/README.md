# CV interactif – Débora Mandon

Application web Streamlit présentant mon CV interactif, mon parcours et une démo de monitoring de pipelines data.

## 🎯 Objectif

Proposer un CV moderne, interactif et déployé en ligne, mettant en avant :
- Data Engineering & BI (Azure, ETL, Power BI, Qlik, Node-RED…)
- Communication & branding
- Mise en place de dashboards et monitoring de flux de données

## 🧱 Structure de l’application

L’application est une app Streamlit multipage :

- `app.py` : point d’entrée, navigation entre les pages
- `page0.py` : Accueil
- `page1.py` : Profil
- `page2.py` : Expériences professionnelles
- `page3.py` : Projets (pipelines, automatisations, BI)
- `page4.py` : Contact (formulaire)
- `page5.py` : Démo *Pipeline Monitoring Live* (SQLite + dashboards)
- `assets/` : photo, CV PDF, autres ressources statiques
- `pipelines.db` / `contact.db` (optionnel) : bases SQLite utilisées par la démo

## 🚀 Lancer l’app en local

Cloner le dépôt
git clone https://github.com/<TON_USER>/<TON_REPO>.git
cd <TON_REPO>

Créer l’environnement (optionnel mais recommandé)
python -m venv .venv
source .venv/bin/activate # Linux/Mac

ou
.venv\Scripts\activate # Windows

Installer les dépendances
pip install -r requirements.txt

Lancer Streamlit
streamlit run app.py


L’app est ensuite accessible sur `http://localhost:8501`.

## 🗄️ Données & bases SQLite

La page **Démo / Pipeline Monitoring Live** utilise une base SQLite (`pipelines.db`) pour simuler :
- les runs de différents pipelines (Azure Stream Analytics, Node-RED/FlowFuse, Talend…)
- le suivi du statut, des durées, et du volume de données traitées

À chaque lancement, si la base est vide, des données d’exemple sont automatiquement insérées.

## ☁️ Déploiement

L’application est pensée pour être déployée sur **Streamlit Community Cloud** :

1. Pousser ce dépôt sur GitHub
2. Créer une nouvelle app sur https://share.streamlit.io
3. Sélectionner :
   - Repository : `<TON_USER>/<TON_REPO>`
   - Branch : `main`
   - Main file : `app.py`
4. Déployer

Les bases SQLite peuvent être recréées automatiquement au démarrage.

## 📬 Contact

- LinkedIn : https://www.linkedin.com/in/débora-mandon  
- GitHub : https://github.com/DeboraMandon  
- Email : debora.mandon@mail.com

Tu peux ajuster les noms de fichiers si besoin.




