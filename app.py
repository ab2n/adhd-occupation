import streamlit as st
import random
import time

# --- Config ---
st.set_page_config(
    page_title="ADHD Playground",
    page_icon="🎲",
    layout="wide"
)

# --- Style ---
st.markdown("""
<style>
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        background-color: #FFF0F0;
    }
    .stMarkdown {
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("🎲 **ADHD Playground**")
st.markdown("Pour survivre aux réunions sans mourir d'ennui. Par **bgriot**.")

# --- Sidebar ---
st.sidebar.header("⚡ Menu")
activity = st.sidebar.radio(
    "Choisis ton aventure :",
    ["🎲 Décideur Absurde", "📝 Cadavre Exquis", "🖱️ Clic Frénétique", "💡 Idées Folles", "🎨 Gribouillis"]
)

# --- Tabs ---
if activity == "🎲 Décideur Absurde":
    st.header("⚖️ Le Décideur Absurde")
    st.write("Pose une question existentielle, et laisse le destin décider.")

    question = st.text_input("Ta question :", placeholder="Ex: Dois-je aller aux toilettes MAINTENANT ?")
    if st.button("Lancer le dé du destin"):
        if question:
            decision = random.choice([
                "✅ **OUI, FONCE !** (Mais discrètement.)",
                "❌ **NON, ATTEND.** (Ou pas.)",
                "🤷 **PEUT-ÊTRE.** (Lance à nouveau.)",
                "💥 **FAIS-LE SANS RÉFLÉCHIR.**",
                "😴 **VA FAIRE UNE SIESTE.**",
                "🎉 **TRANSFORME TA QUESTION EN CHANSON.**"
            ])
            st.balloons()
            st.success(decision)
        else:
            st.warning("Pose une question, sinon le destin ne peut pas t'aider !")

elif activity == "📝 Cadavre Exquis":
    st.header("📜 Cadavre Exquis")
    st.write("Écris un mot, et laisse l'IA générer une phrase complètement déjantée.")

    word = st.text_input("Ton mot :", placeholder="Ex: Licorne")
    if st.button("Générer l'absurdité"):
        if word:
            absurd_phrases = [
                f"Le/La {word} a volé mon sandwich et l'a remplacé par un {random.choice(['nuage', 'réfrigérateur', 'président', 'chat en pyjama'])}.",
                f"Hier, j'ai vu un {word} danser la salsa avec {random.choice(['ma grand-mère', 'un robot', 'une pizza', 'ton boss'])}.",
                f"Attention : ce {word} est en réalité un espion de {random.choice(['la CIA', 'les aliens', 'ton frigo', 'Emmanuel Macron'])}.",
                f"Si tu mélanges un {word} avec {random.choice(['du ketchup', 'une chaussette', 'un Excel', 'ton café'])}, tu obtiens... le bonheur.",
                f"Le {word} est la solution à tous tes problèmes. Sauf celui de {random.choice(['ta belle-mère', 'les impôts', 'la gravité', 'cette réunion'])}."
            ]
            st.balloons()
            st.success(random.choice(absurd_phrases))
        else:
            st.warning("Il faut un mot pour démarrer la folie !")

elif activity == "🖱️ Clic Frénétique":
    st.header("🖱️ Clic Frénétique")
    st.write("Clic sur le bouton **aussi vite que possible** pendant 10 secondes !")

    # Initialisation des variables de session
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'time_left' not in st.session_state:
        st.session_state.time_left = 10
    if 'game_active' not in st.session_state:
        st.session_state.game_active = False

    # Bouton pour démarrer le jeu
    if st.button("🚀 **DÉMARRER LE CHRONO**") and not st.session_state.game_active:
        st.session_state.score = 0
        st.session_state.time_left = 10
        st.session_state.game_active = True
        st.rerun()

    # Logique du jeu
    if st.session_state.game_active:
        if st.session_state.time_left > 0:
            # Bouton pour cliquer
            if st.button("💥 **CLIC !**", key="click_button", use_container_width=True):
                st.session_state.score += 1
                st.rerun()

            # Affichage du temps restant et du score
            progress_bar = st.progress((10 - st.session_state.time_left) / 10)
            st.write(f"⏳ Temps restant : **{st.session_state.time_left} secondes**")
            st.write(f"🎯 Score actuel : **{st.session_state.score} clics**")

            # Décrémenter le temps
            time.sleep(1)
            st.session_state.time_left -= 1
            st.rerun()
        else:
            # Fin du jeu
            st.session_state.game_active = False
            st.balloons()
            st.success(f"🎉 **SCORE FINAL : {st.session_state.score} clics en 10 secondes !**")
            if st.session_state.score > 30:
                st.write("🔥 **T'es une machine à cliquer !**")
            elif st.session_state.score > 15:
                st.write("👍 **Pas mal !**")
            else:
                st.write("😅 **T'as besoin de t'entraîner !**")

elif activity == "💡 Idées Folles":
    st.header("💡 Boîte à Idées Folles")
    st.write("Note toutes les idées géniales (ou pas) qui te passent par la tête pendant la réunion.")

    idea = st.text_area("Ta pensée du moment :", placeholder="Ex: Et si on remplaçait les réunions par des battles de karaoké ?")
    if st.button("📥 Sauvegarder cette pépite"):
        if idea:
            st.success("✅ Idée enregistrée ! (En vrai, elle est juste là. Mais c'est déjà ça.)")
            st.markdown(f"> *{idea}*")
        else:
            st.warning("T'as oublié d'écrire ton chef-d'œuvre !")

elif activity == "🎨 Gribouillis":
    st.header("🎨 Gribouillis Numérique")
    st.write("Dessine avec des emojis ! (Oui, c'est limité. Mais c'est mieux que rien.)")

    canvas = st.text_area("Ton œuvre d'art :", placeholder="Ex: 🎨⬛⬜⬛\n⬜🟥⬜\n⬛⬜⬛", height=200)
    if st.button("🖼️ Afficher mon chef-d'œuvre"):
        if canvas:
            st.code(canvas, language="text")
            st.success("Magnifique ! (Ou pas. Mais on s'en fiche.)")
        else:
            st.warning("T'as rien dessiné, artiste !")

# --- Footer ---
st.markdown("---")
st.markdown("💡 PS : Si t'as d'autres idées de modules, dis-le-moi !")
