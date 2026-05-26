import streamlit as st
import streamlit.components.v1 as components

# 🛠️ CONFIGURATION DE LA SUITE
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
# ÉCRAN DE BIENVENUE & EXÉCUTION DES MINI APPS (CONNECTÉ)
# ------------------------------------------------------------------
else:
    # 🎯 LISTE BIEN ORDONNÉE ET EXACTE DE VOS FICHIERS (D'APRÈS VOTRE PHOTO)
    options_apps = {
        "🛡️ Mail Bouclier Pro": "pages/1_mailbouclierpro.py",
        "🏠 Créateur de Texte Immobilier": "pages/2_immobilier texte ge....py",
        "📝 Créateur de Fiche": "pages/3_createur de fiche d....py",
        "✍️ Créateur de Texte": "pages/4_createur de texte p....py",
        "📞 Script Téléphonique": "pages/5_scripte telephonique.py",
        "🧲 Aimant à Client": "pages/6_aimment a client.py",
        "📣 Créateur de Pub": "pages/7_createur de pub.py",
        "🚀 Astuces Top Performance": "pages/8_truc pour etre top ....py",
        "📊 Présentation Pro": "pages/9_truc pour genre pre....py",
        "💻 Création de Scripts": "pages/10_truc pour crée des scripte.py",
        "🔄 Automatisation des Retours": "pages/11_truc pour genre automatiser les retour.py",
        "🛠️ Détection des Pannes": "pages/12_truc pour detecter les pannes.py",
        "✒️ Bonnes Descriptions": "pages/13_truc pour gerne faire de bonne description.py",
        "✉️ Relance Emails Persuasifs": "pages/14_truc pour relancer des email persuasife.py",
        "📅 Calendrier Éditorial": "pages/15_calendrier editorial.py",
        "✨ Écritures Spéciales": "pages/16_truc pour ecrire genre des truc special.py",
        "🤝 Outils pour Convaincre": "pages/17_truc pour convaincre.py",
        "🌐 Traducteur Amélioré": "pages/18_traducteur ameliorer.py",
        "⚡ Optimisateur pour Combo": "pages/19_optimisateur pour combo.py",
        "📦 App 8en1 - Premier": "pages/20.1_ premier de l'app 8en1.py",
        "📦 App 8en1 - Deuxième": "pages/20.2 deuxieme du 8en1.py",
        "📦 App 8en1 - Partie 3": "pages/20.3 du 8en1.py",
        "📦 App 8en1 - Partie 4": "pages/20.4_du 8en1.py",
        "📦 App 8en1 - Partie 5": "pages/20.5 8en1.py",
        "📦 App 8en1 - Partie 6": "pages/20.6 de 8en1.py",
        "📦 App 8en1 - Partie 7": "pages/20.7_du 8en1.py",
        "📦 App 8en1 - Partie 8": "pages/20.8_du 8en1.py"
    }
    
    # Construction de la barre latérale
    st.sidebar.title("📱 Vos Applications")
    choix_app = st.sidebar.selectbox("Sélectionnez votre outil :", list(options_apps.keys()))
    
    # Bouton de déconnexion en bas de la barre
    st.sidebar.write("---")
    if st.sidebar.button("🚪 Se déconnecter", use_container_width=True):
        st.session_state.est_abonne_global = False
        st.rerun()

    # Lecture et exécution du fichier sélectionné
    chemin_fichier = options_apps[choix_app]
    
    try:
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            code_mini_app = f.read()
        
        # CETTE LIGNE MAGIQUE CORRIGE LE BUG : Elle affiche le vrai code de votre mini-application
        exec(code_mini_app)
        
    except FileNotFoundError:
        st.error(f"⚠️ Erreur de lecture : Le fichier `{chemin_fichier}` est introuvable dans le dossier `pages`.")
        st.info("Vérifiez que le nom du fichier sur GitHub correspond bien mot pour mot (espaces inclus).")
