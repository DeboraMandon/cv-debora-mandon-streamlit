import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.domain-card {
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 20px 22px;
    background: #fafafa;
    height: 100%;
}
.domain-title {
    font-size: 1rem;
    font-weight: 700;
    color: #403EBB;
    margin-bottom: 12px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.domain-item {
    font-size: 0.9rem;
    padding: 4px 0;
    border-bottom: 1px solid #f0f0f0;
    color: inherit;
}
.tool-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid #f0f0f0;
}
.tool-name {
    font-weight: 600;
    font-size: 0.9rem;
    border-bottom: 1px dotted #0056a3;
    cursor: help;
    position: relative;
}
.tool-name:hover::after {
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
.stars { font-size: 1.1rem; letter-spacing: 2px; }
.star-filled { color: #ffb400; }
.star-empty  { color: #ddd; }
.pill {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.82rem;
    font-weight: 600;
    margin: 3px 4px 3px 0;
}
.pill-lang { background: #f0f4ff; color: #2a4fb4; }
.pill-soft { background: #f0faf0; color: #1b5e20; }
@media (prefers-color-scheme: dark) {
    .domain-card { background: #1e1e1e !important; border-color: #333 !important; }
    .domain-item { border-color: #2a2a2a !important; }
    .tool-row    { border-color: #2a2a2a !important; }
    .star-empty  { color: #444 !important; }
    .pill-lang   { background: #1a2a4a !important; color: #a0b4ff !important; }
    .pill-soft   { background: #1a2a1a !important; color: #80c080 !important; }
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# HEADER
# ---------------------------------------------------------------

st.markdown("<h1 style='text-align:center;'>Compétences & Profil</h1>", unsafe_allow_html=True)
st.markdown("<div style='height:24px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# DOMAINES — 3 cards
# ---------------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class='domain-card'>
    <p class='domain-title'>Data Engineering</p>
    <p class='domain-item'>Modélisation & architecture data</p>
    <p class='domain-item'>Pipelines ETL / ELT</p>
    <p class='domain-item'>Optimisation SQL</p>
    <p class='domain-item'>Intégrations API & automatisation</p>
    <p class='domain-item'>Databricks · dbt · Airflow</p>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class='domain-card'>
    <p class='domain-title'>Cloud & Orchestration</p>
    <p class='domain-item'>Azure — Logic Apps · Stream Analytics</p>
    <p class='domain-item'>ADLS · Key Vault · Databricks</p>
    <p class='domain-item'>Talend</p>
    <p class='domain-item'>FlowFuse · Node-RED</p>
    <p class='domain-item'>Git · CI/CD · GitHub Actions</p>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class='domain-card'>
    <p class='domain-title'>DataViz & BI</p>
    <p class='domain-item'>Power BI · DAX</p>
    <p class='domain-item'>Qlik Sense</p>
    <p class='domain-item'>Metabase</p>
    <p class='domain-item'>Analyse fonctionnelle & KPI</p>
    <p class='domain-item'>Communication & Branding</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:36px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# OUTILS — table avec étoiles, 2 colonnes
# ---------------------------------------------------------------

st.markdown("### Outils & technologies")
st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)

tools = {
    "SQL":        (5, "Langage de requête relationnel — utilisé quotidiennement."),
    "Python":     (4, "Scripts de transformation, automatisation, ML."),
    "PostgreSQL": (4, "SGBD open-source — modélisation, optimisation de requêtes."),
    "SQL Server": (4, "SGBD Microsoft — contexte Azure / client."),
    "Azure":      (4, "Logic Apps, Stream Analytics, ADLS, Key Vault, Databricks."),
    "Talend":     (4, "ETL : jobs de transformation, intégration SharePoint via Graph API."),
    "Power BI":   (4, "Dashboards, mesures DAX, modèles tabulaires."),
    "Git":        (4, "Versioning, branches, PR, GitHub Actions."),
    "Qlik Sense": (3, "Dashboards KPI, set analysis, cartes régionales."),
    "dbt":        (3, "Transformation SQL versionnée, tests, documentation."),
    "Databricks": (3, "Pipelines Spark sur Azure, lecture ADLS, écriture JDBC."),
    "Node-RED":   (3, "Flows d'intégration, déclencheurs, logique conditionnelle."),
    "Airflow":    (2, "Orchestration de DAGs, scheduling de pipelines."),
    "Metabase":   (2, "Dashboards analytiques self-service."),
}

items = list(tools.items())
mid = len(items) // 2
left_tools  = items[:mid]
right_tools = items[mid:]

col_l, col_spacer, col_r = st.columns([5, 0.3, 5])

def render_tools(tool_list):
    for tool, (level, tip) in tool_list:
        stars = "".join(
            "<span class='star-filled'>★</span>" if i < level
            else "<span class='star-empty'>☆</span>"
            for i in range(5)
        )
        st.markdown(f"""
<div class='tool-row'>
    <span class='tool-name' data-tip="{tip}">{tool}</span>
    <span class='stars'>{stars}</span>
</div>""", unsafe_allow_html=True)

with col_l:
    render_tools(left_tools)

with col_r:
    render_tools(right_tools)

st.markdown("<div style='height:36px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# LANGUES + SOFT SKILLS — côte à côte
# ---------------------------------------------------------------

col_lang, col_soft = st.columns(2)

with col_lang:
    st.markdown("### Langues")
    for lang, level in [("Français", "Langue maternelle"), ("Anglais", "Niveau technique"), ("Espagnol", "Scolaire")]:
        st.markdown(
            f"<span class='pill pill-lang'>{lang}</span> <span style='font-size:0.85rem; color:#888;'>{level}</span>",
            unsafe_allow_html=True
        )

with col_soft:
    st.markdown("### Savoir-être")
    softs = [
        "Esprit analytique", "Rigueur", "Pédagogie",
        "Vulgarisation technique", "Autonomie", "Vision métier / technique"
    ]
    for s in softs:
        st.markdown(f"<span class='pill pill-soft'>{s}</span>", unsafe_allow_html=True)

st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
