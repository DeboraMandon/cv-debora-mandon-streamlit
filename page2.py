import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.timeline {
    border-left: 2px solid #403EBB;
    padding-left: 24px;
    margin-left: 8px;
}
.timeline-item {
    margin-bottom: 36px;
    position: relative;
}
.timeline-item::before {
    content: "";
    width: 12px;
    height: 12px;
    background-color: #403EBB;
    border-radius: 50%;
    position: absolute;
    left: -30px;
    top: 6px;
    border: 2px solid white;
    box-shadow: 0 0 0 2px #403EBB;
}
.exp-title   { font-size: 1.1rem; font-weight: 700; margin: 0 0 2px 0; }
.exp-company { color: #403EBB; font-size: 0.9rem; margin: 0 0 2px 0; font-weight: 500; }
.exp-dates   { color: #E69B73; font-size: 0.82rem; margin: 0 0 10px 0; }
.exp-bullet  { font-size: 0.88rem; line-height: 1.6; margin: 0; color: inherit; }
.aside-badge {
    display: inline-block;
    background: #fff3e0;
    color: #e65100;
    padding: 2px 8px;
    border-radius: 6px;
    font-size: 0.76rem;
    font-weight: 700;
    margin-right: 6px;
    vertical-align: middle;
}
.tag {
    display: inline-block;
    background: #e8f0ff;
    color: #2a4fb4;
    padding: 3px 10px;
    margin: 4px 4px 0 0;
    border-radius: 6px;
    font-size: 0.76rem;
    font-weight: 600;
}
.tag-health {
    background: #fce4ec;
    color: #880e4f;
}
.formation-card {
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 16px 20px;
    background: #fafafa;
}
.formation-title { font-size: 0.95rem; font-weight: 700; margin: 0 0 4px 0; }
.formation-sub   { font-size: 0.82rem; color: #888; margin: 0; }
.section-label {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #888;
    margin: 0 0 16px 0;
}
@media (prefers-color-scheme: dark) {
    .timeline-item::before { border-color: #111 !important; }
    .tag     { background: #1a2a4a !important; color: #a0b4ff !important; }
    .tag-health { background: #3a1020 !important; color: #ff80ab !important; }
    .formation-card { background: #1e1e1e !important; border-color: #333 !important; }
    .aside-badge { background: #3a2000 !important; color: #ffb74d !important; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>Expériences</h1>", unsafe_allow_html=True)
st.markdown("<div style='height:24px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# TIMELINE
# ---------------------------------------------------------------

st.markdown("<div class='timeline'>", unsafe_allow_html=True)

# --- BIIR ---
st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)
st.markdown("<p class='exp-title'>Consultante Data / BI — Data Engineer</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-company'>BIIR · ESN spécialisée BI · Bordeaux</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-dates'>Depuis 2023</p>", unsafe_allow_html=True)
st.markdown("""
<p class='exp-bullet'>
• Conception d'architectures de données pour la centralisation et la valorisation de données opérationnelles.<br>
• Modélisation relationnelle (PostgreSQL / SQL Server) : schémas, tables de faits et dimensions.<br>
• Développement de pipelines ETL/ELT avec Talend, Azure Logic Apps et Azure Stream Analytics.<br>
• Scripts SQL et Python pour la transformation, la qualité et l'automatisation des flux.<br>
• Traitements temps réel et génération d'événements JSON pour l'alimentation de systèmes aval.<br>
• Exposition de la donnée via Power BI et Qlik.<br>
• Collaboration métier / technique — définition des KPI et structuration des modèles analytiques.<br>
• Avant-vente et rédaction d'offres commerciales.
</p>
""", unsafe_allow_html=True)
st.markdown("<p style='margin:8px 0 6px 0;'><span class='aside-badge'>Activité annexe</span> <strong>Responsable Communication &amp; Marketing</strong> — création du pôle, branding, contenus, réseaux sociaux.</p>", unsafe_allow_html=True)
for t in ["Azure", "Logic Apps", "Stream Analytics", "PostgreSQL", "SQL Server", "Talend", "Power BI", "Qlik", "Python", "SQL"]:
    st.markdown(f"<span class='tag'>{t}</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- IMADIS Bordeaux ---
st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)
st.markdown("<p class='exp-title'>Responsable Régional de Site</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-company'>IMADIS · Téléradiologie · Bordeaux</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-dates'>2021 – 2023</p>", unsafe_allow_html=True)
st.markdown("""
<p class='exp-bullet'>
• Supervision de la logistique et de la maintenance des sites.<br>
• Formation et intégration des radiologues.<br>
• Animation et organisation d'événements.<br>
• Relai de l'équipe support et des Centres Hospitaliers.<br>
• Mise en place des outils BI pour les métiers (dashboards / reporting).<br>
• Participation au développement et rayonnement de l'activité.
</p>
""", unsafe_allow_html=True)
for t in ["Management", "BI", "Formation", "Coordination"]:
    st.markdown(f"<span class='tag tag-health'>{t}</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- IMADIS Lyon ---
st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)
st.markdown("<p class='exp-title'>Chef de Projet – Téléradiologie</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-company'>IMADIS · Téléradiologie · Lyon</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-dates'>2019 – 2021</p>", unsafe_allow_html=True)
st.markdown("""
<p class='exp-bullet'>
• Déploiement de la solution de téléradiologie sur les sites clients.<br>
• Formation des utilisateurs (radiologues, personnels hospitaliers).<br>
• Support technique et résolution des incidents.<br>
• Management d'une équipe de 10 personnes.<br>
• Élaboration des plans de projet (échéanciers, jalons, livrables).
</p>
""", unsafe_allow_html=True)
for t in ["Gestion de projet", "Management", "Formation", "Support"]:
    st.markdown(f"<span class='tag tag-health'>{t}</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- HEH Lyon ---
st.markdown("<div class='timeline-item'>", unsafe_allow_html=True)
st.markdown("<p class='exp-title'>Manipulatrice en Radiologie</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-company'>HEH · Hôpital · Lyon</p>", unsafe_allow_html=True)
st.markdown("<p class='exp-dates'>2009 – 2019</p>", unsafe_allow_html=True)
st.markdown("""
<p class='exp-bullet'>
• Prise en charge de patients pour des examens radiologiques et scanographiques.<br>
• 10 ans d'expérience dans un environnement hospitalier à fort enjeu humain et technique.
</p>
""", unsafe_allow_html=True)
for t in ["Radiologie", "Scanner", "Relation patient"]:
    st.markdown(f"<span class='tag tag-health'>{t}</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # fin timeline

st.markdown("<div style='height:32px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# FORMATIONS
# ---------------------------------------------------------------

st.markdown("<p class='section-label'>Formations</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
<div class='formation-card'>
    <p class='formation-title'>Master Data Analyst — Titre RNCP Niv. 2</p>
    <p class='formation-sub'>Liora (Datascientest) · Écoles des Mines ParisTech · 2022 – 2023</p>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class='formation-card'>
    <p class='formation-title'>Licence Manipulateur en Électroradiologie Médicale</p>
    <p class='formation-sub'>Esquirol · Lyon · 2006 – 2009</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
