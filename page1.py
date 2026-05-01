import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.tool-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid #eee;
}
.tool-name {
    font-weight: 600;
    font-size: 0.95rem;
}
.stars { font-size: 1.2rem; letter-spacing: 3px; }
.star-filled { color: #ffb400; }
.star-empty  { color: #ccc; }
.tooltip {
    border-bottom: 1px dotted #0056a3;
    cursor: help;
    position: relative;
}
.tooltip:hover::after {
    content: attr(data-tip);
    position: absolute;
    left: 0;
    bottom: 120%;
    background: #0056a3;
    color: white;
    padding: 6px 10px;
    border-radius: 6px;
    white-space: nowrap;
    font-size: 0.75rem;
    z-index: 1000;
}
a[data-testid="stPageLink"] {
    text-align: center !important;
    justify-content: center !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# HEADER
# ---------------------------------------------------------------

st.markdown("<h1 style='text-align:center;'>Profil professionnel</h1>", unsafe_allow_html=True)
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# PRÉSENTATION
# ---------------------------------------------------------------

st.markdown("## 🧑‍💻 Présentation")
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

st.markdown("""
Consultante Data/BI confirmée avec **plus de 15 ans d'expérience initiale dans le secteur de la santé**.

Je conçois et développe des pipelines de données, des architectures analytiques et des tableaux de bord
permettant la valorisation de données opérationnelles.

Mon parcours hybride **santé / data** me permet d'aborder la donnée comme un levier d'impact concret,
notamment dans des secteurs à fort enjeu collectif.

En parallèle, j'occupe un rôle de **Responsable Communication & Marketing** chez BIIR,
que j'ai contribué à structurer de zéro.
""")

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# VISION
# ---------------------------------------------------------------

st.markdown("## 🎯 Vision")
st.write("""
Construire des environnements data robustes, fiables et adaptés aux besoins opérationnels.
Favoriser la compréhension et la valorisation des données comme levier de décision.
""")

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# DOMAINES D'EXPERTISE
# ---------------------------------------------------------------

st.markdown("## 🧩 Domaines d'expertise")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🔷 Data Engineering")
    st.markdown("""
- Modélisation & architecture data
- Pipelines ETL/ELT
- Optimisation SQL
- Intégrations API & automatisation
- Databricks, dbt, Airflow
    """)

with col2:
    st.markdown("### 🔷 Cloud & Orchestration")
    st.markdown("""
- Azure (Logic Apps, Stream Analytics)
- FlowFuse / Node-RED
- Talend
- Git & CI/CD
    """)

with col3:
    st.markdown("### 🔷 DataViz & BI")
    st.markdown("""
- Power BI / DAX
- Qlik Sense
- Metabase
- Analyse fonctionnelle & KPI
    """)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# OUTILS & TECHNOLOGIES
# ---------------------------------------------------------------

st.markdown("<h2 style='text-align:center;'>🛠️ Outils & technologies</h2>", unsafe_allow_html=True)
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

# (outil, niveau/5, tooltip)
tools = {
    "SQL":          (5, "Langage de requête relationnel — utilisé quotidiennement."),
    "Python":       (4, "Scripts de transformation, automatisation, ML."),
    "PostgreSQL":   (4, "SGBD relationnel open-source — modélisation, optimisation."),
    "SQL Server":   (4, "SGBD Microsoft — utilisé en contexte Azure / client."),
    "Azure":        (4, "Logic Apps, Stream Analytics, ADLS, Key Vault, Databricks."),
    "Talend":       (4, "ETL : jobs de transformation, intégration SharePoint via Graph API."),
    "Power BI":     (4, "Dashboards, mesures DAX, modèles tabulaires."),
    "Qlik Sense":   (3, "Dashboards KPI, set analysis, cartes régionales."),
    "dbt":          (3, "Transformation SQL versionnée, tests de qualité, documentation."),
    "Databricks":   (3, "Pipelines Spark sur Azure, lecture ADLS, écriture JDBC."),
    "Node-RED":     (3, "Flows d'intégration, déclencheurs, logique conditionnelle."),
    "Airflow":      (2, "Orchestration de DAGs, scheduling de pipelines."),
    "Metabase":     (2, "Dashboards analytiques self-service."),
    "Git":          (4, "Versioning, branches, PR, GitHub Actions."),
}

for tool, (level, tooltip) in tools.items():
    stars_html = "".join(
        "<span class='star-filled'>★</span>" if i < level else "<span class='star-empty'>☆</span>"
        for i in range(5)
    )
    st.markdown(
        f"""
        <div class='tool-row'>
            <div class='tool-name tooltip' data-tip="{tooltip}">{tool}</div>
            <div class='stars'>{stars_html}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# LANGUES
# ---------------------------------------------------------------

st.markdown("## 🌍 Langues")
st.markdown("""
- **Français** — Langue maternelle
- **Anglais** — Technique
- **Espagnol** — Scolaire
""")

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# SOFT SKILLS
# ---------------------------------------------------------------

st.markdown("## 💡 Soft skills")
st.markdown("""
- Esprit analytique & rigueur
- Communication claire — vulgarisation de la complexité technique
- Pédagogie & accompagnement client
- Proactivité et autonomie
- Vision hybride métier / technique
- Sens du service consultant
""")

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------------

btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("⬅️ Revenir à l'Accueil 🎈", use_container_width=True):
        st.switch_page("page0.py")

with btn_col2:
    if st.button("🎉 Aller aux Expériences ➡️", use_container_width=True):
        st.switch_page("page2.py")
