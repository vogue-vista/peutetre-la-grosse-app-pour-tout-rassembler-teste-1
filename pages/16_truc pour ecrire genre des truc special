import streamlit as st
import streamlit.components.v1 as components
from groq import Groq

# L'application vérifie la mémoire globale :
if "est_abonne_global" not in st.session_state or not st.session_state.est_abonne_global:
    st.warning("🔒 Veuillez vous connecter sur la page d'accueil.")
    st.stop()  # Si pas payé, le code s'arrête net ici !


# -------------------------
# CONFIGURATION DE LA PAGE
# -------------------------

st.markdown("""
<style>
[data-testid="stSidebar"] {display: none !important;}
[data-testid="stSidebarNav"] {display: none !important;}
@import url('https://googleapis.com');
html, body, div, p, h1, h2, h3, h4, h5, h6, span {
    font-family: 'Poppins', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

PAYPAL_CLIENT_ID = "DEMO"
PAYPAL_PLAN_ID = "DEMO"

if "est_abonne" not in st.session_state:
    st.session_state.est_abonne = False

try:
    API_KEY = st.secrets["GROQ_API_KEY"]
except:
    API_KEY = ""

st.title("✍️ Écrivain de Newsletters IA — Version Pro")

if not st.session_state.est_abonne:
    st.warning("🔒 Cette application est réservée aux membres de la version Premium.")
    col_offre, col_connexion = st.columns(2, gap="large")
    
    with col_offre:
        st.subheader("🚀 Débloquez l'IA pour 20 $/mois")
        st.write("Rédigez des newsletters captivantes pour engager votre liste et exploser vos ventes.")
        paypal_html = """
        <a href="https://paypal.com" target="_blank" style="text-decoration: none;">
            <div style="background-color: #ffc439; color: #003087; text-align: center; padding: 12px; font-weight: bold; border-radius: 4px; max-width: 300px;">
                🟨 S'abonner avec PayPal (Démo)
            </div>
        </a>
        """
        components.html(paypal_html, height=150, scrolling=False)
        
    with col_connexion:
        st.subheader("🔑 Déjà abonné ?")
        email = st.text_input("Adresse e-mail")
        mot_de_passe = st.text_input("Mot de passe", type="password")
        if st.button("Se connecter", use_container_width=True):
            if email == "test@client.com" and mot_de_passe == "access20":
                st.session_state.est_abonne = True
                st.rerun()
            else:
                st.error("Identifiants incorrects.")
else:
    st.write("✨ Espace Premium Actif.")
    if st.button("🚪 Se déconnecter"):
        st.session_state.est_abonne = False
        st.rerun()

    with st.container(border=True):
        col_input, col_options = st.columns(2)
        with col_input:
            sujet = st.text_area("Sujet ou objectif de la newsletter", placeholder="Ex: Lancement de notre produit...")
            offre = st.text_input("Code promo ou appel à l'action", placeholder="Ex: -20% avec CODE20")
        with col_options:
            style = st.selectbox("Style", ["📣 Promotionnel", "📖 Storytelling", "💡 Valeur/Conseils"])
            ton = st.selectbox("Ton", ["Amical", "Professionnel", "Direct"])

        generer = st.button("🚀 Rédiger la Newsletter Pro", use_container_width=True)

    if generer:
        if not API_KEY:
            st.error("⚠️ Clé manquante.")
        elif not sujet:
            st.error("⚠️ Indiquez le sujet.")
        else:
            with st.spinner("Rdaction de la newsletter..."):
                try:
                    client = Groq(api_key=API_KEY)
                    prompt_systeme = "Tu es un copywriter. Rédige 3 objets d'e-mail percutants suivis du corps de la newsletter. Pas d'intro ni de conclusion."
                    reponse = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": prompt_systeme},
                            {"role": "user", "content": f"Sujet: {sujet}. Offre: {offre}. Style: {style}. Ton: {ton}."}
                        ],
                        temperature=0.7
                    )
                    email_genere = reponse.choices[0].message.content
                    st.success("✨ Newsletter prête !")
                    st.markdown(email_genere)
                except Exception as e:
                    st.error(f"Erreur : {str(e)}")
