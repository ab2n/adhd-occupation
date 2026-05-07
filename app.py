import streamlit as st
import random
import time
from datetime import datetime

st.set_page_config(
    page_title="Réu Survival Kit",
    page_icon="🧠",
    layout="wide"
)

# -----------------------------
# Helpers
# -----------------------------

quotes = [
    "Cette réunion aurait pu être un email.",
    "Tu tiens bon. Le speaker, moins.",
    "Le vrai KPI c'est survivre jusqu'à la fin.",
    "Ton cerveau mérite une médaille.",
    "Oui, ils reparlent du même sujet.",
    "Respire. Hoche la tête. Continue.",
    "Tu es actuellement en mode camouflage social.",
]

buzzwords = [
    "synergie", "roadmap", "scalabilité", "alignement",
    "disruptif", "pipeline", "quick win", "vision produit",
    "ownership", "verticalisation", "optimisation"
]

animals = [
    "🦦", "🦝", "🐸", "🐢", "🦥", "🐙", "🦜", "🐌"
]

excuses = [
    "Je crois que mon VPN mange ma bande passante.",
    "Pardon, Teams a décidé de redémarrer mon cerveau.",
    "J'avais un lag audio quantique.",
    "Mon micro était muté dans une autre dimension.",
    "Je prenais des notes ultra stratégiques.",
]

if "score" not in st.session_state:
    st.session_state.score = 0

if "pet_name" not in st.session_state:
    st.session_state.pet_name = "Blob"

if "pet_mood" not in st.session_state:
    st.session_state.pet_mood = 5

# -----------------------------
# Header
# -----------------------------

st.title("🧠 Réu Survival Kit")
st.caption("Un mini refuge dopamine-friendly pour les réunions interminables.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Niveau de survie", f"{st.session_state.score} XP")

with col2:
    st.metric("Motivation actuelle", random.randint(3, 97))

with col3:
    st.metric("Temps perdu estimé", f"{random.randint(14, 83)} min")

st.divider()

# -----------------------------
# Tabs
# -----------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎯 Mini dopamine",
    "🐾 Animal de réu",
    "🎲 Chaos",
    "📈 Bingo corporate",
    "🧘 Focus absurde"
])

# -----------------------------
# TAB 1
# -----------------------------

with tab1:
    st.subheader("Boutons inutiles mais satisfaisants")

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("🎉 Dopamine instantanée"):
            st.balloons()
            st.session_state.score += 10
            st.success(random.choice(quotes))

    with c2:
        if st.button("🔥 Booster de productivité fictif"):
            st.session_state.score += 5
            st.toast("Tu es maintenant 2% plus corporate.")

    with c3:
        if st.button("💀 Réunion critique détectée"):
            st.error("Quelqu'un vient de dire 'on se refait un point'.")

    st.divider()

    st.subheader("Machine à compliments absurdes")

    compliments = [
        "Ton multitasking est scientifiquement inquiétant.",
        "Tu pourrais survivre à 4 daily meetings d'affilée.",
        "Ton niveau de patience est mythologique.",
        "Même ton onglet YouTube est organisé.",
        "Tu maîtrises l'art du regard attentif vide.",
    ]

    if st.button("✨ Générer un compliment"):
        st.info(random.choice(compliments))

# -----------------------------
# TAB 2
# -----------------------------

with tab2:
    st.subheader("Ton animal de réunion")

    pet = random.choice(animals)

    st.markdown(
        f"## {pet} {st.session_state.pet_name}\n"
        f"Humeur actuelle : {'⭐' * st.session_state.pet_mood}"
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("🍪 Nourrir"):
            st.session_state.pet_mood = min(10, st.session_state.pet_mood + 1)
            st.success("L'animal approuve cette stratégie.")

    with c2:
        if st.button("🎾 Jouer"):
            st.session_state.pet_mood = min(10, st.session_state.pet_mood + 2)
            st.balloons()

    with c3:
        if st.button("📉 Lui montrer le backlog"):
            st.session_state.pet_mood = max(1, st.session_state.pet_mood - 3)
            st.warning("Erreur psychologique.")

# -----------------------------
# TAB 3
# -----------------------------

with tab3:
    st.subheader("Chaos generator")

    if st.button("🎲 Situation aléatoire"):
        events = [
            "Quelqu'un parle depuis 8 minutes sans respirer.",
            "Une personne partage le mauvais écran.",
            "Le manager dit 'rapidement' avant un monologue.",
            "Un micro produit des sons extraterrestres.",
            "Quelqu'un dit 'petite question' et ouvre un débat de 40 min.",
            "Tu reviens mentalement après 12 minutes d'absence totale.",
        ]

        st.write(random.choice(events))
        st.session_state.score += 3

    st.divider()

    st.subheader("Excuse professionnelle d'urgence")

    if st.button("🛟 Générer une excuse"):
        st.code(random.choice(excuses))

# -----------------------------
# TAB 4
# -----------------------------

with tab4:
    st.subheader("Bingo Corporate")

    cols = st.columns(3)

    for i, word in enumerate(random.sample(buzzwords, 9)):
        with cols[i % 3]:
            if st.checkbox(word, key=f"buzz_{i}"):
                st.session_state.score += 1

    if st.session_state.score > 25:
        st.success("🏆 Achievement unlocked : survivant senior des réunions")

# -----------------------------
# TAB 5
# -----------------------------

with tab5:
    st.subheader("Focus absurde")

    duration = st.slider("Timer de faux focus (minutes)", 1, 15, 5)

    if st.button("⏳ Lancer le focus"):
        bar = st.progress(0)
        status = st.empty()

        fake_tips = [
            "Regarde intensément ton écran.",
            "Hoche la tête de temps en temps.",
            "Dis 'bonne question'.",
            "Prends des notes illisibles.",
            "Fais semblant de comprendre le diagramme.",
        ]

        for i in range(100):
            time.sleep(0.03)
            bar.progress(i + 1)

            if i % 20 == 0:
                status.info(random.choice(fake_tips))

        st.success("Focus terminé. Récompense émotionnelle virtuelle accordée.")
        st.session_state.score += 15

# -----------------------------
# Footer
# -----------------------------

st.divider()

st.caption(
    f"Dernière mise à jour mentale : {datetime.now().strftime('%H:%M:%S')}"
)

st.markdown("""
### 💡 Lancement

```bash
pip install streamlit
streamlit run app.py
