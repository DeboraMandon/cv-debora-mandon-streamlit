import streamlit as st
import sqlite3
from datetime import datetime

st.set_page_config(layout="wide")

# -----------------------------------
# STYLE
# -----------------------------------
st.markdown("""
<style>

.contact-card {
    border: 1px solid #e6e6e6;
    padding: 25px;
    border-radius: 12px;
    background: #fafafa;
    width: 70%;
    margin: auto;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.06);
}

.contact-title {
    text-align: center;
    font-size: 2.4rem;  /* Était 1.8rem → maintenant 2.4rem */
    font-weight: 700;
    color: #403EBB;
    margin-bottom: 5px;
    line-height: 1.2;  /* Améliore lisibilité */
}

@media (prefers-color-scheme: dark) {
    .contact-title { 
        color: #A8B2FF !important; 
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);  /* Ombre subtile dark */
    }
}

.contact-sub {
    text-align: center;
    font-size: 1rem;
    color: #e6e6e6;
    margin-bottom: 25px;
}

.contact-line {
    font-size: 1.1rem;
    margin-bottom: 12px;
}

.contact-icon {
    font-size: 1.3rem;
    margin-right: 10px;
}

.contact-link a {
    color: #403EBB;
    font-weight: 600;
    text-decoration: none;
    transition: 0.2s;
}

.contact-link a:hover {
    color: #6B69FF;
    text-decoration: underline;
}

.form-input {
    background-color: white;
    border-radius: 8px;
}

/* AJOUTER à votre CSS existant */
@media (prefers-color-scheme: dark) {
    .contact-card {
        background: #1e1e1e !important;
        border-color: #444 !important;
        color: #e0e0e0 !important;
    }
    .contact-title { color: #A8B2FF !important; }
    .contact-sub { color: #888 !important; }
    .contact-link a { color: #A8B2FF !important; }
    .contact-link a:hover { color: #C0C0FF !important; }
}

.contact-line {
    display: flex;
    align-items: center;
    font-size: 1.1rem;
    margin-bottom: 15px;
}
/* Centre le texte des st.page_link dans la page FUN/Contact/etc. */
a[data-testid="stPageLink"] {
    text-align: center !important;
    justify-content: center !important;
}
</style>
""", unsafe_allow_html=True)

def save_message(name, email, message):
    conn = sqlite3.connect("contact.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    """)
    c.execute("INSERT INTO messages (date, name, email, message) VALUES (?, ?, ?, ?)",
              (datetime.now().isoformat(), name, email, message))
    conn.commit()
    conn.close()
    
# -----------------------------------
# HEADER
# -----------------------------------
st.markdown("<h1 style='text-align:center;'>Contact</h1>", unsafe_allow_html=True)
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# -----------------------------------
# CONTACT CARD
# -----------------------------------

st.markdown("<p class='contact-title'>Entrer en contact avec moi</p>", unsafe_allow_html=True)
st.markdown("<p class='contact-sub'>Je réponds rapidement sur mes canaux professionnels</p>", unsafe_allow_html=True)

st.markdown(
    """
    <div class='contact-line contact-link'>
        <span class='contact-icon'>📧</span>
        <a href="mailto:debora.mandon@biiir.com">debora.mandon@biiir.com</a>
    </div>

    <div class='contact-line contact-link'>
        <span class='contact-icon'>💼</span>
        <a href="https://www.linkedin.com/in/débora-mandon" target="_blank">
            LinkedIn - Profil professionnel
        </a>
    </div>

    <div class='contact-line contact-link'>
        <span class='contact-icon'>💻</span>
        <a href="https://github.com/DeboraMandon" target="_blank">
            GitHub - Projets & code
        </a>
    </div>
    <div class='contact-line contact-link'>
        <span class='contact-icon'>📱</span>
        <a href="tel:0640222354">06 40 22 23 54</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")


# FORMULAIRE:

st.subheader("💬 Me laisser un message")
with st.form("contact_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1: name = st.text_input("Votre nom")
    with col2: email = st.text_input("Votre e-mail", help="Format: nom@exemple.com")
    message = st.text_area("Votre message", placeholder="Bonjour, je suis intéressé(e) par...")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        submit = st.form_submit_button("🚀 Envoyer", use_container_width=True, type="primary")
    
    if submit:
        save_message(name, email, message)
        st.success("✅ Merci ! Votre message a été enregistré.")
        st.balloons()  # Effet festif !
        
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ----------------------------------------------
# CTA SECTION AVEC BOUTON "changement de pages"
# ----------------------------------------------

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

btn_col1, btn_col2 = st.columns([2, 2])

with btn_col1:
    if st.button("⬅️ Revenir aux Projets 🏗️", use_container_width=True):
        st.switch_page("page3.py")

with btn_col2:
    if st.button("🌈 Aller à la section Démo monitoring ➡️", use_container_width=True):
        st.switch_page("page5.py")


# ----------------------------------------------
# BOUTON ACCUEIL
# ----------------------------------------------

left, center, right = st.columns([7,2,7])

with center:
    st.page_link(
        "page0.py",
        label="🏠 Accueil",
        use_container_width=True
    )
