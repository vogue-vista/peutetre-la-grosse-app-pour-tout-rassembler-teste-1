import streamlit as st
from groq import Groq

# 🔒 Sécurité : synchronisé avec l'écran d'accueil global
if "est_abonne_global" not in st.session_state or not st.session_state.est_abonne_global:
    st.warning("🔒 Veuillez vous connecter sur la page d'accueil.")
    st.stop()

st.title("💼 Générateur de Réponses Professionnelles (IA PRO)")
st.write("Générez automatiquement des réponses professionnelles, personnalisées et adaptées au contexte du message client.")

# 🔑 Clé IA sécurisée
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_API_KEY)
except:
    st.error("❌ Clé GROQ_API_KEY manquante dans les secrets Streamlit.")
    st.stop()

# --- Interface ---
message = st.text_area("Message reçu du client :", placeholder="Collez ici l'e-mail ou le message du client mécontent, indécis ou demandant un remboursement...")
ton = st.selectbox("Ton de la réponse", ["Professionnel", "Amical", "Empathique", "Ferme mais poli", "Luxe", "SAV Premium"])

if st.button("Générer la réponse professionnelle", use_container_width=True):
    if message.strip() == "":
        st.error("⚠️ Veuillez entrer un message avant de lancer la génération.")
    else:
        with st.spinner("⏳ Notre IA de support client rédige la réponse parfaite..."):
            prompt = f"""
            Tu es un expert du service client e-commerce d'élite.

            Analyse ce message client et génère une réponse professionnelle, claire et adaptée.

            Message du client :
            \"\"\"{message}\"\"\"

            Ton demandé : {ton}

            Ta réponse doit obligatoirement :
            - être polie et professionnelle
            - rassurer le client de manière chaleureuse
            - proposer une action concrète (ex : vérifier commande, demander numéro, etc.)
            - être courte, aérée et efficace
            - ne jamais inventer d'informations (laisser des crochets comme [Insérer Date] si nécessaire)
            - rester 100% réaliste

            Donne uniquement la réponse finale directement utilisable par le SAV, aucun texte d'explication avant ou après.
            """

            try:
                chat = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": "Tu es un expert en service client e-commerce."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.4,
                    max_tokens=400
                )

                # Utilisation sécurisée du format choices avec index
                reponse = chat.choices.message.content

                st.subheader("✉️ Votre réponse personnalisée")
                st.info(reponse)
                st.text_area("Copier le message brut pour votre SAV :", value=reponse, height=200)

            except Exception as e:
                st.error(f"Erreur IA : {e}")
