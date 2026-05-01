import streamlit as st
import sqlite3
from datetime import datetime
from contextlib import contextmanager
import pandas as pd

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
    font-size: 2.4rem;
    font-weight: 700;
    color: #403EBB;
    margin-bottom: 5px;
    line-height: 1.2;
}
@media (prefers-color-scheme: dark) {
    .contact-title {
        color: #A8B2FF !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
}
.contact-sub {
    text-align: center;
    font-size: 1rem;
    color: #e6e6e6;
    margin-bottom: 25px;
}
.contact-line {
    display: flex;
    align-items: center;
    font-size: 1.1rem;
    margin-bottom: 15px;
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
a[data-testid="stPageLink"] {
    text-align: center !important;
    justify-content: center !important;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------------
# DB — context manager (pattern page5)
# -----------------------------------

@contextmanager
def get_db():
    conn = sqlite3.connect("contact.db", check_same_thread=False)
    try:
        yield conn
    finally:
        conn.close()


def init_contact_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                date    TEXT,
                name    TEXT,
                email   TEXT,
                message TEXT
            )
        """)
        conn.commit()


def save_message(name, email, message):
    with get_db() as conn:
        conn.execute(
            "INSERT INTO messages (date, name, email, message) VALUES (?, ?, ?, ?)",
            (datetime.now().isoformat(), name, email, message)
        )
        conn.commit()


init_contact_db()


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
        <a href="mailto:debora.mandon@biir.fr">debora.mandon@biir.fr</a>
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

# -----------------------------------
# FORMULAIRE
# -----------------------------------

st.subheader("💬 Me laisser un message")

with st.form("contact_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Votre nom")
    with col2:
        email = st.text_input("Votre e-mail", help="Format: nom@exemple.com")

    message = st.text_area("Votre message", placeholder="Bonjour, je suis intéressé(e) par...")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submit = st.form_submit_button("🚀 Envoyer", use_container_width=True, type="primary")

    if submit:
        save_message(name, email, message)
        st.success("✅ Merci ! Votre message a été enregistré.")
        st.balloons()

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# -----------------------------------
# NAVIGATION
# -----------------------------------

btn_col1, btn_col2 = st.columns([2, 2])
with btn_col1:
    if st.button("⬅️ Revenir aux Projets 🏗️", use_container_width=True):
        st.switch_page("page3.py")
with btn_col2:
    if st.button("🌈 Aller à la section Démo monitoring ➡️", use_container_width=True):
        st.switch_page("page5.py")

left, center, right = st.columns([7, 2, 7])
with center:
    st.page_link("page0.py", label="🏠 Accueil", use_container_width=True)

# -----------------------------------
# ADMIN — protégé par st.secrets
# -----------------------------------

st.markdown("---")

if "admin_authenticated" not in st.session_state:
    st.session_state.admin_authenticated = False

if not st.session_state.admin_authenticated:
    admin_password = st.text_input("🔐 Mot de passe admin", type="password")
    if st.button("👁️ Voir les messages", type="secondary"):
        try:
            correct_password = st.secrets["admin"]["password"]
        except KeyError:
            st.error("⚠️ Secret 'admin.password' non configuré dans Streamlit Secrets.")
            st.stop()

        if admin_password == correct_password:
            st.session_state.admin_authenticated = True
            st.success("✅ Accès admin autorisé !")
            st.rerun()
        else:
            st.error("❌ Mot de passe incorrect")
else:
    st.success("🔓 Mode admin activé")
    if st.button("🔒 Fermer session admin", type="secondary"):
        st.session_state.admin_authenticated = False
        st.rerun()

    st.markdown("---")
    st.subheader("📬 Messages reçus")

    try:
        with get_db() as conn:
            df = pd.read_sql("""
                SELECT
                    date,
                    name,
                    email,
                    length(message) as nb_car,
                    SUBSTR(message, 1, 100) as preview
                FROM messages
                ORDER BY date DESC
                LIMIT 50
            """, conn)

        if df.empty:
            st.info("✨ Aucun message pour le moment.")
        else:
            st.dataframe(df, use_container_width=True, hide_index=True)

            col1, col2, col3 = st.columns(3)
            current_month = datetime.now().strftime("%Y-%m")
            with col1:
                st.metric("Messages totaux", len(df))
            with col2:
                st.metric("Ce mois", len(df[df.date.str.startswith(current_month)]))
            with col3:
                st.metric("Non lus", "0")

            csv = df.to_csv(index=False, encoding="utf-8")
            st.download_button("💾 Exporter CSV", csv, "messages_contact.csv", "text/csv")

    except Exception as e:
        st.error(f"❌ Erreur lecture DB : {e}")
