import streamlit as st
import streamlit.components.v1 as components

# 🛠️ CONFIGURATION DE LA BARRE LATÉRALE NATIVE
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
# ÉCRAN DE BIENVENUE & VRAIE BARRE LATÉRALE NATIVE (CONNECTÉ)
# ------------------------------------------------------------------
else:
    # 1. On crée le bouton de déconnexion tout en haut de la barre de gauche
    with st.sidebar:
        st.title("🚀 Suite Pro 500$/mo")
        st.write(f"Connecté en tant que: admin@entreprise.com")
        if st.button("🚪 Se déconnecter de la plateforme", use_container_width=True):
            st.session_state.est_abonne_global = False
            st.rerun()
        st.write("---") # Ligne de séparation esthétique

    # 2. On déclare la liste de vos 28 fichiers pour créer la barre latérale native
    # Streamlit va lire directement dans votre dossier 'pages' réparé
    pages_disponibles = [
        st.Page("pages/1_mailbouclierpro.py", title="🛡️ Mail Bouclier Pro"),
        st.Page("pages/2_immobilier texte ge....py", title="🏠 Créateur Texte Immobilier"),
        st.Page("pages/3_createur de fiche d....py", title="📝 Créateur de Fiche"),
        st.Page("pages/4_createur de texte p....py", title="✍️ Créateur de Texte"),
        st.Page("pages/5_scripte telephonique.py", title="📞 Script Téléphonique"),
        st.Page("pages/6_aimment a client.py", title="🧲 Aimant à Client"),
        st.Page("pages/7_createur de pub.py", title="📣 Créateur de Pub"),
        st.Page("pages/8_truc pour etre top ....py", title="🚀 Astuces Top Performance"),
        st.Page("pages/9_truc pour genre pre....py", title="📊 Présentation Pro"),
        st.Page("pages/10_truc pour crée des scripte.py", title="💻 Création de Scripts"),
        st.Page("pages/11_truc pour genre automatiser les retour.py", title="🔄 Automatisation Retours"),
        st.Page("pages/12_truc pour detecter les pannes.py", title="🛠️ Détection des Pannes"),
        st.Page("pages/13_truc pour gerne faire de bonne description.py", title="✒️ Bonnes Descriptions"),
        st.Page("pages/14_truc pour relancer des email persuasife.py", title="✉️ Relance Emails"),
        st.Page("pages/15_calendrier editorial.py", title="📅 Calendrier Éditorial"),
        st.Page("pages/16_truc pour ecrire genre des truc special.py", title="✨ Écritures Spéciales"),
        st.Page("pages/17_truc pour convaincre.py", title="🤝 Outils pour Convaincre"),
        st.Page("pages/18_traducteur ameliorer.py", title="🌐 Traducteur Amélioré"),
        st.Page("pages/19_optimisateur pour combo.py", title="⚡ Optimisateur Combo"),
        st.Page("pages/20.1_ premier de l'app 8en1.py", title="📦 App 8en1 - Premier"),
        st.Page("pages/20.2 deuxieme du 8en1.py", title="📦 App 8en1 - Deuxième"),
        st.Page("pages/20.3 du 8en1.py", title="📦 App 8en1 - Partie 3"),
        st.Page("pages/20.4_du 8en1.py", title="📦 App 8en1 - Partie 4"),
        st.Page("pages/20.5 8en1.py", title="📦 App 8en1 - Partie 5"),
        st.Page("pages/20.6 de 8en1.py", title="📦 App 8en1 - Partie 6"),
        st.Page("pages/20.7_du 8en1.py", title="📦 App 8en1 - Partie 7"),
        st.Page("pages/20.8_du 8en1.py", title="📦 App 8en1 - Partie 8")
    ]
    
    # 3. La commande officielle de Streamlit pour lancer la navigation native à gauche
    navigation_suite = st.navigation(pages_disponibles)
    navigation_suite.run()
