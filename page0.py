import streamlit as st

st.set_page_config(
    page_title="Débora Mandon — Data Engineer",
    page_icon="👤",
    layout="wide"
)

st.markdown("""
<style>
.hero-title {
    font-size: 2.4rem;
    font-weight: 800;
    margin-bottom: 4px;
    line-height: 1.2;
}
.hero-subtitle {
    font-size: 1.15rem;
    color: #403EBB;
    font-weight: 600;
    margin-bottom: 16px;
}
.hero-text {
    font-size: 1rem;
    line-height: 1.7;
    max-width: 680px;
}
.kpi-box {
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 18px 20px;
    text-align: center;
    background: #fafafa;
}
.kpi-value {
    font-size: 2rem;
    font-weight: 800;
    color: #403EBB;
    margin: 0;
}
.kpi-label {
    font-size: 0.82rem;
    color: #888;
    margin-top: 4px;
}
.kpi-since {
    font-size: 0.78rem;
    color: #aaa;
    margin-top: 2px;
}
@media (prefers-color-scheme: dark) {
    .kpi-box {
        background: #1e1e1e !important;
        border-color: #333 !important;
    }
    .hero-text { color: #ddd; }
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# HERO
# ---------------------------------------------------------------

st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)

col_text, col_space = st.columns([2, 1])

with col_text:
    st.markdown("<p class='hero-title'>Débora Mandon</p>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>Data Engineer · Consultante BI · Bordeaux</p>", unsafe_allow_html=True)
    st.markdown("""
<p class='hero-text'>
Consultante Data/BI confirmée avec plus de 15 ans d'expérience dans le secteur de la santé,
reconvertie dans la data depuis 2023.<br><br>
Je conçois des pipelines de données, des architectures analytiques et des tableaux de bord
qui transforment des données opérationnelles en leviers de décision concrets.<br><br>
Mon parcours hybride <strong>santé / data</strong> me permet d'aborder les projets avec
une vision métier forte et une rigueur technique éprouvée.
</p>
""", unsafe_allow_html=True)

st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# KPI
# ---------------------------------------------------------------

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown("""
<div class='kpi-box'>
    <p class='kpi-value'>15+</p>
    <p class='kpi-label'>Années d'expérience</p>
    <p class='kpi-since'>santé & data</p>
</div>""", unsafe_allow_html=True)

with k2:
    st.markdown("""
<div class='kpi-box'>
    <p class='kpi-value'>2+</p>
    <p class='kpi-label'>Ans en Data Engineering</p>
    <p class='kpi-since'>depuis 2023 · BIIR</p>
</div>""", unsafe_allow_html=True)

with k3:
    st.markdown("""
<div class='kpi-box'>
    <p class='kpi-value'>7+</p>
    <p class='kpi-label'>Projets clients</p>
    <p class='kpi-since'>en production</p>
</div>""", unsafe_allow_html=True)

with k4:
    st.markdown("""
<div class='kpi-box'>
    <p class='kpi-value'>10</p>
    <p class='kpi-label'>Personnes managées</p>
    <p class='kpi-since'>IMADIS Lyon · 2019–2021</p>
</div>""", unsafe_allow_html=True)

st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# STACK RAPIDE
# ---------------------------------------------------------------

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
st.markdown("#### 🛠️ Stack principal")

tags = [
    "SQL", "Python", "PostgreSQL", "SQL Server", "Azure",
    "Talend", "dbt", "Databricks", "Airflow",
    "Power BI", "Qlik", "Metabase", "Node-RED"
]

st.markdown(
    " ".join(
        f"<span style='display:inline-block; background:#e8f0ff; color:#2a4fb4; "
        f"padding:5px 11px; margin:3px; border-radius:8px; font-size:0.82rem; "
        f"font-weight:600;'>{t}</span>"
        for t in tags
    ),
    unsafe_allow_html=True
)

st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
