import streamlit as st
import streamlit.components.v1 as components

# 🛠️ CONFIGURATION : Barre latérale forcée
st.set_page_config(
    page_title="Suite IA Entreprise PRO", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="expanded"
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
        email = st.text_input("Adresse e-mail")
        mot_de_passe = st.text_input("Mot de passe", type="password")
        
        if st.button("Débloquer la Suite Pro", use_container_width=True):
            if email == "admin@entreprise.com" and mot_de_passe == "suite500":
                st.session_state.est_abonne_global = True
                st.success("Accès accordé !")
                st.rerun()
            else:
                st.error("Identifiants incorrects ou abonnement inactif.")

# ------------------------------------------------------------------
# ÉCRAN DE BIENVENUE & BARRE LATÉRALE (L'UTILISATEUR EST CONNECTÉ)
# ------------------------------------------------------------------
else:
    # 🌟 CORRECTION ICI : Création de la liste des 28 applications
    liste_apps = [f"🛠️ Application {i}" for i in range(1, 29)]
    
    # Ajout du titre et du sélecteur directement DANS la barre latérale
    st.sidebar.title("📱 Vos 28 Applications")
    st.sidebar.write("Sélectionnez votre outil :")
    choix_app = st.sidebar.selectbox("Navigation", liste_apps, label_visibility="collapsed")
    
    # Bouton de déconnexion placé en bas de la barre latérale
    st.sidebar.write("---")
    if st.sidebar.button("🚪 Se déconnecter", use_container_width=True):
        st.session_state.est_abonne_global = False
        st.rerun()

    # Contenu de l'application principale selon le choix de l'utilisateur
    st.title(f"⚡ {choix_app}")
    st.success("🔓 Vos accès globaux sont actifs.")
    
    # Structure conditionnelle pour afficher le bon module
    if choix_app == "🛠️ Application 1":
        st.subheader("Bienvenue dans l'outil de gestion 1")
        st.info("Insérez ici le code spécifique à votre première mini-app.")
        # Ajoutez vos inputs, graphiques ou fonctions de l'app 1 ici...
        
    elif choix_app == "🛠️ Application 2":
        st.subheader("Bienvenue dans l'outil d'analyse 2")
        st.info("Insérez ici le code spécifique à votre deuxième mini-app.")
        
    # Répétez le pattern `elif` pour vos autres applications spécifiques...
    else:
        st.write("Le contenu de cette application sera configuré ici.")
