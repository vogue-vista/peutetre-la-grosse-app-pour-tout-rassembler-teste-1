import streamlit as st
import streamlit.components.v1 as components
from groq import Groq

# L'application vérifie la mémoire globale :
if "est_abonne_global" not in st.session_state or not st.session_state.est_abonne_global:
    st.warning("🔒 Veuillez vous connecter sur la page d'accueil.")
    st.stop()  # Si pas payé, le code s'arrête net ici !


# -------------------------
# CONFIGURATION DE LA PAGE
# -------------------------

# Design pro et suppression de la sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none !important;}
[data-testid="stSidebarNav"] {display: none !important;}
@import url('https://googleapis.com');
html, body, div, p, h1, h2, h3, h4, h5, h6, span {
    font-family: 'Poppins', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# CONFIGURATION PAYPAL (À REMPLIR PLUS TARD)
# -------------------------
PAYPAL_CLIENT_ID = "DEMO"  
PAYPAL_PLAN_ID = "DEMO"    

# -------------------------
# GESTION DE L'ACCÈS
# -------------------------
if "est_abonne" not in st.session_state:
    st.session_state.est_abonne = False

try:
    API_KEY = st.secrets["GROQ_API_KEY"]
except:
    API_KEY = ""

# -------------------------
# INTERFACE SÉCURISÉE
# -------------------------
st.title("🏠 ImmoText Pro")
st.subheader("Transformez vos notes brutes en annonces immobilières captivantes en 2 secondes.")

# CAS 1 : L'UTILISATEUR N'A PAS PAYÉ
if not st.session_state.est_abonne:
    st.warning("🔒 Cette application est réservée aux membres de la version Premium.")
    
    col_offre, col_connexion = st.columns(2, gap="large")
    
    with col_offre:
        st.subheader("🚀 Boostez vos ventes pour 20 $/mois")
        st.write("Générez des descriptions de biens immobiliers captivantes, rédigez des posts réseaux sociaux pour vos mandats et gagnez des heures de rédaction.")
        st.write("Le paiement est entièrement sécurisé par **PayPal**.")
        
        if PAYPAL_CLIENT_ID == "DEMO":
            paypal_html = """
            <a href="https://paypal.com" target="_blank" style="text-decoration: none;">
                <div style="background-color: #ffc439; color: #003087; text-align: center; 
                            padding: 12px; font-family: Arial, sans-serif; font-weight: bold; 
                            border-radius: 4px; max-width: 300px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    🟨 S'abonner avec PayPal (Démo)
                </div>
            </a>
            """
        else:
            paypal_html = f"""
            <div id="paypal-button-container-fixed" style="max-width: 350px; margin-top: 20px;"></div>
            <script src="https://paypal.com/sdk/js?client-id={PAYPAL_CLIENT_ID}&vault=true&intent=subscription" data-sdk-integration-source="button-factory"></script>
            <script>
              paypal.Buttons({{
                  style: {{ shape: 'rect', color: 'gold', layout: 'vertical', label: 'subscribe' }},
                  createSubscription: function(data, actions) {{
                    return actions.subscription.create({{ 'plan_id': '{PAYPAL_PLAN_ID}' }});
                  }},
                  onApprove: function(data, actions) {{
                    alert('Abonnement réussi ! ID : ' + data.subscriptionID);
                  }}
              }}).render('#paypal-button-container-fixed');
            </script>
            """
        components.html(paypal_html, height=150, scrolling=False)
        
    with col_connexion:
        st.subheader("🔑 Déjà abonné ?")
        email = st.text_input("Adresse e-mail")
        mot_de_passe = st.text_input("Mot de passe", type="password")
        
        if st.button("Se connecter", use_container_width=True):
            if email == "test@client.com" and mot_de_passe == "immo30":
                st.session_state.est_abonne = True
                st.success("Accès accordé !")
                st.rerun()
            else:
                st.error("Identifiants incorrects.")

# CAS 2 : L'UTILISATEUR EST ABONNÉ -> ACCÈS IMMOBILIER
else:
    st.write("✨ **Espace Premium Actif.** Prêt à rédiger vos mandats.")
    if st.button("🚪 Se déconnecter", key="logout"):
        st.session_state.est_abonne = False
        st.rerun()
        
    st.write("---")

    with st.container(border=True):
        col_inputs, col_options = st.columns(2)
        
        with col_inputs:
            caracteristiques = st.text_area(
                "Caractéristiques du bien (notes brutes) :", 
                placeholder="Ex: T3 65m2, Lyon 3e, 2ch, salon lumineux, cuisine équipée, balcon 8m2, garage fermé, proche métro D, travaux récents"
            )
            prix = st.text_input("Prix du bien (Optionnel) :", placeholder="Ex: 295 000 €")
            
        with col_options:
            style_annonce = st.selectbox("Style de l'annonce", [
                "✨ Coup de cœur / Émotionnel (Idéal familles/particuliers)",
                "💼 Professionnel / Factuel (Idéal investisseurs)",
                "🏙️ Moderne / Storytelling (Idéal réseaux sociaux / Instagram)",
                "⚡ Court & Percutant (Idéal plateformes de type LeBonCoin)"
            ])
            
            langue = st.selectbox("Langue de l'annonce", ["Français", "Anglais", "Espagnol"])

        generer = st.button("🚀 Générer l'Annonce Parfaite", use_container_width=True)

    if generer:
        if not API_KEY:
            st.error("⚠️ Erreur : La clé GROQ_API_KEY est manquante dans les Secrets.")
        elif not caracteristiques:
            st.error("⚠️ Veuillez entrer au moins quelques détails sur le bien.")
        else:
            with st.spinner("L'IA de Groq rédige votre annonce immobilière..."):
                try:
                    client = Groq(api_key=API_KEY)
                    
                    prompt_systeme = f"""Tu es un agent immobilier d'élite et un copywriter professionnel. 
                    Ton but est de rédiger des annonces immobilières captivantes qui déclenchent des appels et des visites.
                    Utilise des émojis pertinents, structure l'annonce avec des titres clairs (L'avis de l'agence, Les points forts, La localisation).
                    Inclus le prix s'il est fourni. 
                    Rédige l'annonce directement en {langue}. Ne fais aucune introduction ni conclusion, commence directement par l'annonce."""

                    prompt_utilisateur = f"""
                    Notes brutes du bien : {caracteristiques}
                    Prix proposé : {prix}
                    Style demandé : {style_annonce}
                    """

                    reponse = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": prompt_systeme},
                            {"role": "user", "content": prompt_utilisateur}
                        ],
                        temperature=0.7
                    )
                    
                    annonce_genere = reponse.choices[0].message.content
                    st.success("✨ Votre annonce immobilière est prête !")
                    st.markdown(annonce_genere)
                    st.text_area("Copier le texte brut :", value=annonce_genere, height=300)

                except Exception as e:
                    st.error(f"Erreur technique Groq : {str(e)}")
