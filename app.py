################################################################################################
#        pour lancer l'application Streamlit                                                   #
#        dans un terminal se placer dans le répertoire                                         #
#        cd C:\99_PERSO\Streamlit\Projet_CV                                                    #
#        lancer streamlit: streamlit run app.py                                          #
#        streamlit démarre un petit serveur local sur : http://localhost:8501                  #
#        pour arrêter l'app dans le terminal faire : Ctrl+C                                    #
################################################################################################

import streamlit as st
from pathlib import Path


# Define the pages
main_page = st.Page("page0.py", title="Accueil", icon="🎈")
page_1 = st.Page("page1.py", title="Profil", icon="❄️")
page_2 = st.Page("page2.py", title="Experiences", icon="🎉")
page_3 = st.Page("page3.py", title="Projet", icon="🏗️")
page_4 = st.Page("page4.py", title="Contact", icon="📲")
page_5 = st.Page("page5.py", title="Démo monitoring", icon="🌈")

# Set up navigation
pg = st.navigation([main_page, page_1, page_2, page_3, page_4, page_5])

# Run the selected page
pg.run()

# Barre latérale
with st.sidebar:
    st.image("assets/photo.png", width=150)
    st.markdown("### Débora Mandon")
    st.markdown("Consultante Data")
    st.markdown("---")
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/débora-mandon)")
    st.markdown("[💻 GitHub](https://github.com/DeboraMandon)")
    st.markdown("---")
    st.subheader("📄 Télécharger mon CV")
    with open("assets/CV_Debora_Mandon_DE.pdf", "rb") as pdf:
        st.download_button(
            "Télécharger le CV PDF",
            data=pdf,
            file_name="CV_Debora_Mandon_DE.pdf",
            mime="application/pdf"
    )



