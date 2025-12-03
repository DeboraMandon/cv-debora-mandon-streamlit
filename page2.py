import streamlit as st

st.set_page_config(layout="wide")

# ---------- STYLE TIMELINE ----------
st.markdown("""
<style>

.timeline {
    border-left: 3px solid #4b9ce2;
    padding-left: 20px;
    margin-left: 10px;
}

.timeline-item {
    margin-bottom: 35px;
    position: relative;
}

.timeline-item::before {
    content: "";
    width: 15px;
    height: 15px;
    background-color: #4b9ce2;
    border-radius: 50%;
    position: absolute;
    left: -28px;
    top: 5px;
    border: 2px solid white;
    box-shadow: 0 0 0 2px #4b9ce2;
}

.exp-title {
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 2px;
}

.exp-company {
    color: #403EBB;
    font-size: 1rem;
    margin-bottom: 5px;
    font-weight: 500;
}

.exp-dates {
    color: #E69B73;
    font-size: 0.9rem;
    margin-bottom: 10px;
}

.exp-desc {
    color: #403EBB;
    font-size: 0.95rem;
    margin-bottom: 5px;
}

@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-30px); }
    to { opacity: 1; transform: translateX(0); }
}
.timeline-item {
    margin-bottom: 35px;
    position: relative;
    animation: slideInLeft 0.6s ease forwards;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>Expériences professionnelles</h1>", unsafe_allow_html=True)

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("<div class='timeline'>", unsafe_allow_html=True)

# ---------- EXPERIENCE 1 ----------
st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)

st.markdown("<p class='exp-title'>Responsable Communication & Marketing (20%)</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-company'>BiiR – ESN spécialisée en Data</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-dates'>2024 – Aujourd’hui</p>", unsafe_allow_html=True)

st.markdown(
    """
    • Création du pôle communication de l’entreprise.<br>
    • Production des contenus internes et externes (tone of voice, identité).<br>
    • Gestion des réseaux sociaux, branding et supports commerciaux.<br>
    • Conception des documents corporate et process internes.<br>
    • Coordination des retours consultants pour valorisation des missions.
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------- EXPERIENCE 2 ----------
st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)

st.markdown("<p class='exp-title'>Consultante Data / BI – Data Engineer</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-company'>BiiR – ESN spécialisée en Data</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-dates'>2023 – Aujourd’hui</p>", unsafe_allow_html=True)

st.markdown(
    """
    • Conception et modélisation de bases de données (PostgreSQL, SQL Server).<br>
    • Mise en place de pipelines data (Azure, Logic Apps, Stream Analytics).<br>
    • Intégrations API (Graph API, automatisation, orchestrations).<br>
    • Développements FlowFuse / Node-RED.<br>
    • Création de dashboards Power BI et Qlik.<br>
    • Accompagnement clients : cadrage, méthodo, best practices.<br>
    • Participation à l’avant-vente (réponses, structuration technique).
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------- EXPERIENCE 3 ----------
st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)

st.markdown("<p class='exp-title'>Consultante – Analyste Data (stages & alternances)</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-company'>Divers projets & entreprises</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-dates'>2021 – 2023</p>", unsafe_allow_html=True)

st.markdown(
    """
    • Analyse de données, reporting et pré-études BI.<br>
    • Automatisation de traitements et ETL simples.<br>
    • Constructions de modèles d’indicateurs.<br>
    • Mise en qualité de données et fiabilisation de référentiels.<br>
    • Participation à des ateliers métier et à la documentation.
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # timeline end

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ----------------------------------------------
# CTA SECTION AVEC BOUTON "changement de pages"
# ----------------------------------------------

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

btn_col1, btn_col2 = st.columns([2,2])

with btn_col1:
    if st.button("⬅️ Revenir au Profil ❄️", use_container_width=True):
        st.switch_page("page1.py")

    
with btn_col2:
    if st.button("🏗️ Aller aux Projets ➡️", use_container_width=True):
        st.switch_page("page3.py")

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
