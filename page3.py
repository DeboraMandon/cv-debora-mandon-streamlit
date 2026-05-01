import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.project-card {
    border: 1px solid #e0e0e0;
    padding: 20px;
    border-radius: 12px;
    background: #fafafa;
    transition: 0.2s ease;
    margin-bottom: 25px;
}
.project-card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 4px 12px rgba(0,0,0,0.12);
}
.project-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #403EBB;
    margin-bottom: 3px;
}
.project-sub {
    font-size: 1rem;
    margin-bottom: 12px;
    color: #555;
}
.project-desc {
    font-size: 0.95rem;
    line-height: 1.6;
}
.tag {
    display: inline-block;
    background: #e8f0ff;
    color: #2a4fb4;
    padding: 5px 10px;
    margin: 4px 5px 0 0;
    border-radius: 8px;
    font-size: 0.8rem;
    font-weight: 600;
}
.tag-green {
    background: #e8f5e9;
    color: #1b5e20;
}
@media (prefers-color-scheme: dark) {
    .project-card { background: #1e1e1e !important; border-color: #444 !important; }
    .project-desc { color: #e0e0e0 !important; }
    .tag { background: #2a4fb4 !important; color: white !important; }
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}
.project-card { animation: fadeInUp 0.6s ease forwards; }
a[data-testid="stPageLink"] {
    text-align: center !important;
    justify-content: center !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>Projets</h1>", unsafe_allow_html=True)
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# PROJET 1 — Pipeline temps réel Azure
# ---------------------------------------------------------------

st.markdown("""
<div class='project-card'>
    <p class='project-title'>Pipeline de collecte et traitement temps réel</p>
    <p class='project-sub'>Azure Stream Analytics · Logic Apps · PostgreSQL · JSON Events</p>
    <p class='project-desc'>
        Mise en place d'une chaîne Cloud complète permettant la collecte, le traitement
        et l'ingestion d'événements en temps réel dans PostgreSQL.<br><br>
        <strong>Le pipeline inclut :</strong><br>
        • Ingestion via Logic Apps<br>
        • Transformation dans Stream Analytics<br>
        • Routage dynamique vers APIs<br>
        • Monitoring et alertes automatisées
    </p>
""", unsafe_allow_html=True)

for t in ["Azure", "Stream Analytics", "Logic Apps", "PostgreSQL", "JSON", "Monitoring"]:
    st.markdown(f"<span class='tag'>{t}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# PROJET 2 — Node-RED / FlowFuse
# ---------------------------------------------------------------

st.markdown("""
<div class='project-card'>
    <p class='project-title'>Automatisation de flux via Node-RED / FlowFuse</p>
    <p class='project-sub'>API Graph · Flows automatisés · SharePoint · Intégration fichiers</p>
    <p class='project-desc'>
        Conception de flux automatisés pour récupérer, transformer et déposer des fichiers
        provenant de SharePoint via l'API Graph Microsoft.<br><br>
        Déclencheurs programmés, gestion d'erreurs, logs centralisés
        et mécanismes de reprise automatique pour garantir la fiabilité des échanges.
    </p>
""", unsafe_allow_html=True)

for t in ["FlowFuse", "Node-RED", "API Graph", "Automatisation", "SharePoint", "Intégration"]:
    st.markdown(f"<span class='tag'>{t}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# PROJET 3 — Dashboards BI
# ---------------------------------------------------------------

st.markdown("""
<div class='project-card'>
    <p class='project-title'>Modélisation & Dataviz — Tableaux de bord BI</p>
    <p class='project-sub'>Power BI · Qlik · Modélisation DWH · KPI métiers</p>
    <p class='project-desc'>
        Construction de modèles de données optimisés et dashboards visuels
        pour différents métiers : opérations, finance, support client.<br><br>
        Travail sur la définition des indicateurs, la mise en qualité des données,
        l'UX des visuels, la publication et la gestion des droits.
    </p>
""", unsafe_allow_html=True)

for t in ["Power BI", "Qlik", "DAX", "Modélisation", "KPI", "Dataviz"]:
    st.markdown(f"<span class='tag'>{t}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# PROJET 4 — Retail Pipeline ELT (Olist) — PORTFOLIO
# ---------------------------------------------------------------

st.markdown("""
<div class='project-card'>
    <p class='project-title'>Retail Pipeline ELT — Olist Brazil E-Commerce</p>
    <p class='project-sub'>Projet portfolio · Python · PostgreSQL · dbt · Airflow · scikit-learn · Prophet</p>
    <p class='project-desc'>
        Pipeline ELT end-to-end sur le dataset Olist Brazil (99 441 commandes, Kaggle).<br><br>
        <strong>Architecture Medallion :</strong><br>
        • <strong>Ingestion</strong> — Python + API Kaggle → PostgreSQL (schéma raw)<br>
        • <strong>Transformation</strong> — dbt (staging → marts)<br>
        • <strong>Orchestration</strong> — Airflow 2.9<br>
        • <strong>ML</strong> — Prophet (prévisions revenue) · scikit-learn (scoring satisfaction client)<br>
        • <strong>Dataviz</strong> — Metabase<br><br>
        La page <em>Démo Monitoring</em> de cette application présente les résultats
        d'analyse pipeline issus de ce dataset.
    </p>
""", unsafe_allow_html=True)

for t in ["Python", "PostgreSQL", "dbt", "Airflow", "scikit-learn", "Prophet", "Metabase", "ELT", "Medallion"]:
    css = "tag tag-green" if t in ["dbt", "Airflow", "Prophet"] else "tag"
    st.markdown(f"<span class='{css}'>{t}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# PROJET 5 — CV Streamlit (ce projet)
# ---------------------------------------------------------------

st.markdown("""
<div class='project-card'>
    <p class='project-title'>CV Interactif — Application Streamlit</p>
    <p class='project-sub'>Streamlit · Python · SQLite · GitHub Actions · Streamlit Community Cloud</p>
    <p class='project-desc'>
        Cette application elle-même — CV dynamique déployé sur Streamlit Community Cloud.<br><br>
        • Multi-pages avec navigation Streamlit native<br>
        • Formulaire de contact avec stockage SQLite et espace admin sécurisé<br>
        • Démo monitoring pipeline avec données réelles (Olist)<br>
        • Keep-alive via GitHub Actions<br>
        • Secrets gérés via Streamlit Secrets (aucune donnée sensible dans le code)
    </p>
""", unsafe_allow_html=True)

col_tags, col_link = st.columns([3, 1])
with col_tags:
    for t in ["Streamlit", "Python", "SQLite", "GitHub Actions", "CI/CD"]:
        st.markdown(f"<span class='tag'>{t}</span>", unsafe_allow_html=True)
with col_link:
    st.markdown(
        "<a href='https://github.com/DeboraMandon/cv-debora-mandon-streamlit' target='_blank'>"
        "💻 Voir le repo</a>",
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------------

btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("⬅️ Revenir aux Expériences 🎉", use_container_width=True):
        st.switch_page("page2.py")

with btn_col2:
    if st.button("📲 Aller au Contact ➡️", use_container_width=True):
        st.switch_page("page4.py")

left, center, right = st.columns([7, 2, 7])
with center:
    st.page_link("page0.py", label="🏠 Accueil", use_container_width=True)
