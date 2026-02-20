import streamlit as st
from dataclasses import dataclass

# -------------------------
# Page config
# -------------------------
st.set_page_config(
    page_title="Accent Bias Awareness | Discriminação Linguística",
    page_icon="💬",
    layout="centered",
)

# -------------------------
# Styling (light pink + rounded "bubbles")
# -------------------------
PINK_CSS = """
<style>
:root {
  --bg: #fff5f8;
  --card: #ffffff;
  --accent: #ff6fae;
  --accent2: #ffc2d8;
  --text: #2b2b2b;
  --muted: #6b6b6b;
}

.stApp {
  background: var(--bg);
  color: var(--text);
}

h1, h2, h3, h4 {
  color: var(--text);
}

.bubble-card {
  background: var(--card);
  border-radius: 28px;
  padding: 18px 18px 14px 18px;
  border: 1px solid rgba(255, 111, 174, 0.25);
  box-shadow: 0 6px 18px rgba(255, 111, 174, 0.08);
  margin-bottom: 14px;
}

.bubble-soft {
  background: rgba(255, 194, 216, 0.25);
  border-radius: 999px;
  padding: 10px 16px;
  display: inline-block;
  margin: 6px 0 10px 0;
  border: 1px solid rgba(255, 111, 174, 0.18);
}

.small-muted {
  color: var(--muted);
  font-size: 0.92rem;
}

hr {
  border: none;
  height: 1px;
  background: rgba(255, 111, 174, 0.18);
  margin: 16px 0;
}

div.stButton > button {
  background: var(--accent);
  color: white;
  border: none;
  border-radius: 999px;
  padding: 0.55rem 1.0rem;
  font-weight: 600;
}

div.stButton > button:hover {
  background: #ff4f9f;
}

.stRadio div[role="radiogroup"] {
  background: white;
  border-radius: 18px;
  padding: 10px 14px;
  border: 1px solid rgba(255, 111, 174, 0.18);
}

footer {visibility: hidden;}
</style>
"""
st.markdown(PINK_CSS, unsafe_allow_html=True)


# -------------------------
# Bilingual text dictionary
# -------------------------
TEXT = {
    "pt": {
        "lang_label": "🌍 Língua / Language",
        "lang_pt": "Português (PT)",
        "lang_en": "English",
        "title": "Sensibilização para Discriminação Linguística no Recrutamento",
        "subtitle": "Uma aplicação educativa baseada em investigação (sem recolha de dados).",
        "purpose_title": "Objetivo",
        "purpose_body": (
            "Esta aplicação visa sensibilizar para a discriminação baseada no sotaque e na variedade linguística "
            "em contextos profissionais, em particular em processos de recrutamento e seleção, promovendo práticas "
            "mais justas e inclusivas."
        ),
        "how_title": "Como funciona",
        "how_body": (
            "Irá ver 3 cenários curtos relacionados com decisões de recrutamento. "
            "Escolha uma opção e, em seguida, veja uma explicação e sugestões práticas para reduzir vieses."
        ),
        "start": "Começar",
        "nav_label": "Navegação",
        "nav_intro": "Introdução",
        "nav_quiz": "Quiz",
        "nav_tips": "Dicas Práticas",
        "nav_refs": "Referências",
        "no_storage": "Nota: As suas respostas não são guardadas. A informação fica apenas nesta sessão.",
        "quiz_title": "Quiz (3 cenários)",
        "scenario": "Cenário",
        "choose": "Escolha uma opção",
        "show_feedback": "Ver feedback",
        "next": "Próximo",
        "back": "Voltar",
        "done": "Concluir",
        "tips_title": "Dicas práticas para mitigar vieses (recrutamento)",
        "tips_intro": "Sugestões aplicáveis em processos de recrutamento e avaliação de candidatos:",
        "refs_title": "Referências e recursos",
        "refs_intro": "Exemplos de conceitos e linhas de investigação relevantes (adicione as suas referências específicas):",
        "github_label": "🔗 Repositório GitHub (opcional)",
        "image_caption": "Bem-vindo/a! (Pode substituir esta imagem por uma ilustração sua.)",
    },
    "en": {
        "lang_label": "🌍 Language / Língua",
        "lang_pt": "Português (PT)",
        "lang_en": "English",
        "title": "Accent & Language-Based Discrimination Awareness in Hiring",
        "subtitle": "A research-informed educational app (no data collection).",
        "purpose_title": "Purpose",
        "purpose_body": (
            "This application aims to raise awareness of accent and language-based discrimination in professional contexts, "
            "particularly in recruitment and hiring, and to promote fairer and more inclusive decision-making practices."
        ),
        "how_title": "How it works",
        "how_body": (
            "You will see 3 short scenarios related to hiring decisions. "
            "Select an option and then view a brief explanation and practical tips to reduce bias."
        ),
        "start": "Start",
        "nav_label": "Navigation",
        "nav_intro": "Introduction",
        "nav_quiz": "Quiz",
        "nav_tips": "Practical Tips",
        "nav_refs": "References",
        "no_storage": "Note: Your responses are not stored. Everything stays in this session only.",
        "quiz_title": "Quiz (3 scenarios)",
        "scenario": "Scenario",
        "choose": "Choose one option",
        "show_feedback": "Show feedback",
        "next": "Next",
        "back": "Back",
        "done": "Finish",
        "tips_title": "Practical bias-mitigation tips for hiring",
        "tips_intro": "Actionable suggestions for recruitment and candidate evaluation:",
        "refs_title": "References & resources",
        "refs_intro": "Examples of relevant concepts and research lines (add your own specific references):",
        "github_label": "🔗 GitHub repository (optional)",
        "image_caption": "Welcome! (You can replace this image with your own illustration.)",
    },
}


# -------------------------
# Quiz content (text-only, neutral tone)
# You can edit these later to match your thesis framing.
# -------------------------
@dataclass
class Scenario:
    title_pt: str
    title_en: str
    prompt_pt: str
    prompt_en: str
    options_pt: list
    options_en: list
    feedback_pt: str
    feedback_en: str
    tips_pt: list
    tips_en: list


SCENARIOS = [
    Scenario(
        title_pt="Entrevista telefónica: avaliação “rápida”",
        title_en="Phone screen: “quick” evaluation",
        prompt_pt=(
            "Dois candidatos têm CVs equivalentes e respondem adequadamente às perguntas técnicas. "
            "Após uma breve conversa telefónica, um avaliador comenta: "
            "“A pessoa parece competente, mas o sotaque é muito forte; pode ser difícil com clientes.”\n\n"
            "Como deve a equipa proceder neste momento do processo?"
        ),
        prompt_en=(
            "Two candidates have equivalent CVs and answer technical questions well. "
            "After a short phone screen, a reviewer comments: "
            "“They seem competent, but the accent is very strong; it may be difficult with clients.”\n\n"
            "How should the team proceed at this stage?"
        ),
        options_pt=[
            "Avançar o candidato para a próxima fase e avaliar competências com critérios estruturados.",
            "Rejeitar o candidato com base no risco percebido de comunicação com clientes.",
            "Manter o candidato em “espera” até aparecer alguém com comunicação “mais neutra”.",
        ],
        options_en=[
            "Advance the candidate and evaluate skills using structured criteria.",
            "Reject the candidate due to the perceived risk of client communication.",
            "Keep the candidate on hold until someone with “more neutral” speech appears.",
        ],
        feedback_pt=(
            "Comentários sobre “sotaque forte” podem funcionar como atalho para julgamentos não relacionados com desempenho. "
            "Uma abordagem mais justa é separar comunicação de conteúdo: definir critérios observáveis (ex.: clareza, turn-taking, "
            "capacidade de reformular) e aplicar a mesma avaliação a todos os candidatos. Se comunicação com clientes é essencial, "
            "crie uma tarefa padronizada e avalie com grelha."
        ),
        feedback_en=(
            "Comments about a “strong accent” can become a shortcut for judgments unrelated to job performance. "
            "A fairer approach is to separate communication style from content: define observable criteria (e.g., clarity, turn-taking, "
            "ability to rephrase) and apply the same evaluation to all candidates. If client communication is essential, use a standardized task "
            "and score it with a rubric."
        ),
        tips_pt=[
            "Use entrevistas estruturadas e grelhas com critérios observáveis.",
            "Evite inferir competência com base em fluência percebida ou sotaque.",
            "Se ‘comunicação’ é requisito, avalie-a com uma tarefa padronizada (não por impressão).",
        ],
        tips_en=[
            "Use structured interviews and rubrics with observable criteria.",
            "Avoid inferring competence from perceived fluency or accent.",
            "If communication is a requirement, assess it via a standardized task (not impressions).",
        ],
    ),
    Scenario(
        title_pt="Reunião de equipa: atribuição de papéis",
        title_en="Team meeting: role assignment",
        prompt_pt=(
            "Durante uma reunião, um candidato (ou novo colaborador) apresenta ideias claras, mas com uma variedade linguística "
            "não-padrão. Um colega sugere: “Talvez seja melhor não o colocar em apresentações externas por agora.”\n\n"
            "Qual é a resposta mais apropriada?"
        ),
        prompt_en=(
            "In a meeting, a candidate (or new hire) presents clear ideas but uses a non-standard language variety. "
            "A colleague suggests: “Maybe we should avoid putting them on external presentations for now.”\n\n"
            "What is the most appropriate response?"
        ),
        options_pt=[
            "Perguntar quais critérios concretos estão a ser usados e propor treino/apoio igualitário para apresentações.",
            "Concordar e evitar exposições externas para proteger a imagem da empresa.",
            "Decidir caso a caso com base em impressões de ‘profissionalismo’ linguístico.",
        ],
        options_en=[
            "Ask what concrete criteria are being used and propose equal access to presentation support/training.",
            "Agree and avoid external exposure to protect the company image.",
            "Decide case by case based on impressions of linguistic ‘professionalism’.",
        ],
        feedback_pt=(
            "Associar ‘profissionalismo’ a uma variedade específica pode reproduzir desigualdades. "
            "Uma estratégia é explicitar critérios (ex.: estrutura da apresentação, mensagens-chave, resposta a perguntas) e garantir "
            "apoio igualitário. Se houver necessidade real (ex.: requisito de idioma para um cliente específico), documente-a e avalie "
            "de forma consistente, evitando generalizações."
        ),
        feedback_en=(
            "Linking ‘professionalism’ to a particular variety can reproduce inequality. "
            "A good strategy is to make criteria explicit (e.g., structure, key messages, Q&A handling) and provide equal support. "
            "If there is a genuine requirement (e.g., a specific client language constraint), document it and evaluate consistently, avoiding generalizations."
        ),
        tips_pt=[
            "Substitua ‘parece pouco profissional’ por critérios observáveis e mensuráveis.",
            "Garanta oportunidades iguais para tarefas visíveis (apresentações, reuniões com clientes).",
            "Promova normas inclusivas de comunicação (ex.: reformulação, clarificação).",
        ],
        tips_en=[
            "Replace ‘seems unprofessional’ with observable, measurable criteria.",
            "Ensure equal access to high-visibility tasks (presentations, client meetings).",
            "Promote inclusive communication norms (e.g., rephrasing, clarification).",
        ],
    ),
    Scenario(
        title_pt="Triagem de candidaturas: ‘fit’ e ‘comunicação’",
        title_en="Application screening: ‘fit’ and ‘communication’",
        prompt_pt=(
            "Na triagem de candidaturas, um avaliador escreve: “Excelente experiência, mas não sei se encaixa; a comunicação pode ser um desafio.” "
            "Não há exemplos concretos — apenas uma impressão geral baseada numa breve interação.\n\n"
            "Qual é a melhor ação para reduzir viés nesta fase?"
        ),
        prompt_en=(
            "During screening, a reviewer writes: “Excellent background, but I’m not sure about fit; communication may be challenging.” "
            "There are no concrete examples—only a general impression from a brief interaction.\n\n"
            "What is the best action to reduce bias at this stage?"
        ),
        options_pt=[
            "Pedir exemplos concretos e usar critérios padronizados (com pontuação) antes de decidir.",
            "Aceitar a impressão do avaliador para acelerar o processo.",
            "Remover candidatos com ‘comunicação duvidosa’ para reduzir risco.",
        ],
        options_en=[
            "Request concrete examples and use standardized, scored criteria before deciding.",
            "Accept the reviewer’s impression to speed up the process.",
            "Remove candidates with ‘questionable communication’ to reduce risk.",
        ],
        feedback_pt=(
            "Impressões vagas (“fit”, “comunicação”) são terreno fértil para viés. "
            "O mais eficaz é exigir justificações baseadas em evidência e aplicar critérios padronizados com pontuação. "
            "Se ‘comunicação’ é relevante, defina o que significa (ex.: clareza, adequação ao contexto, capacidade de síntese) e avalie de forma consistente."
        ),
        feedback_en=(
            "Vague impressions (“fit”, “communication”) are fertile ground for bias. "
            "The most effective response is to require evidence-based justification and apply standardized, scored criteria. "
            "If ‘communication’ matters, define what it means (e.g., clarity, context-appropriateness, summarization ability) and assess consistently."
        ),
        tips_pt=[
            "Use fichas de avaliação com critérios e âncoras (ex.: 1–5 com exemplos).",
            "Exija exemplos concretos antes de rejeitar com base em ‘impressão’.",
            "Inclua mais de um avaliador e discuta discrepâncias com foco em evidência.",
        ],
        tips_en=[
            "Use evaluation forms with criteria and anchors (e.g., 1–5 with examples).",
            "Require concrete examples before rejecting based on ‘impressions’.",
            "Use more than one reviewer and discuss discrepancies with an evidence focus.",
        ],
    ),
]


# -------------------------
# Session state
# -------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "pt"
if "page" not in st.session_state:
    st.session_state.page = "intro"
if "scenario_idx" not in st.session_state:
    st.session_state.scenario_idx = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}  # idx -> option_index


def t(key: str) -> str:
    return TEXT[st.session_state.lang][key]


# -------------------------
# Sidebar (language + navigation)
# -------------------------
st.sidebar.markdown(f"### {t('lang_label')}")
lang_choice = st.sidebar.radio(
    label="",
    options=["pt", "en"],
    format_func=lambda x: TEXT[x]["lang_pt"] if x == "pt" else TEXT[x]["lang_en"],
    index=0 if st.session_state.lang == "pt" else 1,
)
st.session_state.lang = lang_choice

st.sidebar.markdown("---")
st.sidebar.markdown(f"### {t('nav_label')}")

nav = st.sidebar.radio(
    label="",
    options=["intro", "quiz", "tips", "refs"],
    format_func=lambda x: {
        "intro": t("nav_intro"),
        "quiz": t("nav_quiz"),
        "tips": t("nav_tips"),
        "refs": t("nav_refs"),
    }[x],
    index=["intro", "quiz", "tips", "refs"].index(st.session_state.page),
)
st.session_state.page = nav


# -------------------------
# Header
# -------------------------
st.markdown(f"<div class='bubble-soft'>💗 {t('subtitle')}</div>", unsafe_allow_html=True)
st.title(t("title"))

# Center illustration (optional)
# Put an image at: assets/waving.png (or change path / use URL)
try:
    st.image("assets/waving.png", caption=t("image_caption"), use_container_width=True)
except Exception:
    # If image not found, silently continue (keeps app runnable)
    pass

st.markdown(f"<div class='small-muted'>{t('no_storage')}</div>", unsafe_allow_html=True)
st.markdown("<hr/>", unsafe_allow_html=True)


# -------------------------
# Pages
# -------------------------
if st.session_state.page == "intro":
    st.markdown(f"<div class='bubble-card'><h3>{t('purpose_title')}</h3><p>{t('purpose_body')}</p></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='bubble-card'><h3>{t('how_title')}</h3><p>{t('how_body')}</p></div>", unsafe_allow_html=True)

    if st.button(t("start")):
        st.session_state.page = "quiz"
        st.session_state.scenario_idx = 0
        st.rerun()

elif st.session_state.page == "quiz":
    st.subheader(t("quiz_title"))

    idx = st.session_state.scenario_idx
    scenario = SCENARIOS[idx]

    title = scenario.title_pt if st.session_state.lang == "pt" else scenario.title_en
    prompt = scenario.prompt_pt if st.session_state.lang == "pt" else scenario.prompt_en
    options = scenario.options_pt if st.session_state.lang == "pt" else scenario.options_en
    feedback = scenario.feedback_pt if st.session_state.lang == "pt" else scenario.feedback_en
    tips = scenario.tips_pt if st.session_state.lang == "pt" else scenario.tips_en

    st.markdown(
        f"<div class='bubble-card'><h3>{t('scenario')} {idx+1}/3 — {title}</h3><p>{prompt}</p></div>",
        unsafe_allow_html=True,
    )

    # Choose option
    default_index = st.session_state.answers.get(idx, 0)
    choice = st.radio(t("choose"), options, index=default_index)
    chosen_idx = options.index(choice)
    st.session_state.answers[idx] = chosen_idx

    # Feedback section
    with st.expander(t("show_feedback")):
        st.markdown(f"<div class='bubble-card'><p>{feedback}</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='bubble-card'><b>Tips</b><ul>" + "".join([f"<li>{x}</li>" for x in tips]) + "</ul></div>", unsafe_allow_html=True)

    # Navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button(t("back"), disabled=(idx == 0)):
            st.session_state.scenario_idx = max(0, idx - 1)
            st.rerun()
    with col2:
        if idx < 2:
            if st.button(t("next")):
                st.session_state.scenario_idx = min(2, idx + 1)
                st.rerun()
        else:
            if st.button(t("done")):
                st.session_state.page = "tips"
                st.rerun()
    with col3:
        # tiny spacer / no action
        st.write("")

elif st.session_state.page == "tips":
    st.subheader(t("tips_title"))
    st.write(t("tips_intro"))

    tips_pt = [
        "Use entrevistas estruturadas e critérios observáveis (com âncoras de pontuação).",
        "Evite ‘fit’ e ‘profissionalismo’ como justificações vagas; peça exemplos concretos.",
        "Separe competência técnica de estilo de fala; avalie comunicação com tarefas padronizadas quando necessário.",
        "Treine avaliadores para reconhecer vieses e usar linguagem descritiva (o que foi observado) em vez de julgamentos globais.",
        "Garanta múltiplos avaliadores e discuta discrepâncias com foco em evidência.",
    ]
    tips_en = [
        "Use structured interviews and observable criteria (with scoring anchors).",
        "Avoid vague justifications like ‘fit’ or ‘professionalism’; request concrete examples.",
        "Separate technical competence from speaking style; assess communication via standardized tasks when needed.",
        "Train reviewers to recognize bias and use descriptive language (what was observed) rather than global judgments.",
        "Use multiple reviewers and discuss discrepancies with an evidence focus.",
    ]

    tips = tips_pt if st.session_state.lang == "pt" else tips_en
    st.markdown("<div class='bubble-card'><ul>" + "".join([f"<li>{x}</li>" for x in tips]) + "</ul></div>", unsafe_allow_html=True)

    st.markdown("<div class='bubble-card'><b>Optional:</b> Add a short checklist recruiters can print/use in interviews.</div>", unsafe_allow_html=True)

elif st.session_state.page == "refs":
    st.subheader(t("refs_title"))
    st.write(t("refs_intro"))

    refs_pt = [
        "Investigação sobre vieses linguísticos e perceção de sotaque em decisões de credibilidade/competência.",
        "Metodologias como ‘matched-guise’ e julgamentos de voz (sem necessidade de recolha de dados no app).",
        "Práticas de recrutamento baseadas em evidência: entrevistas estruturadas, rubricas e múltiplos avaliadores.",
        "Legislação e políticas internas de diversidade e inclusão (adaptar ao contexto do utilizador).",
    ]
    refs_en = [
        "Research on language-based bias and accent perception in judgments of competence/credibility.",
        "Methods such as matched-guise and voice judgment paradigms (no data collection required in this app).",
        "Evidence-based hiring practices: structured interviews, rubrics, and multiple reviewers.",
        "Legal/policy context and internal DEI guidelines (adapt to the user’s context).",
    ]
    refs = refs_pt if st.session_state.lang == "pt" else refs_en

    st.markdown("<div class='bubble-card'><ul>" + "".join([f"<li>{x}</li>" for x in refs]) + "</ul></div>", unsafe_allow_html=True)

    st.markdown(f"<div class='bubble-card'>{t('github_label')}: <span class='small-muted'>add your GitHub link here</span></div>", unsafe_allow_html=True)