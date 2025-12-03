import streamlit as st

st.set_page_config(layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
.section-title {
    font-size: 1.6rem;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 10px;
}

.text-muted {
    color: #666;
    font-size: 0.95rem;
}

.card {
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #ddd;
    background-color: #fafafa;
}

.tools-container {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.skill-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 6px 12px;
    background-color: #e8f4ff;
    color: #0056a3;
    font-size: 0.85rem;
    font-weight: 600;
    border-radius: 12px;
    border: 1px solid #c8ddf1;
    transition: 0.2s ease;
    white-space: nowrap;  /* empêche les retours à la ligne dans le badge */
}

.skill-badge:hover {
    background-color: #0056a3;
    color: white;
    cursor: pointer;
    transform: translateY(-2px);
    box-shadow: 0px 3px 8px rgba(0,0,0,0.15);
}

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

.stars {
    font-size: 1.2rem;
    letter-spacing: 3px;
}

.star-filled {
    color: #ffb400; /* jaune doré */
}

.star-empty {
    color: #ccc; /* gris */
}


/* Animation to fade in elements */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(10px);}
    to {opacity: 1; transform: translateY(0);}
}
.fade-in {
    animation: fadeIn 0.8s ease forwards;
}

/* Tooltip style for info hints */
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
    opacity: 1;
    pointer-events: auto;
}
.tooltip::after {
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITRE ----------
st.markdown("<h1 style='text-align:center;'>Profil professionnel</h1>", unsafe_allow_html=True)

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------- SECTION PRESENTATION ----------
st.markdown("<h2 >🧑‍💻 Présentation</h2>", unsafe_allow_html=True)

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

st.markdown(
    """
    Data Engineer / Consultante Data BI depuis **2023**, intervenant sur :
    
    • la modélisation et l’architecture data  
    • la création de pipelines et d’intégrations complexes  
    • la mise en place d'infrastructures Azure, ETL, automatisations  
    • la création de dashboards et d’indicateurs métiers
    
    Je combine également une activité de **responsable communication et marketing**, ce qui apporte une vision
    plus complète sur la valorisation des données et l’image des projets livrés.
    """,
)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ----------------------------------------------
# HERO SECTION AVEC LIGNES VERTICALES
# ----------------------------------------------
st.markdown("<h2 >🎯 Vision</h2>", unsafe_allow_html=True)
st.write(
    """
    Construire des environnements data robustes, fiables et adaptés 
    aux besoins opérationnels. 
    Favoriser la compréhension 
    et la valorisation des données.
    """
)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("<h2 >🧩 Domaines d’expertise</h2>", unsafe_allow_html=True)
st.write(
    """
    - Architecture Data  
    - Pipelines & Intégration  
    - Azure / Logic Apps / Stream Analytics  
    - Power BI / Qlik  
    - Automatisation  
    - Communication & Branding
    """
)
st.write("")




st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

# ---------- SECTION COMPÉTENCES ----------
st.markdown("<h2 style='text-align:center;'>🛠️ Compétences techniques</h2>", unsafe_allow_html=True)
st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)

# 3 colonnes pour les grandes familles
col1, sep1, col2, sep2, col3 = st.columns(
    [3, 0.1, 3, 0.1, 3],
    vertical_alignment="top"
)

with col1:
    st.markdown("### 🔷 Data Engineering")
    st.markdown("""
        • Modélisation & architecture  
        • Pipelines ETL/ELT  
        • Optimisation SQL  
        • Intégrations API & automatisation  
    """)
    st.write("")  # Force a bit of height

with sep1:
    st.markdown(
        "<div style='border-left:1px solid #ccc;height:250px;margin:auto;'></div>",
        unsafe_allow_html=True
    )
    
with col2:
    st.markdown("### 🔷 Cloud & Orchestration")
    st.markdown("""
        • Azure (Logic Apps, Data Factory, Stream Analytics)  
        • FlowFuse / Node-RED  
        • Power Apps  
        • Git & CI/CD  
    """)
    st.write("")  # Force a bit of height

with sep2:
    st.markdown(
        "<div style='border-left:1px solid #ccc;height:250px;margin:auto;'></div>",
        unsafe_allow_html=True
    )
    
with col3:
    st.markdown("### 🔷 DataViz")
    st.markdown("""
        • Power BI  
        • Qlik  
        • Analyse fonctionnelle  
        • UX Data  
    """)

    st.write("")  # Force a bit of height
    

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)


# ---------- SECTION OUTILS ----------
st.markdown("<h2 style='text-align:center;'>🧩 Outils & technologies</h2>", unsafe_allow_html=True)

tools = {
    "Python": (4, "Langage de programmation polyvalent, utilisé pour l'analyse de données."),
    "SQL": (5, "Langage de requête pour bases de données relationnelles."),
    "PostgreSQL": (4, "Système de gestion de bases de données relationnelles open-source."),
    "SQL Server": (4, "Système de gestion de bases de données développé par Microsoft."),
    "Azure": (4, "Plateforme cloud de Microsoft pour le déploiement d’applications et services."),
    "Power BI": (4, "Outil Microsoft pour la visualisation et l'analyse de données."),
    "Qlik": (3, "Plateforme de Business Intelligence et d'analyse visuelle."),
    "Talend": (5, "Solution d’intégration de données ETL open-source."),
    "Node-RED": (4, "Outil de programmation par flux pour connecter des appareils matériels, API et services en ligne."),
    "Docker": (2, "Plateforme de conteneurisation pour déployer des applications."),
    "Git": (4, "Système de gestion de versions distribué.")
}

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

for tool, (level, tooltip) in tools.items():
    stars_html = ""
    for i in range(5):
        if i < level:
            stars_html += "<span class='star-filled'>★</span>"
        else:
            stars_html += "<span class='star-empty'>☆</span>"
    st.markdown(
        f"""
        <div class='tool-row'>
            <div class='tool-name tooltip' data-tip="{tooltip}">{tool}</div>
            <div class='stars'>{stars_html}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)


st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------- SECTION SOFT SKILLS ----------
st.markdown("<h2 >💡 Soft skills</h2>", unsafe_allow_html=True)
st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

st.markdown(
    """
    • Esprit analytique  
    • Communication claire  
    • Pédagogie  
    • Capacité à vulgariser la complexité  
    • Proactivité et autonomie  
    • Sens du service consultant  
    """
)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ----------------------------------------------
# CTA SECTION AVEC BOUTON "changement de pages"
# ----------------------------------------------

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

btn_col1, btn_col2 = st.columns([2,2])

with btn_col1:
    if st.button("⬅️ Revenir à l'Accueil 🎈", use_container_width=True):
        st.switch_page("page0.py")

    
with btn_col2:
    if st.button("🎉 Aller aux Expériences ➡️", use_container_width=True):
        st.switch_page("page2.py")