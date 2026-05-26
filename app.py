import streamlit as st
import streamlit.components.v1 as components
import os

# 🛠️ CONFIGURATION DE LA BARRE LATÉRALE FORCÉE
st.set_page_config(
    page_title="Suite IA Entreprise PRO", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Gestion de la session de connexion globale
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
                st.session_state.est_abonne = True 
                st.success("Accès accordé !")
                st.rerun()
            else:
                st.error("Identifiants incorrects ou abonnement inactif.")

# ------------------------------------------------------------------
# ÉCRAN DE BIENVENUE & BARRE LATÉRALE VERSION 2 (CONNECTÉ)
# ------------------------------------------------------------------
else:
    st.session_state.est_abonne = True

    # 🔑 MASQUAGE DE LA LISTE DU HAUT (Spécifique Option 2)
    # Ce code CSS cache la navigation automatique du haut pour ne garder que votre sélecteur jaune
    st.markdown("""
    <style>
    [data-testid="stSidebarNav"] { display: none !important; }
    [data-testid="stSidebar"] { display: flex !important; }
    </style>
    """, unsafe_allow_html=True)

    dossier_pages = "pages"
    fichiers_apps = {}

    # Scan du dossier pour lister vos applications
    if os.path.exists(dossier_pages):
        fichiers = sorted([f for f in os.listdir(dossier_pages) if f.endswith(".py")])
        for f in fichiers:
            nom_propre = f.replace(".py", "").replace("_", " ").title()
            fichiers_apps[nom_propre] = os.path.join(dossier_pages, f)

    # Construction forcée de votre barre latérale manuelle
    with st.sidebar:
        st.title("🚀 Suite Pro 500$/mo")
        st.write("Connecté : admin@entreprise.com")
        
        if st.button("🚪 Se déconnecter de la plateforme", use_container_width=True):
            st.session_state.est_abonne_global = False
            st.session_state.est_abonne = False
            st.rerun()
            
        st.write("---")
        
        if fichiers_apps:
            choix_app = st.selectbox("📂 Sélectionnez votre application :", list(fichiers_apps.keys()))
        else:
            choix_app = None

    # Zone principale d'affichage
    if choix_app:
        chemin_complet = fichiers_apps[choix_app]
        
        try:
            with open(chemin_complet, "r", encoding="utf-8") as file:
                code_mini_app = file.read()
            
            # Filtre automatique anti-masquage de la barre latérale pour vos fichiers
            code_mini_app = code_mini_app.replace('display: none !important;', 'display: flex !important;')
            code_mini_app = code_mini_app.replace('[data-testid="stSidebar"] {display: none !important;}', '')
            
            # Exécution de la mini-app avec accès global pour réparer le pack 8en1
            exec(code_mini_app, globals())
            
        except Exception as e:
            st.title(f"❌ Erreur dans l'application : {choix_app}")
            st.error(f"Le fichier `{chemin_complet}` contient une erreur de code interne.")
            st.warning(f"Détail technique : {str(e)}")
    else:
        st.title("⚡ Bienvenue dans votre Suite IA Entreprise PRO")
        st.info("Aucun fichier détecté dans le dossier `pages`.")
