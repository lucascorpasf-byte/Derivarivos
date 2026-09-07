import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Especialização em Derivativos de Balcão",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS customizada
st.markdown("""
    <style>
    .main-header { font-size: 2.2rem; font-weight: bold; color: #1E3A8A; }
    .sub-header { font-size: 1.2rem; color: #475569; margin-bottom: 20px; }
    .card { background-color: #F8FAFC; border-left: 5px solid #1E3A8A; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
    .stat-card { background-color: #EFF6FF; border: 1px solid #BFDBFE; padding: 15px; border-radius: 8px; text-align: center; }
    .link-box { background-color: #F0FDF4; border: 1px solid #BBF7D0; padding: 10px; border-radius: 6px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# Inicialização do Estado da Sessão (Session State)
if 'progress' not in st.session_state:
    st.session_state.progress = {f"Dia {i}": False for i in range(1, 36)}

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = {}

# ---------------------------------------------------------
# SIDEBAR: Navegação e Progresso
# ---------------------------------------------------------
st.sidebar.title("📚 Módulos do Estudo")

semanas = {
    "Semana 1: Infraestrutura de Mercado, Registro e Liquidação": list(range(1, 6)),
    "Semana 2: Proteção do Investidor, Fundos e Derivativos de Crédito": list(range(6, 11)),
    "Semana 3: Tributação pela Receita Federal, IOF e Regime de Hedge Fiscal": list(range(11, 16)),
    "Semana 4: Requisitos de Capital Regulatório (Basileia III / SA-CCR)": list(range(16, 21)),
    "Semana 5: Contabilidade de Derivativos e Hedge Accounting (IFRS 9)": list(range(21, 26)),
    "Semana 6: Recuperação Judicial, Falência e Derivativos (Lei 11.101/05)": list(range(26, 31)),
    "Semana 7: Documentação Jurídica Internacional (ISDA), B3 e Desafio Final": list(range(31, 36))
}

semana_selecionada = st.sidebar.selectbox("Selecione a Semana:", list(semanas.keys()))

dias_disponiveis = [f"Dia {d}" for d in semanas[semana_selecionada]]
dia_selecionado = st.sidebar.radio("Selecione o Dia de Estudo:", dias_disponiveis)

st.sidebar.markdown("---")
st.sidebar.subheader("📊 Seu Progresso Geral")
dias_concluidos = sum(st.session_state.progress.values())
porcentagem = (dias_concluidos / 35) * 100
st.sidebar.progress(porcentagem / 100)
st.sidebar.write(f"**{dias_concluidos} de 35 dias** concluídos ({porcentagem:.1f}%)")

# ---------------------------------------------------------
# PAINEL PRINCIPAL
# ---------------------------------------------------------
st.markdown('<div class="main-header">Programa de Especialização em Derivativos de Balcão</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Imersão de 7 Semanas | 2 Horas por Dia | Regulação, Capital, IFRS 9 e Recuperação Judicial</div>', unsafe_allow_html=True)

# Dashboard de Métricas
col1, col2, col3, col4 = st.columns(4)
col1.metric("Carga Horária Total", "70 Horas", "2h / dia")
col2.metric("Módulos Regulatórios", "7 Semanas", "35 Dias Úteis")
col3.metric("Foco da Semana", semana_selecionada.split(":")[0])
col4.metric("Status do Dia", "✅ Concluído" if st.session_state.progress[dia_selecionado] else "⏳ Pendente")

st.markdown("---")

# ---------------------------------------------------------
# CONTEÚDO DO DIA 1
# ---------------------------------------------------------
if dia_selecionado == "Dia 1":
    st.header("Dia 1: Lei nº 13.018/2014 e Resolução CMN nº 4.593/2017")
    st.caption("Foco: Obrigatoriedade de registro de operações de balcão e validação em infraestruturas de mercado.")

    # LINKS OFICIAIS DAS NORMAS
    st.markdown("""
    <div class="link-box">
        📌 <b>Links Oficiais das Normas do Dia:</b><br>
        • <a href="https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l13018.htm" target="_blank">Lei nº 13.018/2014 (Planalto) — Registro e depósito de operações de balcão</a><br>
        • <a href="https://www.bcb.gov.br/estabilidadefinanceira/exibenorma?Membresia&numero=4593" target="_blank">Resolução CMN nº 4.593/2017 (Banco Central) — Validação por infraestruturas de mercado</a>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs([
        "📑 Resumo Executivo & Leitura Guiada", 
        "⚙️ Mecânica Operacional & Impacto", 
        "📝 Quiz de Fixação", 
        "💬 Tira-Dúvidas / Assistente AI"
    ])

    with tab1:
        st.subheader("1. O Marco Legal do Registro Obrigatório (Lei nº 13.018/2014)")
        st.markdown("""
        * **Ponto Central:** A Lei 13.018/14 estabeleceu a obrigatoriedade de registro ou de depósito de instrumentos financeiros e operações de derivativos de balcão em entidades administradoras de mercados organizados (como a **B3**).
        * **Finalidade:** Eliminar o "risco cego" de crédito no mercado financeiro nacional, garantindo que o Banco Central e a CVM tenham visibilidade completa das exposições sistêmicas do mercado OTC.
        * **Penalidades:** Operações não registradas ou registradas em desacordo com as normas estão sujeitas a sanções administrativas rigorosas impostas pelo BCB e CVM.
        """)

        st.subheader("2. A Validação e Reconciliação pelas Infraestruturas (Resolução CMN nº 4.593/2017)")
        st.markdown("""
        * **Dupla Checagem (Dual-side reporting):** As operações de balcão devem ser reportadas e **validadas por ambas as partes** ou confirmadas pela infraestrutura credenciada.
        * **Prazos de Registro:** Estabelece limites estritos para a entrada e confirmação dos dados das operações para evitar defasagem no cálculo do Risco de Crédito de Contraparte (CCR).
        * **Integração com B3:** Detalha os requisitos para que sistemas de negociação e plataformas de registro (ex: Balcão B3) atuem como registradores oficiais perante o SFN.
        """)

    with tab2:
        st.subheader("Mecânica de Registro e Reconciliação na B3")
        
        st.markdown('<div class="card"><b>Fluxo Operacional de uma Operação de Balcão (ex: Swap NDF):</b><br>'
                    '1. As partes negociam a operação (voice, chat ou e-broker).<br>'
                    '2. A instituição financeira A insere os dados no sistema de registro B3.<br>'
                    '3. A contraparte B recebe a notificação e efetua o aceite (matching de boleta).<br>'
                    '4. O contrato passa a ter eficácia regulatória e o Banco Central passa a ter acesso aos dados nocionais e de marcação a mercado (MtM).</div>', unsafe_allow_html=True)

        st.info("💡 **Atenção Prática:** Sem o registro correto e a validação tempestiva sob a Res. 4.593, o contrato de derivativo perde eficácia para fins de compensação bilateral (*netting*) sob a Resolução CMN nº 4.662 e para mitigação de RWA no modelo SA-CCR.")

    with tab3:
        st.subheader("Quiz de Fixação do Dia 1 (3 Questões Práticas)")

        with st.form("quiz_form_dia1"):
            q1 = st.radio(
                "1. Qual é o principal impacto trazido pela Lei nº 13.018/2014 para o mercado de derivativos de balcão no Brasil?",
                [
                    "A) Isentar a incidência de Imposto de Renda Retido na Fonte (IRRF) em swaps corporativos.",
                    "B) Tornar obrigatório o registro ou depósito das operações de balcão em infraestruturas de mercado autorizadas.",
                    "C) Proibir a contratação de derivativos de crédito por instituições financeiras de Porte S1.",
                    "D) Substituir a necessidade de contrato-mãe ISDA por registros simplificados em cartório."
                ]
            )

            q2 = st.radio(
                "2. Sob a Resolução CMN nº 4.593/2017, qual condição é essencial para a validação das operações de balcão nas infraestruturas de mercado?",
                [
                    "A) Confirmação unissecuritária pelo Banco Central em até 24 horas.",
                    "B) Liquidação obrigatoriamente efetuada com entrega física do ativo subjacente.",
                    "C) Validação e conciliação bilateral das informações reportadas pelas partes envolvidas.",
                    "D) Homologação prévia da minuta contratual pela CVM antes da execução."
                ]
            )

            q3 = st.radio(
                "3. Se uma instituição financeira deixa de registrar adequadamente uma operação de Swap de balcão na B3, qual a consequência imediata?",
                [
                    "A) O contrato é automaticamente convertido em uma debênture conversível.",
                    "B) A instituição fica sujeita a penalidades regulatórias e perde a eficácia do enquadramento para mitigação de risco e netting.",
                    "C) A B3 é obrigada a assumir o risco de crédito da operação como Contraparte Central.",
                    "D) A operação torna-se isenta de retenção tributária pela Receita Federal."
                ]
            )

            submitted = st.form_submit_button("Enviar Respostas")

            if submitted:
                score = 0
                if q1 == "B) Tornar obrigatório o registro ou depósito das operações de balcão em infraestruturas de mercado autorizadas.":
                    score += 1
                if q2 == "C) Validação e conciliação bilateral das informações reportadas pelas partes envolvidas.":
                    score += 1
                if q3 == "B) A instituição fica sujeita a penalidades regulatórias e perde a eficácia do enquadramento para mitigação de risco e netting.":
                    score += 1

                st.success(f"Você acertou {score} de 3 questões! ({score/3*100:.0f}%)")
                if score == 3:
                    st.balloons()
                    st.session_state.progress["Dia 1"] = True
                    st.info("✅ Parabéns! O Dia 1 foi marcado como CONCLUÍDO no seu progresso!")

    with tab4:
        st.subheader("💬 Canal de Dúvidas sobre o Dia 1")
        st.caption("Digite sua pergunta sobre a norma ou o caso prático do dia:")

        user_question = st.text_input("Sua dúvida sobre a Lei 13.018/14 ou Res. 4.593/17:", key="q_dia1")
        if st.button("Enviar Pergunta"):
            if user_question:
                if "Dia 1" not in st.session_state.chat_history:
                    st.session_state.chat_history["Dia 1"] = []
                
                # Exemplo de resposta estruturada contextualizada
                st.session_state.chat_history["Dia 1"].append(("Você", user_question))
                st.session_state.chat_history["Dia 1"].append(
                    ("Assistente", f"Em relação à sua dúvida sobre '{user_question}': Lembre-se que, sob a Res. 4.593/17, a tempestividade na validação bilateral das boletas na B3 é indispensável para assegurar a validade do netting contratual no cálculo do RWA_CPF.")
                )

        if "Dia 1" in st.session_state.chat_history:
            st.markdown("---")
            st.write("**Histórico de Perguntas e Respostas:**")
            for autor, texto in st.session_state.chat_history["Dia 1"]:
                if autor == "Você":
                    st.markdown(f"👤 **{autor}:** {texto}")
                else:
                    st.markdown(f"🤖 **{autor}:** {texto}")

else:
    st.header(f"{dia_selecionado}: Conteúdo em Preparação")
    st.warning("Este módulo estará disponível no seu cronograma diário conforme você avança na leitura.")
    st.markdown(f"**Tema da Semana:** {semana_selecionada}")

st.markdown("---")
# BOTÃO DE CONCLUSÃO MANUAL DO DIA
col_btn1, col_btn2 = st.columns([1, 4])
with col_btn1:
    is_done = st.checkbox("Marcar como Concluído ✅", value=st.session_state.progress[dia_selecionado])
    if is_done != st.session_state.progress[dia_selecionado]:
        st.session_state.progress[dia_selecionado] = is_done
        st.rerun()
