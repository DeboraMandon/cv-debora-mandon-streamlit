import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from contextlib import contextmanager

st.set_page_config(layout="wide", page_title="Pipeline Monitoring – Débora Mandon")

st.markdown("""
<style>
a[data-testid="stPageLink"] {
    text-align: center !important;
    justify-content: center !important;
}
.metric-label { font-size: 0.85rem; color: #888; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# DONNÉES PRÉ-AGRÉGÉES — source : Olist Brazil E-Commerce Dataset
# (Kaggle, 99 441 commandes, sept. 2016 – oct. 2018)
# ---------------------------------------------------------------

# Latences médianes par mois (commandes livrées uniquement, jan 2017 – août 2018)
LATENCY_RAW = [
    ("2017-01", 0.29, 42.81, 171.45, 0.969, 750),
    ("2017-02", 0.23, 44.83, 175.53, 0.968, 1653),
    ("2017-03", 0.12, 43.45, 169.07, 0.944, 2546),
    ("2017-04", 0.24, 47.20, 213.60, 0.921, 2303),
    ("2017-05", 0.24, 38.12, 168.75, 0.964, 3546),
    ("2017-06", 0.24, 38.14, 166.49, 0.945, 3478),
    ("2017-07", 0.24, 38.46, 161.32, 0.951, 4094),
    ("2017-08", 0.23, 36.95, 158.67, 0.961, 5196),
    ("2017-09", 0.24, 37.68, 159.48, 0.958, 4671),
    ("2017-10", 0.23, 40.41, 165.28, 0.944, 6096),
    ("2017-11", 0.26, 46.38, 181.53, 0.904, 8084),
    ("2017-12", 0.28, 45.21, 172.34, 0.935, 6029),
    ("2018-01", 0.27, 43.86, 168.92, 0.951, 7448),
    ("2018-02", 0.25, 42.54, 165.43, 0.960, 6875),
    ("2018-03", 0.26, 44.12, 171.28, 0.948, 7862),
    ("2018-04", 0.24, 43.28, 169.74, 0.955, 6981),
    ("2018-05", 0.25, 42.97, 167.83, 0.958, 7483),
    ("2018-06", 0.26, 44.51, 172.18, 0.943, 6524),
    ("2018-07", 0.27, 45.23, 174.36, 0.937, 6983),
    ("2018-08", 0.28, 46.14, 176.52, 0.931, 5512),
]

df_latency = pd.DataFrame(LATENCY_RAW, columns=[
    "month", "approval_h", "carrier_h", "last_mile_h", "on_time_rate", "orders_count"
])
df_latency["month_dt"] = pd.to_datetime(df_latency["month"])

# Funnel des statuts (total dataset)
FUNNEL_RAW = [
    ("delivered",   96478),
    ("shipped",      1107),
    ("canceled",      625),
    ("unavailable",   609),
    ("invoiced",      314),
    ("processing",    301),
    ("created",         5),
    ("approved",        2),
]
df_funnel = pd.DataFrame(FUNNEL_RAW, columns=["status", "count"])

# ---------------------------------------------------------------
# HEADER
# ---------------------------------------------------------------

st.markdown(
    "<h1 style='text-align:center;'>📦 Pipeline Monitoring — Olist E-Commerce</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; color:#888;'>"
    "Analyse de 99 441 commandes · Olist Brazil · sept. 2016 – oct. 2018 · "
    "<a href='https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce' target='_blank'>source Kaggle</a>"
    "</p>",
    unsafe_allow_html=True
)
st.markdown("---")

# ---------------------------------------------------------------
# KPI GLOBAUX
# ---------------------------------------------------------------

total_orders   = 99441
delivered      = 96478
on_time_global = df_latency["on_time_rate"].mean()
median_total_h = (
    df_latency["approval_h"].median()
    + df_latency["carrier_h"].median()
    + df_latency["last_mile_h"].median()
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Commandes totales",  f"{total_orders:,}".replace(",", " "))
c2.metric("Taux de livraison",  f"{delivered/total_orders:.1%}")
c3.metric("Livraisons à temps", f"{on_time_global:.1%}")
c4.metric("Durée médiane totale", f"{median_total_h/24:.1f} j")

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# VOLUME MENSUEL + TAUX ON-TIME
# ---------------------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Volume de commandes livrées / mois")
    fig_vol = px.bar(
        df_latency, x="month", y="orders_count",
        color_discrete_sequence=["#403EBB"],
        labels={"month": "", "orders_count": "Commandes livrées"},
    )
    fig_vol.update_layout(margin=dict(t=20, b=0), height=320)
    st.plotly_chart(fig_vol, use_container_width=True)

with col2:
    st.subheader("✅ Taux de livraison à temps")
    fig_ot = px.line(
        df_latency, x="month_dt", y="on_time_rate",
        markers=True,
        color_discrete_sequence=["#2ecc71"],
        labels={"month_dt": "", "on_time_rate": "% à temps"},
    )
    fig_ot.update_layout(
        yaxis_tickformat=".0%",
        yaxis_range=[0.88, 1.0],
        margin=dict(t=20, b=0),
        height=320
    )
    fig_ot.add_hline(
        y=0.95, line_dash="dash", line_color="orange",
        annotation_text="Seuil SLA 95%", annotation_position="bottom right"
    )
    st.plotly_chart(fig_ot, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------------
# LATENCES PIPELINE — 3 ÉTAPES
# ---------------------------------------------------------------

st.subheader("⏱️ Latences médianes par étape du pipeline (heures)")

st.caption(
    "**Achat → Approbation** : validation de paiement  |  "
    "**Approbation → Transporteur** : préparation & expédition  |  "
    "**Transporteur → Client** : last mile"
)

df_melt = df_latency.melt(
    id_vars=["month_dt"],
    value_vars=["approval_h", "carrier_h", "last_mile_h"],
    var_name="étape", value_name="heures"
)
df_melt["étape"] = df_melt["étape"].map({
    "approval_h":   "1. Achat → Approbation",
    "carrier_h":    "2. Approbation → Transporteur",
    "last_mile_h":  "3. Transporteur → Client (last mile)",
})

fig_lat = px.line(
    df_melt, x="month_dt", y="heures", color="étape",
    markers=False,
    color_discrete_sequence=["#403EBB", "#F39C12", "#E74C3C"],
    labels={"month_dt": "", "heures": "Heures (médiane)", "étape": "Étape"},
)
fig_lat.update_layout(
    height=360,
    margin=dict(t=10, b=0),
    legend=dict(orientation="h", yanchor="bottom", y=1.02)
)
st.plotly_chart(fig_lat, use_container_width=True)

# Encadré insight
with st.expander("💡 Lecture du graphique"):
    st.markdown("""
    - **L'approbation de paiement** (~0,25h) est quasi-instantanée : étape automatisée, aucun bottleneck.
    - **La préparation/expédition** (~40–47h) est l'étape à surveiller : pic visible en **nov. 2017** (Black Friday brésilien).
    - **Le last mile** (~160–215h, soit 7–9 jours) est la plus longue : logistique physique, peu compressible.
    - Le pic d'avril 2017 sur le last mile (~214h) est une anomalie à investiguer (données moins denses sur cette période).
    """)

st.markdown("---")

# ---------------------------------------------------------------
# FUNNEL STATUTS
# ---------------------------------------------------------------

col3, col4 = st.columns([1, 1])

with col3:
    st.subheader("🔽 Funnel des statuts de commande")
    fig_funnel = go.Figure(go.Funnel(
        y=df_funnel["status"],
        x=df_funnel["count"],
        textinfo="value+percent initial",
        marker=dict(color=[
            "#2ecc71","#3498db","#e74c3c","#95a5a6",
            "#f39c12","#9b59b6","#1abc9c","#e67e22"
        ])
    ))
    fig_funnel.update_layout(height=380, margin=dict(t=10, b=0))
    st.plotly_chart(fig_funnel, use_container_width=True)

with col4:
    st.subheader("📊 Répartition des statuts")
    fig_pie = px.pie(
        df_funnel[df_funnel["count"] > 10],
        names="status", values="count",
        color_discrete_sequence=px.colors.qualitative.Set2,
        hole=0.4
    )
    fig_pie.update_layout(height=380, margin=dict(t=10, b=0))
    fig_pie.update_traces(textposition="inside", textinfo="percent+label")
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------------
# TABLEAU RÉCAPITULATIF
# ---------------------------------------------------------------

st.subheader("📋 Données mensuelles détaillées")

df_display = df_latency[["month","orders_count","approval_h","carrier_h","last_mile_h","on_time_rate"]].copy()
df_display.columns = ["Mois","Commandes","Approbation (h)","Expédition (h)","Last mile (h)","Taux à temps"]
df_display["Taux à temps"] = df_display["Taux à temps"].map("{:.1%}".format)
df_display["Approbation (h)"] = df_display["Approbation (h)"].round(2)
df_display["Expédition (h)"] = df_display["Expédition (h)"].round(1)
df_display["Last mile (h)"] = df_display["Last mile (h)"].round(1)

st.dataframe(df_display, use_container_width=True, hide_index=True)

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------------

if st.button("⬅️ Revenir au Contact 📲"):
    st.switch_page("page4.py")

left, center, right = st.columns([7, 2, 7])
with center:
    st.page_link("page0.py", label="🏠 Accueil", use_container_width=True)
