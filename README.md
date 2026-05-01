# 📊 CV Interactif — Débora Mandon

Application Streamlit déployée sur Streamlit Community Cloud : CV dynamique, formulaire de contact et démo de monitoring pipeline.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cv-debora-mandon.streamlit.app)

---

## 🗂️ Structure

```
├── app.py              # Point d'entrée, navigation multi-pages
├── page0.py            # Accueil
├── page1.py            # Profil
├── page2.py            # Expériences
├── page3.py            # Projets
├── page4.py            # Contact (formulaire + admin)
├── page5.py            # Démo monitoring pipeline
├── assets/             # Photo, CV PDF
├── requirements.txt
└── .github/workflows/  # Keep-alive GitHub Actions
```

## 🛠️ Stack

- **Frontend** : Streamlit 1.57
- **Stockage local** : SQLite (messages de contact, logs de démo)
- **Visualisation** : Plotly, Altair
- **CI** : GitHub Actions (keep-alive)

## 🚀 Lancer en local

```bash
# 1. Cloner le repo
git clone https://github.com/DeboraMandon/cv-debora-mandon-streamlit.git
cd cv-debora-mandon-streamlit

# 2. Environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Windows : .venv\Scripts\activate

# 3. Dépendances
pip install -r requirements.txt

# 4. Secrets (mot de passe admin)
mkdir -p .streamlit
cp secrets.toml.template .streamlit/secrets.toml
# → Éditer .streamlit/secrets.toml avec ton mot de passe

# 5. Lancer
streamlit run app.py
```

## 🔐 Configuration des secrets

Le mot de passe de la section admin est géré via **Streamlit Secrets** (jamais en dur dans le code).

**En local** : éditer `.streamlit/secrets.toml` (ignoré par git) :
```toml
[admin]
password = "ton_mot_de_passe"
```

**Sur Streamlit Community Cloud** : Settings → Secrets → coller le même contenu.

## 📦 Déploiement

Le projet est déployé automatiquement sur Streamlit Community Cloud à chaque push sur `main`.  
Un workflow GitHub Actions maintient l'app active (keep-alive).
