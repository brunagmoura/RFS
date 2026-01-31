import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuração da Página
st.set_page_config(page_title="Painel Fiscal - Tesouro Nacional", layout="wide")

# Estilo CSS Personalizado (Azul e Cinza)
st.markdown("""
    <style>
    .main {background-color: #f8fafc;}
    h1, h2, h3 {color: #1e3a8a;}
    .metric-card {background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-left: 5px solid #1e3a8a;}
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Painel Regime Fiscal Sustentável")
st.markdown("Dados consolidados: Comparativo 2024, 2025 e projeções 2026")

# --- Dados ---
data_result = {
    'Ano': ['2024', '2025'],
    'Nominal': [-43.0, -61.7],
    'Ajustado': [-11.0, -13.0]
}
df_result = pd.DataFrame(data_result)

data_rap = {
    'Ano': ['2024', '2025', '2026'],
    'Estoque_RAP': [285.5, 312.5, 391.5]
}
df_rap = pd.DataFrame(data_rap)

# --- Métricas Principais ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Resultado Primário 2025 (Nominal)", "R$ -61,7 Bi", "-18,7 Bi vs 2024")
with col2:
    st.metric("Resultado Ajustado (p/ Meta)", "R$ -13,0 Bi", "Dentro da Banda")
with col3:
    st.metric("Estoque Restos a Pagar 2026", "R$ 391,5 Bi", "+25,3%")

st.divider()

# --- Gráficos ---
col_g1, col_g2 = st.columns(2)

with col_g1:
    st.subheader("Resultado Nominal vs. Ajustado")
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=df_result['Ano'], y=df_result['Nominal'],
        name='Nominal (Real)', marker_color='#94a3b8', text=df_result['Nominal'], textposition='auto'
    ))
    fig1.add_trace(go.Bar(
        x=df_result['Ano'], y=df_result['Ajustado'],
        name='Ajustado (Meta)', marker_color='#1e3a8a', text=df_result['Ajustado'], textposition='auto'
    ))
    fig1.update_layout(barmode='group', template='plotly_white', legend=dict(orientation="h", y=1.1))
    st.plotly_chart(fig1, use_container_width=True)

with col_g2:
    st.subheader("Evolução do Estoque de RAP")
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=df_rap['Ano'], y=df_rap['Estoque_RAP'],
        marker_color=['#cbd5e1', '#64748b', '#0f172a'],
        text=df_rap['Estoque_RAP'], textposition='outside'
    ))
    fig2.update_layout(template='plotly_white', yaxis_title="R$ Bilhões")
    st.plotly_chart(fig2, use_container_width=True)

# --- Exceções ---
st.subheader("Detalhamento das Exceções à Meta")
st.info("Valores excluídos para fins de cumprimento da meta de resultado primário.")

df_excecoes = pd.DataFrame({
    "Categoria": ["Calamidade RS", "Precatórios (>Limite)", "Projetos Defesa/Outros"],
    "2024 (R$ Bi)": ["31.8", "-", "0.1"],
    "2025 (R$ Bi)": ["-", "41.1", "7.5"]
})
st.table(df_excecoes)
                    
