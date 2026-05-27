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
        st.write("👉 **Formule Entreprise Pro :** Facturation mensuelle et paiement sécurisé par Virement Interac.")
        
        st.write("---")
        st.markdown("### 📢 Obtenir vos accès en 5 minutes :")
        st.write("Pour abonner votre PME, veuillez remplir ce formulaire. Vous recevrez instantanément les instructions de virement par courriel.")
        
        # Formulaire d'inscription simple pour les entreprises
        nom_pme = st.text_input("Nom de votre entreprise", key="reg_pme")
        courriel_pme = st.text_input("Courriel professionnel de contact", key="reg_email")
        
        if st.button("🚀 Demander mes accès et recevoir la facture", use_container_width=True):
            if nom_pme and courriel_pme:
                st.success(f"✅ Demande enregistrée avec succès pour {nom_pme} !")
                # Modifie l'adresse courriel ci-dessous par celle de ton choix pour le virement
                st.info("""
                📥 **Instructions envoyées !** 
                
                Pour activer vos identifiants immédiatement, veuillez effectuer votre virement de **500,00 $** à l'adresse suivante :
                ➡️ **virement@votre-courriel.com**
                
                *Dès réception, vos codes d'accès 'admin@entreprise.com' seront activés à distance.*
                """)
            else:
                st.error("⚠️ Veuillez remplir toutes les cases pour valider votre demande.")
        
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

    # Masquage de sécurité de la liste du haut
    st.markdown("""
    <style>
    [data-testid="stSidebarNav"] { display: none !important; }
    [data-testid="stSidebar"] { display: flex !important; }
    </style>
    """, unsafe_allow_html=True)

    dossier_pages = "pages"
    fichiers_apps = {}

    # Scan du dossier pages
    if os.path.exists(dossier_pages):
        fichiers = sorted([f for f in os.listdir(dossier_pages) if f.endswith(".py")])
        for f in fichiers:
            nom_propre = f.replace(".py", "").replace("_", " ").title()
            fichiers_apps[nom_propre] = os.path.join(dossier_pages, f)

    # Construction de la barre latérale manuelle
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
            
            # Filtre automatique anti-masquage
            code_mini_app = code_mini_app.replace('display: none !important;', 'display: flex !important;')
            code_mini_app = code_mini_app.replace('[data-testid="stSidebar"] {display: none !important;}', '')
            
            # Exécution de la mini-app
            exec(code_mini_app, globals())
            
            # Ré-injection du masquage de la barre du haut
            st.markdown("<style>[data-testid='stSidebarNav'] { display: none !important; }</style>", unsafe_allow_html=True)
            
        except Exception as e:
            st.title(f"❌ Erreur dans l'application : {choix_app}")
            st.error(f"Le fichier `{chemin_complet}` contient une erreur de code interne.")
            st.warning(f"Détail technique : {str(e)}")
            st.markdown("<style>[data-testid='stSidebarNav'] { display: none !important; }</style>", unsafe_allow_html=True)
    else:
        st.title("⚡ Bienvenue dans votre Suite IA Entreprise PRO")
        st.info("Aucun fichier détecté dans le dossier `pages`.")
