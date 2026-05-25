import streamlit as st
import streamlit.components.v1 as components
from groq import Groq

# ------------------------------------------------------------------
# CONFIGURATION DE LA PLATEFORME TOUT-EN-UN (500 $/MOIS)
# ------------------------------------------------------------------
st.set_page_config(page_title="Suite IA Entreprise PRO", page_icon="🚀", layout="wide")

# Style CSS pour forcer le design épuré, la police Poppins et cacher la sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none !important;}
[data-testid="stSidebarNav"] {display: none !important;}
@import url('https://googleapis.com');
html, body, div, p, h1, h2, h3, h4, h5, h6, span, button {
    font-family: 'Poppins', sans-serif !important;
}
.menu-box {
    background-color: #1e293b; padding: 15px; border-radius: 8px;
    border: 1px solid #334155; margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# CONFIGURATION PAYPAL
# -------------------------
PAYPAL_CLIENT_ID = "DEMO"  
PAYPAL_PLAN_ID = "DEMO"    

if "est_abonne_global" not in st.session_state:
    st.session_state.est_abonne_global = False

try:
    API_KEY = st.secrets["GROQ_API_KEY"]
except:
    API_KEY = ""

# ------------------------------------------------------------------
# CAS 1 : ÉCRAN DE VERROUILLAGE (L'UTILISATEUR N'A PAS PAYÉ)
# ------------------------------------------------------------------
if not st.session_state.est_abonne_global:
    st.title("🚀 Suite Entreprise IA — Plateforme Tout-en-Un")
    st.warning("🔒 L'accès à cet écosystème est réservé aux entreprises membres de la suite Premium.")
    
    col_offre, col_connexion = st.columns(2, gap="large")
    
    with col_offre:
        st.subheader("💎 Accès Illimité à nos 20 Applications pour 500 $/mois")
        st.write("Centralisez tous vos outils de croissance : Marketing, IA, E-commerce, Logistique, Juridique et RH au même endroit.")
        st.write("Un seul abonnement unique. Paiement sécurisé par **PayPal**.")
        
        paypal_html = """
        <a href="https://paypal.com" target="_blank" style="text-decoration: none;">
            <div style="background-color: #ffc439; color: #003087; text-align: center; 
                        padding: 15px; font-weight: bold; border-radius: 4px; max-width: 350px; 
                        cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1); font-size: 16px;">
                🟨 Activer l'Abonnement Global (500 $/mois)
            </div>
        </a>
        """
        components.html(paypal_html, height=180, scrolling=False)
        
    with col_connexion:
        st.subheader("🔑 Connexion Client Entreprise")
        st.write("Entrez vos identifiants uniques pour débloquer la plateforme.")
        email = st.text_input("Adresse e-mail de l'entreprise")
        mot_de_passe = st.text_input("Mot de passe", type="password")
        
        if st.button("Débloquer la Suite Pro", use_container_width=True):
            if email == "admin@entreprise.com" and mot_de_passe == "suite500":
                st.session_state.est_abonne_global = True
                st.success("Accès global accordé !")
                st.rerun()
            else:
                st.error("Identifiants incorrects.")
# ------------------------------------------------------------------
# CAS 2 : L'UTILISATEUR EST CONNECTÉ -> TABLEAU DE BORD ACTIF
# ------------------------------------------------------------------
else:
    col_header, col_logout = st.columns()
    with col_header:
        st.title("⚡ Votre Espace Centralisé (20 Applications)")
        st.write("💼 Licence active : **Accès Entreprise Illimité (500 $/mois)**")
    with col_logout:
        st.write("") 
        if st.button("🚪 Déconnexion", use_container_width=True):
            st.session_state.est_abonne_global = False
            st.rerun()
            
    st.write("---")

    st.markdown('<div class="menu-box">⚙️ <b>Choisissez l\'application IA à exécuter :</b></div>', unsafe_allow_html=True)
    
    option = st.selectbox("", [
        "🤖 App 1 : L'App Combo 8-en-1 (Comparateur, Scraper, Calculateur...)",
        "📅 App 2 : Générateur de Calendrier Éditorial",
        "✍️ App 3 : Écrivain de Newsletters Engageantes",
        "🗺️ App 4 : Traducteur de Fiches Produits International",
        "💸 App 5 : Optimiseur d'Offres Cross-Sell & Bundles"
    ], label_visibility="collapsed")

    st.write("---")

    # ------------------------------------------------------------------
    # LOGIQUE DES MODULES (PARTIE 1)
    # ------------------------------------------------------------------
    
    if "App 1 :" in option:
        st.subheader("🤖 App 1 : L'App Combo 8-en-1")
        st.info("Interface de votre première grosse application regroupant vos 8 premiers outils (Comparateur, Calculateur de Marge, Stock Intelligent, etc.).")

    elif "App 2 :" in option:
        st.subheader("📅 App 2 : Générateur de Calendrier Éditorial")
        col_input, col_options = st.columns(2)
        with col_input:
            niche = st.text_input("Quelle est votre thématique ou produit ?", placeholder="Ex: Sneakers de collection...")
            audience = st.text_input("Quelle est votre cible / audience ?", placeholder="Ex: Jeunes urbains 18-25 ans...")
        with col_options:
            reseau = st.selectbox("Réseau social principal", ["📸 Instagram / Facebook", "💼 LinkedIn PRO", "🎵 TikTok / Reels", "📌 Pinterest"])
            frequence = st.selectbox("Nombre d'idées de contenu demandées", ["7 jours (Express)", "14 jours (Standard)", "30 jours (Complet)"])
        
        generer = st.button("🚀 Générer le Calendrier Éditorial Pro", use_container_width=True)
        if generer:
            if not niche: st.error("⚠️ Veuillez indiquer votre thématique ou produit.")
            else:
                with st.spinner("L'IA conçoit votre stratégie de contenu..."):
                    try:
                        client = Groq(api_key=API_KEY)
                        prompt_systeme = "Tu es un expert en stratégie de contenu. Génère un plan sous forme de tableau Markdown avec 4 colonnes : Jour, Objectif du post, Sujet & Accroche, Hashtags. Ne fais aucune introduction ni conclusion."
                        reponse = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[
                                {"role": "system", "content": prompt_systeme},
                                {"role": "user", "content": f"Thématique: {niche}. Cible: {audience}. Réseau: {reseau}. Durée: {frequence}."}
                            ],
                            temperature=0.7
                        )
                        st.markdown(reponse.choices.message.content)
                    except Exception as e: st.error(f"Erreur technique Groq : {str(e)}")

    elif "App 3 :" in option:
        st.subheader("✍️ App 3 : Écrivain de Newsletters Engageantes")
        col_input, col_options = st.columns(2)
        with col_input:
            sujet = st.text_area("Sujet ou objectif de la newsletter", placeholder="Ex: Lancement de notre produit...")
            offre = st.text_input("Code promo ou appel à l'action", placeholder="Ex: -20% avec CODE20")
        with col_options:
            style = st.selectbox("Style", ["📣 Promotionnel", "📖 Storytelling", "💡 Valeur/Conseils"])
            ton = st.selectbox("Ton", ["Amical", "Professionnel", "Direct"])

        generer = st.button("🚀 Rédiger la Newsletter Pro", use_container_width=True)
        if generer:
            if not sujet: st.error("⚠️ Veuillez indiquer le sujet.")
            else:
                with st.spinner("Rédaction de la newsletter..."):
                    try:
                        client = Groq(api_key=API_KEY)
                        prompt_systeme = "Tu es un copywriter. Rédige 3 objets d'e-mail percutants suivis du corps de la newsletter. Pas d'intro ni de conclusion."
                        reponse = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[
                                {"role": "system", "content": prompt_systeme},
                                {"role": "user", "content": f"Sujet: {sujet}. Offre: {offre}. Style: {style}. Ton: {ton}."}
                            ],
                            temperature=0.7
                        )
                        st.markdown(reponse.choices.message.content)
                    except Exception as e: st.error(f"Erreur : {str(e)}")
    # ------------------------------------------------------------------
    # LOGIQUE DES MODULES (PARTIE 2)
    # ------------------------------------------------------------------
    elif "App 4 :" in option:
        st.subheader("🗺️ App 4 : Traducteur de Fiches Produits International")
        col_text, col_langs = st.columns(2)
        with col_text:
            texte_origine = st.text_area("Fiche produit originale", height=200, placeholder="Texte à traduire...")
        with col_langs:
            langue_cible = st.selectbox("Langue cible", ["🇺🇸 Anglais (USA)", "🇩🇪 Allemand", "🇪🇸 Espagnol", "🇮🇹 Italien"])
            optimisation = st.checkbox("Optimiser le copywriting local", value=True)

        generer = st.button("🚀 Lancer la Traduction Stratégique", use_container_width=True)
        if generer:
            if not texte_origine: st.error("⚠️ Ajoutez du texte.")
            else:
                with st.spinner("Traduction en cours..."):
                    try:
                        client = Groq(api_key=API_KEY)
                        prompt_systeme = "Tu es un traducteur expert. Adapte le ton marketing et renvoie directement le texte traduit en Markdown, sans introduction."
                        reponse = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[
                                {"role": "system", "content": prompt_systeme},
                                {"role": "user", "content": f"Traduire en {langue_cible}. Texte : {texte_origine}. Optimisation locale: {optimisation}"}
                            ],
                            temperature=0.4
                        )
                        st.markdown(reponse.choices.message.content)
                    except Exception as e: st.error(f"Erreur : {str(e)}")

    elif "App 5 :" in option:
        st.subheader("💸 App 5 : Optimiseur d'Offres Cross-Sell & Bundles")
        col_prod, col_strat = st.columns(2)
        with col_prod:
            produit_principal = st.text_input("Produit phare", placeholder="Ex: Crème hydratante bio...")
            prix_principal = st.number_input("Prix ($)", min_value=1.0, value=40.0)
            details = st.text_area("Description courte", placeholder="Bénéfices clés...")
        with col_strat:
            type_offre = st.selectbox("Stratégie", ["🔥 Le Bundle Parfait", "⚡ L'Upsell Post-Achat", "🤝 Le Cross-Sell de Panier"])
            agressivite = st.select_slider("Persuasion", options=["Discret", "Équilibré", "Très Persuasif"])

        generer = st.button("🚀 Générer la Stratégie", use_container_width=True)
        if generer:
            if not produit_principal: st.error("⚠️ Indiquez le produit.")
            else:
                with st.spinner("Génération des offres..."):
                    try:
                        client = Groq(api_key=API_KEY)
                        prompt_systeme = "Tu es un expert CRO. Rédige une offre de bundle, la liste des produits complémentaires et le script de vente. Pas de blabla, va droit au but."
                        reponse = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[
                                {"role": "system", "content": prompt_systeme},
                                {"role": "user", "content": f"Produit: {produit_principal} ({prix_principal}$). Description: {details}. Stratégie: {type_offre}. Force: {agressivite}."}
                            ],
                            temperature=0.7
                        )
                        st.markdown(reponse.choices.message.content)
                    except Exception as e: st.error(f"Erreur : {str(e)}")


