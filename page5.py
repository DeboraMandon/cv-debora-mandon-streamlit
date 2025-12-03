import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import numpy as np
from datetime import datetime
from contextlib import contextmanager

st.set_page_config(layout="wide", page_title="Pipeline Monitoring - Débora Mandon")


# -----------------------------------
# CONFIG DB
# -----------------------------------
@contextmanager
def get_db():
    """Context manager : nouvelle connexion à chaque fois"""
    conn = sqlite3.connect('pipelines.db', check_same_thread=False)
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS pipeline_runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pipeline_name TEXT,
                status TEXT,
                duration_ms INTEGER,
                records_processed INTEGER,
                error_rate REAL,
                run_time DATETIME
            )
        ''')
        # Données exemple
        conn.execute('SELECT COUNT(*) FROM pipeline_runs').fetchone()[0] or conn.executemany('''
            INSERT INTO pipeline_runs VALUES (NULL, ?, ?, ?, ?, ?, ?)
        ''', [
            ('Azure_Stream_Analytics', 'SUCCESS', 2450, 12500, 0.01, '2025-12-03 08:00:00'),
            ('NodeRED_FlowFuse', 'SUCCESS', 3890, 45000, 0.02, '2025-12-03 07:45:00'),
            ('PowerBI_ETL', 'WARNING', 8920, 89000, 0.045, '2025-12-03 07:30:00'),
            ('Talend_Migration', 'FAILED', 15400, 120000, 0.12, '2025-12-03 07:15:00')
        ])
        conn.commit()

def add_pipeline_run():
    pipelines = ['Azure_Stream_Analytics', 'NodeRED_FlowFuse', 'PowerBI_ETL', 'Talend_Migration']
    statuses = ['SUCCESS', 'SUCCESS', 'WARNING', 'FAILED']
    data = {
        'pipeline_name': np.random.choice(pipelines),
        'status': np.random.choice(statuses, p=[0.7, 0.2, 0.08, 0.02]),
        'duration_ms': np.random.randint(1500, 15000),
        'records_processed': np.random.randint(1000, 100000),
        'error_rate': np.random.uniform(0, 0.05),
        'run_time': datetime.now()
    }
    with get_db() as conn:
        conn.execute('''
            INSERT INTO pipeline_runs (pipeline_name, status, duration_ms, records_processed, error_rate, run_time)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (data['pipeline_name'], data['status'], data['duration_ms'], 
              data['records_processed'], data['error_rate'], data['run_time']))
        conn.commit()

def get_data(_=None):
    with get_db() as conn:
        return pd.read_sql('SELECT * FROM pipeline_runs ORDER BY run_time DESC LIMIT 1000', conn)

# -----------------------------------
# INIT DB
# -----------------------------------

init_db()

st.markdown("<h1 style='text-align:center;'>🚀 Pipeline Monitoring Live - Débora Mandon</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Azure • Node-RED • ETL • Monitoring</h3>", unsafe_allow_html=True)
st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
st.markdown("---")

if st.button("🔄 Simuler nouveau run pipeline", type="secondary"):
    add_pipeline_run()
    st.success("✅ Pipeline run ajouté !")
    st.rerun()

df = get_data()

if len(df) == 0:
    st.info("👆 Cliquez 'Simuler nouveau run' pour commencer !")
    st.stop()

# -----------------------------------
# DASHBOARD
# -----------------------------------
# Métriques
st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

metrics_container = st.container()

with metrics_container:
    col1, col2, col3 = st.columns(3)
    col1.metric("Runs total", len(df))
    success_rate = len(df[df.status=='SUCCESS']) / len(df)
    col2.metric("Success Rate", f"{success_rate:.1%}")
    col3.metric("Avg Duration", f"{df.duration_ms.mean():.0f}ms")

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# Graphiques
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(px.pie(df.tail(20), names='status', title="Status récents"), use_container_width=True)
with col2:
    st.plotly_chart(px.bar(df.nlargest(10, 'duration_ms'), x='pipeline_name', y='duration_ms', 
                          color='status', title="Top Durées"), use_container_width=True)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("📈 Évolution temporelle")
st.plotly_chart(px.line(df.tail(50).sort_values('run_time'), x='run_time', y='duration_ms', 
                       color='status'), use_container_width=True)

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("📋 Derniers runs")
st.dataframe(df[['pipeline_name', 'status', 'duration_ms', 'records_processed', 'run_time']].tail(20))

st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)
st.markdown("---")

# ----------------------------------------------
# CTA SECTION AVEC BOUTON "changement de pages"
# ----------------------------------------------

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

if st.button("⬅️ Revenir au Contact 📲"):
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
