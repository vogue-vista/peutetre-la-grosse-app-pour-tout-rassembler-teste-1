import streamlit as st
import streamlit.components.v1 as components

# Configuration globale
st.set_page_config(page_title="Suite IA Entreprise PRO", page_icon="🚀", layout="wide")

# Session state de connexion
if "est_abonne_global" not in st.session_state:
    st.session_state.est_abonne_global = False

# Masquer le menu de navigation si pas connecté
if not st.session_state.est_abonne_global:
    st.markdown("<style>[data-testid='stSidebar'] {display: none !important;}</style>", unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://googleapis.com');
html, body, div, p, h1, h2, h3, h4, h5, h6, span, button { font-family: 'Poppins', sans-serif !important; }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# SYSTEME DE VERROUILLAGE PAYPAL
# ------------------------------------------------------------------
if not st.session_state.est_abonne_global:
    st.title("🚀 Suite Entreprise IA — Plateforme Tout-en-Un")
    st.warning("🔒 L'accès à cet écosystème est réservé aux membres Premium.")
    
    col_offre, col_connexion = st.columns(2, gap="large")
    
    with col_offre:
        st.subheader("💎 Accès Illimité à nos 20 Applications pour 500 $/mois")
        st.write("Un seul abonnement unique. Paiement sécurisé par PayPal.")
        
        paypal_html = """
        <a href="https://paypal.com" target="_blank" style="text-decoration: none;">
            <div style="background-color: #ffc439; color: #003087; text-align: center; padding: 15px; font-weight: bold; border-radius: 4px; max-width: 350px;">
                🟨 Activer l'Abonnement Global (500 $/mois)
            </div>
        </a>
        """
        components.html(paypal_html, height=100, scrolling=False)
        
    with col_connexion:
        st.subheader("🔑 Connexion Client Entreprise")
        email = st.text_input("Adresse e-mail")
        mot_de_passe = st.text_input("Mot de passe", type="password")
        
        if st.button("Débloquer la Suite Pro", use_container_width=True):
            if email == "admin@entreprise.com" and mot_de_passe == "suite500":
                st.session_state.est_abonne_global = True
                st.success("Accès accordé !")
                st.rerun()
            else:
                st.error("Identifiants incorrects.")

# ------------------------------------------------------------------
# CAS CONNECTÉ : SYSTEME DE NAVIGATION PAR FICHIERS DISTINCTS
# ------------------------------------------------------------------
else:
    # On définit les pages en pointant directement sur tes fichiers .py
    pages_disponibles = {
        "📊 Accueil & Déconnexion": st.Page(lambda: accueil_dashboard(), title="Tableau de Bord", icon="👋"),
        "📅 Application 2": st.Page("calendrier.py", title="Générateur Calendrier", icon="📅"),
        "✍️ Application 3": st.Page("newsletter.py", title="Écrivain Newsletter", icon="✍️"),
        "🗺️ Application 4": st.Page("traducteur.py", title="Traducteur International", icon="🗺️"),
        "💸 Application 5": st.Page("cross_sell.py", title="Optimiseur Cross-Sell", icon="💸")
    }
    
    # On lance la navigation Streamlit
    pg = st.navigation(list(pages_disponibles.values()))
    pg.run()

# Petite fonction pour l'écran d'accueil une fois connecté
def accueil_dashboard():
    st.title("⚡ Bienvenue dans votre Espace Centralisé")
    st.success("🔓 Vos accès sont actifs. Utilisez le menu latéral à gauche pour ouvrir vos applications !")
    if st.button("🚪 Se déconnecter de la plateforme", use_container_width=True):
        st.session_state.est_abonne_global = False
        st.rerun()




