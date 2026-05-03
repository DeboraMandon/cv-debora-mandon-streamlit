################################################################################################
#        pour lancer l'application Streamlit                                                   #
#        cd C:\99_PERSO\cv_streamlit\CV_GIT\cv-debora-mandon-streamlit                        #
#        streamlit run app.py                                                                  #
#        http://localhost:8501                                                                  #
################################################################################################

import streamlit as st

# ---------------------------------------------------------------
# SIDEBAR — définie avant pg.run() pour éviter le flash
# ---------------------------------------------------------------

with st.sidebar:
    try:
        st.image("assets/photo.png", width=140)
    except Exception:
        pass

    st.markdown("""
<div style='text-align:center; margin-top:8px;'>
    <p style='font-size:1.2rem; font-weight:700; margin:0;'>Débora Mandon</p>
    <p style='font-size:0.9rem; color:#403EBB; margin:4px 0 0 0;'>Data Engineer · BI Consultant</p>
    <p style='font-size:0.8rem; color:#888; margin:2px 0 0 0;'>📍 Saint-Aubin-de-Médoc · Bordeaux</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
<div style='font-size:0.85rem; line-height:2;'>
    <a href="mailto:debora.mandon@gmail.com" style='text-decoration:none;'>📧 debora.mandon@gmail.com</a><br>
    <a href="tel:0640222354" style='text-decoration:none;'>📱 06 40 22 23 54</a><br>
    <a href="https://www.linkedin.com/in/débora-mandon" target="_blank" style='text-decoration:none;'>💼 LinkedIn</a><br>
    <a href="https://github.com/DeboraMandon" target="_blank" style='text-decoration:none;'>💻 GitHub</a>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    try:
        with open("assets/CV_DMA_DE.pdf", "rb") as pdf:
            st.download_button(
                label="📄 Télécharger le CV",
                data=pdf,
                file_name="CV_Debora_Mandon.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    except FileNotFoundError:
        st.warning("CV PDF non trouvé dans assets/")

# ---------------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------------

main_page = st.Page("page0.py", title="Accueil",          icon="🏠")
page_1    = st.Page("page1.py", title="Profil",            icon="👤")
page_2    = st.Page("page2.py", title="Expériences",       icon="💼")
page_3    = st.Page("page3.py", title="Projets",           icon="🏗️")
page_4    = st.Page("page4.py", title="Contact",           icon="📲")
page_5    = st.Page("page5.py", title="Démo monitoring",   icon="📊")

pg = st.navigation([main_page, page_1, page_2, page_3, page_4, page_5])
pg.run()
