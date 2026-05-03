import streamlit as st
import sqlite3
from datetime import datetime
from contextlib import contextmanager
import pandas as pd

st.set_page_config(layout="wide")

st.markdown("""
<style>
.contact-row {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 0.9rem;
    margin-bottom: 8px;
}
.contact-row a {
    color: #403EBB;
    text-decoration: none;
    font-weight: 500;
}
.contact-row a:hover { text-decoration: underline; }
@media (prefers-color-scheme: dark) {
    .contact-row a { color: #A8B2FF !important; }
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# DB
# ---------------------------------------------------------------

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

# ---------------------------------------------------------------
# HEADER
# ---------------------------------------------------------------

st.markdown("<h1 style='text-align:center;'>Contact</h1>", unsafe_allow_html=True)
st.markdown("<div style='height:24px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------------
# LAYOUT : infos gauche | formulaire droite
# ---------------------------------------------------------------

col_info, col_form = st.columns([1, 2], gap="large")

with col_info:
    st.markdown("#### Me retrouver")
    st.markdown("""
<div class='contact-row'>📧 <a href='mailto:debora.mandon@biir.fr'>debora.mandon@biir.fr</a></div>
<div class='contact-row'>📱 <a href='tel:0640222354'>06 40 22 23 54</a></div>
<div class='contact-row'>💼 <a href='https://www.linkedin.com/in/débora-mandon' target='_blank'>LinkedIn</a></div>
<div class='contact-row'>💻 <a href='https://github.com/DeboraMandon' target='_blank'>GitHub</a></div>
""", unsafe_allow_html=True)

with col_form:
    st.markdown("#### Laisser un message")
    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Nom")
        with c2:
            email = st.text_input("E-mail")
        message = st.text_area("Message", placeholder="Bonjour, je suis intéressé(e) par...", height=130)
        submit = st.form_submit_button("Envoyer", use_container_width=True)
        if submit:
            if name and email and message:
                save_message(name, email, message)
                st.success("✅ Message envoyé, merci !")
            else:
                st.warning("Merci de remplir tous les champs.")

st.markdown("<div style='height:32px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# ADMIN
# ---------------------------------------------------------------

if "admin_authenticated" not in st.session_state:
    st.session_state.admin_authenticated = False

if not st.session_state.admin_authenticated:
    with st.expander("🔐 Espace admin"):
        admin_password = st.text_input("Mot de passe", type="password", label_visibility="collapsed")
        if st.button("Accéder", type="secondary"):
            try:
                if admin_password == st.secrets["admin"]["password"]:
                    st.session_state.admin_authenticated = True
                    st.rerun()
                else:
                    st.error("Mot de passe incorrect")
            except KeyError:
                st.error("Secret 'admin.password' non configuré.")
else:
    with st.expander("🔓 Espace admin — ouvert", expanded=True):
        if st.button("Fermer la session", type="secondary"):
            st.session_state.admin_authenticated = False
            st.rerun()

        try:
            with get_db() as conn:
                df = pd.read_sql("""
                    SELECT date, name, email,
                           SUBSTR(message, 1, 100) as aperçu
                    FROM messages ORDER BY date DESC LIMIT 50
                """, conn)
            if df.empty:
                st.info("Aucun message pour le moment.")
            else:
                st.dataframe(df, use_container_width=True, hide_index=True)
                current_month = datetime.now().strftime("%Y-%m")
                c1, c2 = st.columns(2)
                c1.metric("Messages totaux", len(df))
                c2.metric("Ce mois", len(df[df.date.str.startswith(current_month)]))
                csv = df.to_csv(index=False, encoding="utf-8")
                st.download_button("💾 Exporter CSV", csv, "messages_contact.csv", "text/csv")
        except Exception as e:
            st.error(f"Erreur lecture DB : {e}")

st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
