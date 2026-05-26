import streamlit as st
import streamlit.components.v1 as components

# 🛠️ CONFIGURATION INITIALE
st.set_page_config(page_title="Suite IA Entreprise PRO", page_icon="🚀", layout="wide")

if "est_abonne_global" not in st.session_state:
    st.session_state.est_abonne_global = False

# Configuration PayPal
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
        components.html(f"""
        <div id="paypal-button-container-suite" style="max-width: 350px; margin-top: 20px;"></div>
        <script src="https://paypal.com{PAYPAL_CLIENT_ID}&vault=true&intent=subscription"></script>
        <script>
          paypal.Buttons({{
              style: {{ shape: 'rect', color: 'gold', layout: 'vertical', label: 'subscribe' }},
              createSubscription: function(data, actions) {{ return actions.subscription.create({{ 'plan_id': '{PAYPAL_PLAN_ID}' }}); }},
              onApprove: function(data, actions) {{ alert('Succès !'); }}
          }}).render('#paypal-button-container-suite');
        </script>
        """, height=180)
        
    with col_connexion:
        st.subheader("🔑 Connexion Client Entreprise")
        email = st.text_input("Adresse e-mail")
        mot_de_passe = st.text_input("Mot de passe", type="password")
        if st.button("Débloquer la Suite Pro", use_container_width=True):
            if email == "admin@entreprise.com" and mot_de_passe == "suite500":
                st.session_state.est_abonne_global = True
                st.rerun()
            else:
                st.error("Identifiants incorrects.")

# ------------------------------------------------------------------
# ÉCRAN DE BIENVENUE & CHARGEMENT DES PAGES (CONNECTÉ)
# ------------------------------------------------------------------
else:
    # Déclaration des pages de votre dossier 'pages'
    # Remplacez "Nom_du_Fichier.py" par les vrais noms de vos fichiers
    pages_disponibles = [
        st.Page("pages/app1.py", title="🛠️ Application 1", icon="📊"),
        st.Page("pages/app2.py", title="🛠️ Application 2", icon="📈"),
        # Ajoutez vos 28 pages ici sur le même modèle...
    ]
    
    # Injection du bouton de déconnexion dans la barre latérale
    with st.sidebar:
        st.title("📱 Vos 28 Applications")
        if st.button("🚪 Se déconnecter", use_container_width=True):
            st.session_state.est_abonne_global = False
            st.rerun()
        st.write("---")
        
    # Initialisation de la navigation avec vos pages
    pg = st.navigation(pages_disponibles)
    pg.run()
