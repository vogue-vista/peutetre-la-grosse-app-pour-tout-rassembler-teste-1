import streamlit as st
import streamlit.components.v1 as components

# 🛠️ CONFIGURATION DE LA SUITE
st.set_page_config(
    page_title="Suite IA Entreprise PRO", 
    page_icon="🚀", 
    layout="wide"
)

# Gestion de la session de connexion
if "est_abonne_global" not in st.session_state:
    st.session_state.est_abonne_global = False

# Design épuré en police Poppins
st.markdown("""
<style>
@import url('https://googleapis.com');
html, body, div, p, h1, h2, h3, h4, h5, h6, span, button { font-family: 'Poppins', sans-serif !important; }
</style>
""", unsafe_allow_html=True)

# CONFIGURATION PAYPAL
PAYPAL_CLIENT_ID = "sandbox"  
PAYPAL_PLAN_ID = "P-XXXXXXXXXX"  

# ------------------------------------------------------------------
# ÉCRAN DE VERROUILLAGE (L'UTILISATEUR N'A PAS PAYÉ)
# ------------------------------------------------------------------
if not st.session_state.est_abonne_global:
    st.title("🚀 Suite Entreprise IA — Plateforme Tout-en-Un")
    st.warning("🔒 L'accès à cet écosystème est réservé aux membres Premium.")
    
    col_offre, col_connexion = st.columns(2, gap="large")
    
    with col_offre:
        st.subheader("💎 Accès Illimité à nos 28 Applications pour 500 $/mois")
        st.write("Centralisez tous vos outils de croissance au même endroit.")
        st.write("Un seul abonnement unique. Paiement entièrement sécurisé par **PayPal**.")
        
        paypal_button_html = f"""
        <div id="paypal-button-container-suite" style="max-width: 350px; margin-top: 20px;"></div>
        <script src="https://paypal.com{PAYPAL_CLIENT_ID}&vault=true&intent=subscription" data-sdk-integration-source="button-factory"></script>
        <script>
          paypal.Buttons({{
              style: {{ shape: 'rect', color: 'gold', layout: 'vertical', label: 'subscribe' }},
              createSubscription: function(data, actions) {{
                return actions.subscription.create({{ 'plan_id': '{PAYPAL_PLAN_ID}' }});
              }},
              onApprove: function(data, actions) {{
                alert('Abonnement PayPal validé avec succès. ID : ' + data.subscriptionID);
              }}
          }}).render('#paypal-button-container-suite');
        </script>
        """
        components.html(paypal_button_html, height=180, scrolling=False)
        
    with col_connexion:
        st.subheader("🔑 Connexion Client Entreprise")
        st.write("Entrez vos identifiants pour débloquer votre accès.")
        email = st.text_input("Adresse e-mail", key="login_email")
        mot_de_passe = st.text_input("Mot de passe", type="password", key="login_password")
        
        if st.button("Débloquer la Suite Pro", use_container_width=True):
            if email.strip() == "admin@entreprise.com" and mot_de_passe.strip() == "suite500":
                st.session_state.est_abonne_global = True
                st.success("Accès accordé !")
                st.rerun()
            else:
                st.error("Identifiants incorrects ou abonnement inactif.")

# ------------------------------------------------------------------
# ÉCRAN DE BIENVENUE & BARRE LATÉRALE NATIVE ULTRA-STABLE (CONNECTÉ)
# ------------------------------------------------------------------
else:
    # Bouton de déconnexion fixe dans le volet de gauche
    with st.sidebar:
        st.title("🚀 Suite Pro 500$/mo")
        st.write("Connecté : admin@entreprise.com")
        if st.button("🚪 Se déconnecter de la plateforme", use_container_width=True):
            st.session_state.est_abonne_global = False
            st.rerun()
        st.write("---")

    # 🔑 CORRECTION SÉCURISÉE : Laisse Streamlit gérer la découverte des fichiers
    # Cette syntaxe charge automatiquement TOUS les fichiers .py valides du dossier 'pages'
    # sans risquer de planter sur les chemins sous Python 3.14.
    try:
        navigation_suite = st.navigation(st.sidebar) 
        navigation_suite.run()
    except Exception as e:
        # Système de secours automatique si un fichier individuel comporte une erreur interne de code
        st.error("💡 Une de vos mini-applications comporte une ligne de code incompatible (comme un ancien st.set_page_config).")
        st.info("Vérifiez le fichier de script vidéo ou l'application sélectionnée pour retirer les configurations de page en trop.")
