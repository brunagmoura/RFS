import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- Configuração da Página ---
st.set_page_config(
    page_title="Regime Fiscal Sustentável - CGU/Tesouro",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS Personalizado para Estilização (Réplica do Layout) ---
st.markdown("""
<style>
    /* Cabeçalho Azul Escuro */
    .main-header {
        background-color: #0E1E45;
        padding: 20px;
        border-radius: 5px;
        color: white;
        margin-bottom: 20px;
    }
    .main-header h1 {
        color: white;
        font-size: 28px;
        margin: 0;
    }
    .main-header h3 {
        color: #A0C4FF;
        font-size: 16px;
        margin: 0;
        font-weight: 300;
    }
    
    /* Estilo dos Cards (Bordas arredondadas e sombra leve) */
    div.css-1r6slb0 {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    
    /* Métricas Customizadas */
    .metric-card {
        background-color: #2E4078; /* Azul Escuro do Print 3 */
        color: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
    }
    .metric-label {
        font-size: 12px;
        text-transform: uppercase;
        opacity: 0.8;
    }
    .status-badge {
        background-color: #2ca02c; /* Verde Sucesso */
        color: white;
        padding: 5px 10px;
        border-radius: 15px;
        font-weight: bold;
        display: inline-block;
    }
    
    /* Ajuste de abas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: white;
        border-radius: 5px;
        color: #444;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #F0F2F6;
        color: #0E1E45;
        border-bottom: 2px solid #0E1E45;
    }
</style>
""", unsafe_allow_html=True)

# --- Cabeçalho Principal (Print 1) ---
st.markdown("""
<div class="main-header">
    <h1>Regime Fiscal Sustentável</h1>
    <h3>SECRETARIA DO TESOURO NACIONAL • LC 200/2023</h3>
    <div style="text-align: right; font-size: 12px; margin-top: -30px;">
        Atualização<br><strong>Dezembro 2025</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Navegação por Abas ---
tab1, tab2, tab3, tab4 = st.tabs(["Os Três Pilares", "Limite vs. Meta", "Resultados 2024-2026", "<> Código Streamlit"])

# ==============================================================================
# ABA 1: OS TRÊS PILARES (Réplica do Print 1)
# ==============================================================================
with tab1:
    st.markdown("<h2 style='text-align: center;'>A Estrutura da Lei Complementar 200/2023</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>O novo arcabouço fiscal busca garantir a sustentabilidade da dívida pública conciliando responsabilidade fiscal com flexibilidade para investimentos.</p><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("**1. Metas de Resultado Primário**")
        st.markdown("""
        Compromisso com trajetórias de saldo primário (receitas - despesas) compatíveis com a estabilização da dívida. Possui uma **banda de tolerância** de ±0,25% do PIB.
        
        <br><small style='background-color:#F0F2F6; padding:5px; border-radius:5px;'>**Objetivo:** Solvência e credibilidade fiscal.</small>
        """, unsafe_allow_html=True)

    with col2:
        st.info("**2. Limite de Crescimento de Gastos**")
        st.markdown("""
        A despesa real só pode crescer atrelada à receita (70% do crescimento da receita real). Possui um **piso de 0,6%** e um **teto de 2,5%** de crescimento real ao ano.
        
        <br><small style='background-color:#F0F2F6; padding:5px; border-radius:5px;'>**Objetivo:** Controle da expansão do estado (anticíclico).</small>
        """, unsafe_allow_html=True)

    with col3:
        st.info("**3. Gatilhos e Ajustes**")
        st.markdown("""
        Mecanismos de correção automática. Se a meta não for cumprida, o crescimento permitido de gastos cai para **50%** da receita. Vedações (ex: concursos) são acionadas em casos extremos.
        
        <br><small style='background-color:#F0F2F6; padding:5px; border-radius:5px;'>**Objetivo:** Incentivo ao cumprimento e correção de rota.</small>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><div style='text-align:center'><button style='background-color:#0b5ed7; color:white; border:none; padding:10px 20px; border-radius:20px;'>Continuar esta conversa</button></div>", unsafe_allow_html=True)


# ==============================================================================
# ABA 2: LIMITE VS. META (Réplica do Print 2)
# ==============================================================================
with tab2:
    st.markdown("<h3 style='text-align: center; margin-bottom: 30px;'>Limite de Gastos vs. Meta de Primário</h3>", unsafe_allow_html=True)
    
    col_lim, col_meta = st.columns(2)
    
    with col_lim:
        st.markdown("#### 🔒 Limite de Gastos")
        st.write("Define o **teto máximo** que a despesa pode crescer de um ano para o outro, independentemente da arrecadação extraordinária.")
        with st.container(border=True):
            st.markdown("**EXCEÇÕES COMUNS (LC 200/23)**")
            st.markdown("- Complementação ao FUNDEB")
            st.markdown("- Piso da Enfermagem")
            st.markdown("- Despesas custeadas com receitas próprias (Universidades)")
            st.markdown("- Créditos Extraordinários (Calamidades)")

    with col_meta:
        st.markdown("#### 🐖 Meta de Resultado Primário")
        st.write("Define o **saldo final** (Receita - Despesa) a ser entregue. É o alvo de solvência.")
        with st.container(border=True):
            st.markdown("**EXCEÇÕES À META (DADOS TESOURO 24/25)**")
            st.markdown("- **2024:** Calamidade RS (R$ 31,8 bi)")
            st.markdown("- **2025:** Precatórios acima do limite (R$ 41,1 bi)")
            st.markdown("- **2025:** Compensação INSS (ADPF 1236)")
            st.markdown("- **2025:** Projetos Estratégicos Defesa (LC 221)")


# ==============================================================================
# ABA 3: RESULTADOS 2024-2026 (Réplica dos Prints 3, 4, 5 e 6)
# ==============================================================================
with tab3:
    # --- Print 3: Barra Azul com Métricas ---
    st.markdown("### ✨ Impacto Prático das Exceções (2025)")
    st.caption("As exceções permitem que o governo apresente um resultado 'ajustado' para fins de cumprimento da legislação, mesmo que o déficit nominal (financeiro real) seja maior.")
    
    # Custom HTML Layout para as métricas azuis
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    
    with col_m1:
        st.markdown("""
        <div style="background-color:#1E3A8A; color:white; padding:15px; border-radius:8px; text-align:center;">
            <div style="font-size:10px; opacity:0.8;">RESULTADO NOMINAL</div>
            <div style="font-size:22px; font-weight:bold;">-R$ 61,7 Bi</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_m2:
        st.markdown("""
        <div style="background-color:#1E3A8A; color:white; padding:15px; border-radius:8px; text-align:center;">
            <div style="font-size:10px; opacity:0.8;">TOTAL EXCEÇÕES</div>
            <div style="font-size:22px; font-weight:bold; color:#4ade80;">+R$ 48,7 Bi</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_m3:
        st.markdown("""
        <div style="background-color:#1E3A8A; color:white; padding:15px; border-radius:8px; text-align:center;">
            <div style="font-size:10px; opacity:0.8;">RESULTADO P/ META</div>
            <div style="font-size:22px; font-weight:bold;">-R$ 13,0 Bi</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_m4:
        st.markdown("""
        <div style="background-color:#1E3A8A; color:white; padding:15px; border-radius:8px; text-align:center;">
            <div style="font-size:10px; opacity:0.8;">STATUS</div>
            <div style="background-color:#22c55e; color:white; padding:2px 10px; border-radius:10px; display:inline-block; font-weight:bold; margin-top:5px;">Cumpriu Meta</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()

    # --- Print 4: Panorama Fiscal ---
    st.subheader("Panorama Fiscal: 2024 vs 2025 vs 2026")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Déficit Primário 2025 (Nominal)", "-R$ 61,7 Bi", "-R$ 43,0 Bi (vs 2024)", delta_color="inverse")
    c2.metric("Déficit Primário 2025 (% PIB)", "-0,48%", "Meta central era 0%")
    c3.metric("Estoque Restos a Pagar 2026", "R$ 391,5 Bi", "+25,3% vs 2025", delta_color="inverse")
    
    st.divider()
    
    # --- Print 5: Gráficos ---
    g_col1, g_col2 = st.columns(2)
    
    with g_col1:
        st.markdown("**Resultado Nominal vs. Ajustado (Meta)**")
        # Dados simulados baseados no print
        data_res = pd.DataFrame({
            "Ano": ["2024", "2024", "2025", "2025"],
            "Tipo": ["Resultado Nominal (Déficit Real)", "Resultado Ajustado (P/ Meta)", "Resultado Nominal (Déficit Real)", "Resultado Ajustado (P/ Meta)"],
            "Valor": [-43.0, -11.0, -61.7, -13.0]
        })
        
        fig1 = px.bar(data_res, x="Ano", y="Valor", color="Tipo", barmode="group",
                      color_discrete_map={"Resultado Nominal (Déficit Real)": "#9ca3af", "Resultado Ajustado (P/ Meta)": "#1E3A8A"})
        fig1.update_layout(legend=dict(orientation="h", y=-0.2), margin=dict(t=10))
        st.plotly_chart(fig1, use_container_width=True)
        st.caption("* O resultado ajustado desconta as exceções legais (Calamidade RS, Precatórios, etc.)")

    with g_col2:
        st.markdown("**Pressão Fiscal Futura: Restos a Pagar (RAP)**")
        data_rap = pd.DataFrame({
            "Ano": ["2024", "2025", "2026"],
            "Valor": [285, 312, 391.5]
        })
        
        fig2 = px.bar(data_rap, x="Ano", y="Valor", text="Valor")
        fig2.update_traces(marker_color=["#cbd5e1", "#64748b", "#0f172a"]) # Gradiente de cinza/azul
        fig2.update_layout(yaxis_title="", margin=dict(t=10))
        st.plotly_chart(fig2, use_container_width=True)
        st.caption("* Valores inscritos para o exercício seguinte (ex: barra 2026 = inscrito em dez/25)")

    st.divider()

    # --- Print 6: Tabela Detalhada ---
    st.subheader("Detalhamento das Exceções à Meta (R$ Bilhões)")
    
    # Criando o DataFrame
    df_detalhe = pd.DataFrame({
        "ITEM": ["Déficit Nominal", "(-) Calamidade RS / Climática", "(-) Precatórios (Excedente)", "(-) Outros (INSS, Defesa, Saúde)", "Resultado Ajustado (p/ Meta)"],
        "2024": [-43.0, 31.8, 0.0, 0.1, -11.0],
        "2025": [-61.7, 0.0, 41.1, 7.5, -13.0]
    })
    
    # Função para colorir os valores
    def color_vals(val):
        if val < 0: return 'color: red; font-weight: bold;'
        if val > 0: return 'color: green;'
        return 'color: gray;'

    # Exibindo como dataframe estilizado
    st.dataframe(
        df_detalhe.style.format("{:.1f}").applymap(color_vals, subset=["2024", "2025"]),
        use_container_width=True,
        hide_index=True
    )
    
    # Badges de status no final
    col_s1, col_s2, col_s3 = st.columns([2,1,1])
    with col_s2:
        st.markdown("<span style='background-color:#d1fae5; color:#065f46; padding:5px 15px; border-radius:15px; font-size:12px;'>Dentro da Banda</span>", unsafe_allow_html=True)
    with col_s3:
        st.markdown("<span style='background-color:#d1fae5; color:#065f46; padding:5px 15px; border-radius:15px; font-size:12px;'>Dentro da Banda</span>", unsafe_allow_html=True)

# ==============================================================================
# ABA 4: Placeholder para código
# ==============================================================================
with tab4:
    st.code("Este painel foi gerado inteiramente com Python e Streamlit.", language="python")
