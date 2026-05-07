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
    ["🎲 Décideur Absurde", "📝 Cadavre Exquis", "🖱️ Clic Frénétique (Jauge)", "💡 Idées Folles", "🎨 Gribouillis"]
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

elif activity == "🖱️ Clic Frénétique (Jauge)":
    st.header("🖱️ **Clic Frénétique : La Jauge de la Mort**")
    st.write("La jauge monte toute seule ! **Clic pour la faire redescendre** et éviter qu'elle n'atteigne 100% pendant 20 secondes.")

    # Initialisation des variables de session
    if 'gauge_value' not in st.session_state:
        st.session_state.gauge_value = 0
    if 'time_left' not in st.session_state:
        st.session_state.time_left = 20
    if 'game_active' not in st.session_state:
        st.session_state.game_active = False
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False

    # Bouton pour démarrer le jeu
    if st.button("🚀 **DÉMARRER LE JEU**") and not st.session_state.game_active and not st.session_state.game_over:
        st.session_state.gauge_value = 0
        st.session_state.time_left = 20
        st.session_state.game_active = True
        st.session_state.game_over = False
        st.rerun()

    # Logique du jeu
    if st.session_state.game_active and not st.session_state.game_over:
        # Affichage de la jauge
        progress_bar = st.progress(st.session_state.gauge_value / 100)
        st.write(f"📈 **Jauge : {st.session_state.gauge_value}%**")
        st.write(f"⏳ **Temps restant : {st.session_state.time_left} secondes**")

        # Bouton pour cliquer et faire baisser la jauge
        if st.button("💥 **CLIC POUR FAIRE BAISSER LA JAUGE !**", key="click_button", use_container_width=True):
            st.session_state.gauge_value = max(0, st.session_state.gauge_value - 10)  # Baisse de 10% par clic
            st.rerun()

        # La jauge monte toute seule
        st.session_state.gauge_value = min(100, st.session_state.gauge_value + 1)  # Monte de 1% par rafraîchissement

        # Vérifier si la jauge a atteint 100%
        if st.session_state.gauge_value >= 100:
            st.session_state.game_active = False
            st.session_state.game_over = True
            st.rerun()

        # Décrémenter le temps
        time.sleep(0.5)  # Rafraîchissement toutes les 0.5 secondes pour un effet fluide
        st.session_state.time_left -= 0.5
        st.rerun()

        # Fin du jeu si le temps est écoulé
        if st.session_state.time_left <= 0:
            st.session_state.game_active = False
            st.session_state.game_over = False
            st.balloons()
            st.success(f"🎉 **BRAVO ! Tu as tenu 20 secondes !** (Jauge finale : {st.session_state.gauge_value}%)")
            if st.session_state.gauge_value < 20:
                st.write("🔥 **T'es un pro du clic !**")
            elif st.session_state.gauge_value < 50:
                st.write("👍 **Pas mal !**")
            else:
                st.write("😅 **T'as failli perdre !**")

    # Si la jauge a atteint 100%
    if st.session_state.game_over:
        st.error("💥 **GAME OVER ! La jauge a explosé !**")
        if st.button("🔄 **Recommencer**"):
            st.session_state.gauge_value = 0
            st.session_state.time_left = 20
            st.session_state.game_active = False
            st.session_state.game_over = False
            st.rerun()

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
