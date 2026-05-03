import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.project-card {
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 20px 24px;
    background: #fafafa;
    margin-bottom: 20px;
    transition: 0.2s ease;
}
.project-card:hover {
    transform: translateY(-3px);
    box-shadow: 0px 4px 14px rgba(0,0,0,0.10);
}
.project-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #403EBB;
    margin: 0 0 2px 0;
}
.project-sub {
    font-size: 0.82rem;
    color: #888;
    margin: 0 0 12px 0;
}
.project-desc {
    font-size: 0.88rem;
    line-height: 1.6;
    margin: 0 0 12px 0;
}
.tag {
    display: inline-block;
    background: #e8f0ff;
    color: #2a4fb4;
    padding: 3px 10px;
    margin: 3px 4px 0 0;
    border-radius: 6px;
    font-size: 0.76rem;
    font-weight: 600;
}
.tag-green {
    background: #e8f5e9;
    color: #1b5e20;
}
@media (prefers-color-scheme: dark) {
    .project-card  { background: #1e1e1e !important; border-color: #333 !important; }
    .project-desc  { color: #ccc !important; }
    .project-sub   { color: #666 !important; }
    .tag           { background: #1a2a4a !important; color: #a0b4ff !important; }
    .tag-green     { background: #1a2a1a !important; color: #80c080 !important; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>Projets</h1>", unsafe_allow_html=True)
st.markdown("<div style='height:24px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# helper : rendu d'une card projet
# ---------------------------------------------------------------

def project_card(title, sub, desc, tags, link=None, tag_class="tag"):
    tags_html = "".join(f"<span class='{tag_class}'>{t}</span>" for t in tags)
    link_html = f"<a href='{link}' target='_blank' style='font-size:0.8rem; float:right;'>💻 Voir le repo</a>" if link else ""
    st.markdown(f"""
<div class='project-card'>
    <p class='project-title'>{title} {link_html}</p>
    <p class='project-sub'>{sub}</p>
    <p class='project-desc'>{desc}</p>
    {tags_html}
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# PROJETS
# ---------------------------------------------------------------

project_card(
    title="Pipeline de collecte et traitement temps réel",
    sub="Azure Stream Analytics · Logic Apps · PostgreSQL · JSON Events",
    desc=(
        "Mise en place d'une chaîne Cloud complète permettant la collecte, le traitement "
        "et l'ingestion d'événements en temps réel dans PostgreSQL.<br>"
        "Ingestion via Logic Apps · Transformation dans Stream Analytics · "
        "Routage dynamique vers APIs · Monitoring et alertes automatisées."
    ),
    tags=["Azure", "Stream Analytics", "Logic Apps", "PostgreSQL", "JSON", "Monitoring"],
)

project_card(
    title="Automatisation de flux via Node-RED / FlowFuse",
    sub="API Graph · Flows automatisés · SharePoint · Intégration fichiers",
    desc=(
        "Conception de flux automatisés pour récupérer, transformer et déposer des fichiers "
        "provenant de SharePoint via l'API Graph Microsoft. "
        "Déclencheurs programmés, gestion d'erreurs, logs centralisés et reprise automatique."
    ),
    tags=["FlowFuse", "Node-RED", "API Graph", "Automatisation", "SharePoint"],
)

project_card(
    title="Modélisation & Dataviz — Tableaux de bord BI",
    sub="Power BI · Qlik · Modélisation DWH · KPI métiers",
    desc=(
        "Construction de modèles de données optimisés et dashboards visuels pour différents métiers : "
        "opérations, finance, support client. "
        "Définition des indicateurs, mise en qualité des données, UX des visuels, publication et gestion des droits."
    ),
    tags=["Power BI", "Qlik", "DAX", "Modélisation", "KPI", "Dataviz"],
)

project_card(
    title="Retail Pipeline ELT — Olist Brazil E-Commerce",
    sub="Projet portfolio · Python · PostgreSQL · dbt · Airflow · scikit-learn · Prophet",
    desc=(
        "Pipeline ELT end-to-end sur le dataset Olist Brazil (99 441 commandes, Kaggle). "
        "Architecture Medallion : ingestion Python → PostgreSQL (raw) · dbt (staging → marts) · "
        "Airflow 2.9 · Prophet (prévisions revenue) · scikit-learn (scoring satisfaction) · Metabase.<br>"
        "La page <em>Démo monitoring</em> présente les résultats d'analyse issus de ce dataset."
    ),
    tags=["Python", "PostgreSQL", "dbt", "Airflow", "scikit-learn", "Prophet", "Metabase", "ELT"],
    tag_class="tag tag-green",
    link="https://github.com/DeboraMandon/retail-pipeline-elt",
)

project_card(
    title="CV Interactif — Application Streamlit",
    sub="Streamlit · Python · SQLite · GitHub Actions · Streamlit Community Cloud",
    desc=(
        "Cette application — CV dynamique déployé sur Streamlit Community Cloud. "
        "Multi-pages, formulaire de contact avec stockage SQLite et espace admin sécurisé, "
        "démo monitoring pipeline avec données réelles, keep-alive GitHub Actions, "
        "secrets gérés via Streamlit Secrets."
    ),
    tags=["Streamlit", "Python", "SQLite", "GitHub Actions", "CI/CD"],
    link="https://github.com/DeboraMandon/cv-debora-mandon-streamlit",
)

st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
