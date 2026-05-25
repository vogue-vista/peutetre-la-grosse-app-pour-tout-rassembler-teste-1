import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Suite IA Entreprise PRO", page_icon="🚀", layout="wide")

# Masquer la sidebar native si l'utilisateur n'est pas connecté
if "est_abonne_global" not in st.session_state:
    st.session_state.est_abonne_global = False

if not st.session_state.est_abonne_global:
    st.markdown("<style>[data-testid='stSidebar'] {display: none !important;}</style>", unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://googleapis.com');
html, body, div, p, h1, h2, h3, h4, h5, h6, span, button { font-family: 'Poppins', sans-serif !important; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# MUR DE PAIEMENT PAYPAL & CONNEXION
# -------------------------
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
                st.success("Accès accordé ! Utilisez le menu à gauche pour naviguer.")
                st.rerun()
            else:
                st.error("Identifiants incorrects.")
else:
    st.title("⚡ Bienvenue dans votre Espace Centralisé")
    st.success("🔓 Vos accès sont actifs. Utilisez la barre latérale (Sidebar) à gauche pour ouvrir vos applications !")
    
    if st.button("🚪 Se déconnecter", use_container_width=True):
        st.session_state.est_abonne_global = False
        st.rerun()



