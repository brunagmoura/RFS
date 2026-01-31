
import streamlit as st
import plotly.graph_objects as go

# Configuração da Página
st.set_page_config(page_title="Regime Fiscal Sustentável", layout="wide")

st.title("🏛️ Regime Fiscal Sustentável (LC 200/2023)")
st.markdown("### Simulador de Limite de Despesas")

# Colunas para Inputs
col1, col2 = st.columns(2)

with col1:
    receita_growth = st.slider(
        "Crescimento Real da Receita (%)", 
        min_value=-2.0, 
        max_value=6.0, 
        value=2.0, 
        step=0.1
    )

with col2:
    meta_cumprida = st.checkbox(
        "Meta Fiscal do ano anterior cumprida?", 
        value=True,
        help="Se a meta for cumprida, o limite é 70% da receita. Se não, cai para 50%."
    )

# Lógica de Cálculo (Regra do Arcabouço)
fator = 0.70 if meta_cumprida else 0.50
crescimento_calculado = receita_growth * fator

# Aplicação do Piso (0.6%) e Teto (2.5%)
limite_final = max(0.6, min(crescimento_calculado, 2.5))

# Determinação da cor do resultado
cor_barra = "#3b82f6"  # Blue
if limite_final == 0.6:
    status_msg = "Travado no Piso (0.6%)"
    cor_barra = "#ef4444"  # Red
elif limite_final == 2.5:
    status_msg = "Travado no Teto (2.5%)"
    cor_barra = "#10b981"  # Green
else:
    status_msg = f"Calculado ({int(fator*100)}% da Receita)"

# Exibição de Métricas
st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("Fator de Ajuste", f"{int(fator*100)}%", delta="Baseado na Meta")
c2.metric("Crescimento Calculado", f"{crescimento_calculado:.2f}%", help="Antes do Piso/Teto")
c3.metric("Limite Final Aplicável", f"{limite_final:.2f}%", delta=status_msg)

# Visualização Gráfica (Plotly)
fig = go.Figure()

# Barra de fundo (Range total visual)
fig.add_trace(go.Bar(
    y=['Limite'], x=[3.0], orientation='h', 
    marker_color='#e2e8f0', hoverinfo='none'
))

# Barra do Valor Real
fig.add_trace(go.Bar(
    y=['Limite'], x=[limite_final], orientation='h',
    marker_color=cor_barra, text=f"{limite_final:.2f}%", textposition='auto',
    name='Crescimento Permitido'
))

# Linhas de Piso e Teto
fig.add_vline(x=0.6, line_width=2, line_dash="dash", line_color="gray", annotation_text="Piso 0.6%")
fig.add_vline(x=2.5, line_width=2, line_dash="dash", line_color="gray", annotation_text="Teto 2.5%")

fig.update_layout(
    title="Visualização do Espaço Fiscal",
    xaxis=dict(range=[0, 3.5], title="Crescimento Real (%)"),
    barmode='overlay',
    height=250,
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

st.info("Nota: Este cálculo refere-se ao Art. 5º da LC 200/2023. Exceções constitucionais (Art. 3º) não entram neste limite.")
                
