import streamlit as st

st.set_page_config(layout="wide")

# ----------------- STYLE -----------------
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
}

.project-desc {
    font-size: 0.95rem;
    line-height: 1.5;
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

@media (prefers-color-scheme: dark) {
    .project-card {
        background: #1e1e1e !important;
        border-color: #444 !important;
        color: #e0e0e0 !important;
    }
    .project-desc {
        color: #e0e0e0 !important;
    }
    .tag {
        background: #2a4fb4 !important;
        color: white !important;
    }
}

/* Animation universelle */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
.project-card {
    animation: fadeInUp 0.6s ease forwards;
    margin-bottom: 25px;
}
.project-card:nth-child(1) { animation-delay: 0.1s; }
.project-card:nth-child(2) { animation-delay: 0.2s; }
.project-card:nth-child(3) { animation-delay: 0.3s; }

.tags-container {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: space-between;
    margin-top: 15px;
}
.tags-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    width: 100%;
}
.tag {
    /* vos styles existants + */
    flex: 0 0 auto;
    margin: 0;
}
@media (prefers-color-scheme: dark) {
    .tags-container, .tags-row {
        color: #e0e0e0;
    }
}

</style>
""", unsafe_allow_html=True)

# ----------------- CONTENU -----------------
st.markdown("<h1 style='text-align:center;'>Projets</h1>", unsafe_allow_html=True)

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
# ========================================================
# Projet 1
# ========================================================

st.markdown("""
<div class='project-card'>
    <p class='project-title'>Pipeline de collecte et traitement temps réel</p>
    <p class='project-sub'>Azure Stream Analytics • Logic Apps • PostgreSQL • JSON Events</p>
    <p class='project-desc'>
        Mise en place d'une chaîne Cloud complète permettant la collecte, le traitement
        et l'ingestion d'événements en temps réel dans PostgreSQL.<br><br>
        <strong>Le pipeline inclut :</strong><br>
        • ingestion via Logic Apps<br>
        • transformation dans Stream Analytics<br>
        • routage dynamique vers APIs<br>
        • monitoring et alertes automatisées
    </p>
""", unsafe_allow_html=True)

# Tags
tags = ["Azure", "Stream Analytics", "Logic Apps", "PostgreSQL", "JSON", "Monitoring"]
for t in tags:
    st.markdown(f"<span class='tag'>{t}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ========================================================
# Projet 2
# ========================================================
st.markdown("---")
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

st.markdown("""
<div class='project-card'>
    <p class='project-title'>Automatisation de flux via Node-RED / FlowFuse</p>
    <p class='project-sub'>API Graph • Flows automatisés • Intégration fichiers</p>
    <p class='project-desc'>
        Conception de flux automatisés pour récupérer, transformer et déposer des fichiers
        provenant de SharePoint via l’API Graph.  
        Déclencheurs programmés, gestion d’erreurs, logs centralisés, 
        et mécanismes de reprise automatique pour garantir la fiabilité des échanges.
    </p>
""", unsafe_allow_html=True)

tags = ["FlowFuse", "Node-RED", "API Graph", "Automatisation", "SharePoint", "Intégration"]
for t in tags:
    st.markdown(f"<span class='tag'>{t}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ========================================================
# Projet 3
# ========================================================
st.markdown("---")
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

st.markdown("""
<div class='project-card'>
    <p class='project-title'>Modélisation & Dataviz – Tableaux de bord BI</p>
    <p class='project-sub'>Power BI • Qlik • Modélisation DWH • KPI métiers</p>
    <p class='project-desc'>
        Construction de modèles de données optimisés et dashboards visuels
        pour différents métiers : opérations, finance, support client.  
        Travail sur :  
        – définition d’indicateurs  
        – création de jeux de données propres  
        – mise en qualité  
        – UX des visuels  
        – publication et gestion des droits 
    </p>
""", unsafe_allow_html=True)

tags = ["Power BI", "Qlik", "DAX", "Modélisation", "KPI", "Dataviz"]
for t in tags:
    st.markdown(f"<span class='tag'>{t}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ----------------------------------------------
# CTA SECTION AVEC BOUTON "changement de pages"
# ----------------------------------------------

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

btn_col1, btn_col2 = st.columns([2, 2])

with btn_col1:
    if st.button("⬅️ Revenir aux Expériences 🎉", use_container_width=True):
        st.switch_page("page2.py")

with btn_col2:
    if st.button("📲 Aller au Contact ➡️", use_container_width=True):
        st.switch_page("page4.py")


# ----------------------------------------------
# BOUTON ACCUEIL
# ----------------------------------------------

espace, btn_col, espace = st.columns([7,1,7])

with espace:
    st.markdown("")

with btn_col:
    st.markdown("""
    ### <a href="/page1" target="_self" style="color:#403EBB; font-weight:bold;">Accueil</a>
    # """, unsafe_allow_html=True)