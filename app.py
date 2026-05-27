import streamlit as st
import importlib
import os

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Suite IA Entreprise PRO",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# SESSION
# ---------------------------------------------------------
if "est_abonne_global" not in st.session_state:
    st.session_state.est_abonne_global = False

# ---------------------------------------------------------
# STYLE GLOBAL
# ---------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

html, body, div, p, h1, h2, h3, h4, h5, h6, span, button {
    font-family: 'Poppins', sans-serif !important;
}

[data-testid="stSidebarNav"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# ÉCRAN DE VERROUILLAGE
# ---------------------------------------------------------
if not st.session_state.est_abonne_global:

    st.title("🚀 Suite Entreprise IA — Plateforme Tout-en-Un")
    st.warning("🔒 L'accès à cet écosystème est réservé aux membres Premium.")

    col_offre, col_connexion = st.columns(2, gap="large")

    # -------------------------
    # COLONNE GAUCHE : ABONNEMENT
    # -------------------------
    with col_offre:
        st.subheader("💎 Accès Illimité à nos 28 Applications — 500 $/mois")
        st.write("👉 Paiement sécurisé par Virement Interac.")

        st.write("---")
        st.markdown("### 📢 Obtenir vos accès :")

        nom_pme = st.text_input("Nom de votre entreprise")
        courriel_pme = st.text_input("Courriel professionnel")

        if st.button("🚀 Demander mes accès"):
            if nom_pme and courriel_pme:
                st.success(f"Demande enregistrée pour {nom_pme} !")
                st.info("""
                📥 **Instructions envoyées !**

                Effectuez votre virement de **500,00 $** à :
                ➡️ **virement@votre-courriel.com**

                Vos accès seront activés dès réception.
                """)
            else:
                st.error("Veuillez remplir toutes les cases.")

    # -------------------------
    # COLONNE DROITE : CONNEXION
    # -------------------------
    with col_connexion:
        st.subheader("🔑 Connexion Client Entreprise")

        email = st.text_input("Adresse e-mail")
        mot_de_passe = st.text_input("Mot de passe", type="password")

        if st.button("Débloquer la Suite Pro"):
            if email == "admin@entreprise.com" and mot_de_passe == "suite500":
                st.session_state.est_abonne_global = True
                st.success("Accès accordé !")
                st.rerun()
            else:
                st.error("Identifiants incorrects.")

# ---------------------------------------------------------
# INTERFACE PRINCIPALE (CONNECTÉ)
# ---------------------------------------------------------
else:

    # -------------------------
    # SIDEBAR
    # -------------------------
    with st.sidebar:
        st.title("🚀 Suite Pro 500$/mo")
        st.write("Connecté : admin@entreprise.com")

        if st.button("🚪 Se déconnecter", use_container_width=True):
            st.session_state.est_abonne_global = False
            st.rerun()

        st.write("---")

        # Chargement des mini-apps
        dossier_pages = "pages"
        fichiers_apps = {}

        if os.path.exists(dossier_pages):
            fichiers = sorted([f for f in os.listdir(dossier_pages) if f.endswith(".py")])
            for f in fichiers:
                nom_propre = f.replace(".py", "").replace("_", " ").title()
                fichiers_apps[nom_propre] = f.replace(".py", "")

        choix_app = st.selectbox("📂 Sélectionnez votre application :", list(fichiers_apps.keys()))

    # -------------------------
    # ZONE PRINCIPALE
    # -------------------------
    if choix_app:
        module_name = fichiers_apps[choix_app]
        module_path = f"pages.{module_name}"

        try:
            module = importlib.import_module(module_path)

            if hasattr(module, "app"):
                module.app()
            else:
                st.error(f"L'application '{choix_app}' ne contient pas de fonction app().")

        except Exception as e:
            st.error(f"Erreur dans l'application : {choix_app}")
            st.warning(str(e))

    else:
        st.title("⚡ Bienvenue dans votre Suite IA Entreprise PRO")
        st.info("Aucune application trouvée dans le dossier `pages`.")
