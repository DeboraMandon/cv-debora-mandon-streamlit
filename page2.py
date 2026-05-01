import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.timeline {
    border-left: 3px solid #4b9ce2;
    padding-left: 20px;
    margin-left: 10px;
}
.timeline-item {
    margin-bottom: 40px;
    position: relative;
    animation: slideInLeft 0.6s ease forwards;
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
.exp-title   { font-size: 1.2rem; font-weight: 700; margin-bottom: 2px; }
.exp-company { color: #403EBB; font-size: 1rem; margin-bottom: 5px; font-weight: 500; }
.exp-dates   { color: #E69B73; font-size: 0.9rem; margin-bottom: 10px; }
.exp-tag {
    display: inline-block;
    background: #e8f0ff;
    color: #2a4fb4;
    padding: 3px 9px;
    margin: 3px 4px 0 0;
    border-radius: 8px;
    font-size: 0.78rem;
    font-weight: 600;
}
.aside-badge {
    display: inline-block;
    background: #fff3e0;
    color: #e65100;
    padding: 3px 9px;
    border-radius: 8px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-bottom: 8px;
}
@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-30px); }
    to   { opacity: 1; transform: translateX(0); }
}
a[data-testid="stPageLink"] {
    text-align: center !important;
    justify-content: center !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>Expériences professionnelles</h1>", unsafe_allow_html=True)
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("<div class='timeline'>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# EXPÉRIENCE 1 — BIIR
# ---------------------------------------------------------------

st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)
st.markdown("<p class='exp-title'>Consultante Data / BI — Data Engineer</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-company'>BIIR · ESN spécialisée BI · Bordeaux</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-dates'>Depuis 2023</p>", unsafe_allow_html=True)

st.markdown("""
• Conception et mise en place d'architectures de données pour la centralisation et la valorisation de données opérationnelles.<br>
• Modélisation de bases de données relationnelles (PostgreSQL / SQL Server) : schémas, tables de faits et dimensions.<br>
• Développement de pipelines ETL/ELT avec Talend, Azure Logic Apps et Azure Stream Analytics.<br>
• Développement de scripts SQL et Python pour la transformation, la qualité et l'automatisation des flux de données.<br>
• Mise en place de traitements temps réel et génération d'événements JSON pour l'alimentation de systèmes aval.<br>
• Exposition et valorisation de la donnée via Power BI et Qlik.<br>
• Collaboration avec équipes métiers et techniques pour la définition des KPI et la structuration des modèles analytiques.<br>
• Réalisation d'avant-vente et rédaction d'offres commerciales.
""", unsafe_allow_html=True)

st.markdown("<br><span class='aside-badge'>Activité annexe</span> <strong>Responsable Communication & Marketing</strong> — création du pôle communication, branding, contenus, réseaux sociaux, supports commerciaux.", unsafe_allow_html=True)

for t in ["Azure", "Logic Apps", "Stream Analytics", "PostgreSQL", "SQL Server", "Talend", "Power BI", "Qlik", "Python", "SQL"]:
    st.markdown(f"<span class='exp-tag'>{t}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# EXPÉRIENCE 2 — IMADIS Bordeaux
# ---------------------------------------------------------------

st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)
st.markdown("<p class='exp-title'>Responsable Régional de Site</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-company'>IMADIS · Téléradiologie · Bordeaux</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-dates'>2021 – 2023</p>", unsafe_allow_html=True)

st.markdown("""
• Supervision de la logistique et de la maintenance des sites.<br>
• Formation et intégration des radiologues.<br>
• Animation et organisation d'événements.<br>
• Relai de l'équipe support et des Centres Hospitaliers.<br>
• Mise en place des outils BI pour les métiers (dashboards / reporting).<br>
• Participation au développement et rayonnement de l'activité.
""", unsafe_allow_html=True)

for t in ["Management", "BI", "Formation", "Coordination", "Santé"]:
    st.markdown(f"<span class='exp-tag'>{t}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# EXPÉRIENCE 3 — IMADIS Lyon
# ---------------------------------------------------------------

st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)
st.markdown("<p class='exp-title'>Chef de Projet – Téléradiologie</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-company'>IMADIS · Téléradiologie · Lyon</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-dates'>2019 – 2021</p>", unsafe_allow_html=True)

st.markdown("""
• Déploiement de la solution de téléradiologie sur les sites clients.<br>
• Formation des utilisateurs (radiologues, personnels hospitaliers).<br>
• Support technique et résolution des incidents.<br>
• Management d'une équipe de 10 personnes.<br>
• Participation à l'élaboration des plans de projet (échéanciers, jalons et livrables).
""", unsafe_allow_html=True)

for t in ["Gestion de projet", "Management", "Formation", "Support", "Santé"]:
    st.markdown(f"<span class='exp-tag'>{t}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# EXPÉRIENCE 4 — HEH Lyon
# ---------------------------------------------------------------

st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)
st.markdown("<p class='exp-title'>Manipulatrice en Radiologie</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-company'>HEH · Hôpital · Lyon</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-dates'>2009 – 2019</p>", unsafe_allow_html=True)

st.markdown("""
• Prise en charge de patients pour des examens radiologiques et scanographiques.<br>
• 10 ans d'expérience dans un environnement hospitalier à fort enjeu humain et technique.
""", unsafe_allow_html=True)

for t in ["Radiologie", "Scanner", "Hôpital", "Relation patient"]:
    st.markdown(f"<span class='exp-tag'>{t}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # fin timeline

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# FORMATIONS
# ---------------------------------------------------------------

st.markdown("## 🎓 Formations")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
**Master Data Analyst — Titre RNCP Niv. 2**
Liora (Datascientest) · Écoles des Mines ParisTech
*2022 – 2023*
""")

with col2:
    st.markdown("""
**Licence Manipulateur en Électroradiologie Médicale**
Esquirol · Lyon
*2006 – 2009*
""")

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------------

btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("⬅️ Revenir au Profil ❄️", use_container_width=True):
        st.switch_page("page1.py")

with btn_col2:
    if st.button("🏗️ Aller aux Projets ➡️", use_container_width=True):
        st.switch_page("page3.py")

left, center, right = st.columns([7, 2, 7])
with center:
    st.page_link("page0.py", label="🏠 Accueil", use_container_width=True)
