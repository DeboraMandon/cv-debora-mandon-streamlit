import streamlit as st


# ----------------------------------------------
# PAGE CONFIG
# ----------------------------------------------
st.set_page_config(
    page_title="Accueil – CV Débora Mandon",
    page_icon="🎈",
    layout="wide"
)

# ----------------------------------------------
# HEADER
# ----------------------------------------------
st.markdown("<h1 style='text-align:center;'>Bienvenue sur mon CV interactif 🎈</h1>", unsafe_allow_html=True)
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
st.markdown("---")

st.write(
    """
    Cette application présente mon parcours, mes compétences et mes projets 
    en Data Engineering, Business Intelligence et Communication.  
    """
)
#st.write("")
st.write(
    """
    _Utilisez le menu à gauche pour naviguer dans les différentes pages_.
    """
)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")


# ----------------------------------------------
# Section MÉTRIQUES (
# ----------------------------------------------

#st.markdown("---")
st.markdown("<h2 style='text-align:center;'>📊 Mon parcours en quelques chiffres</h2>", unsafe_allow_html=True)
st.markdown("<div style='height:60px;'></div>", unsafe_allow_html=True)

col_m1, col_m2, col_m3, col_m4 = st.columns(4)

with col_m1:
    st.metric("Imagerie/Télaradiologie", "16 ans", "depuis 2009")  # 2025-2009 [file:1]

with col_m2:
    st.metric("Data Engineering", "+ 3 ans", "depuis 2022")  # BiiR [file:1]

with col_m3:
    st.metric("Projets Clients", "+ 7", delta="en prod")

with col_m4:
    if st.button("🎉 Célébrer !", use_container_width=True):
        st.balloons()


st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")


# ----------------------------------------------
# CTA SECTION AVEC BOUTON "Aller au Profil"
# ----------------------------------------------

profil_col, lien_col = st.columns([2, 1])

with profil_col:
    st.markdown("""
    ### 👉 Pour commencer, cliquez sur <span style="color:#403EBB; font-weight:bold;">Profil</span>
    """, unsafe_allow_html=True)

with lien_col:
    if st.button("❄️ Profil ➡️", use_container_width=True):
        st.switch_page("page1.py")
