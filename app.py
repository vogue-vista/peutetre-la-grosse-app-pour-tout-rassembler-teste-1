import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Suite IA Entreprise PRO", page_icon="🚀", layout="wide")

# Gestion de la session de connexion
if "est_abonne_global" not in st.session_state:
    st.session_state.est_abonne_global = False

# Masquer la barre latérale si l'utilisateur n'est pas connecté
if not st.session_state.est_abonne_global:
    st.markdown("<style>[data-testid='stSidebar'] {display: none !important;}</style>", unsafe_allow_html=True)

# Design épuré en police Poppins
st.markdown("""
<style>
@import url('https://googleapis.com');
html, body, div, p, h1, h2, h3, h4, h5, h6, span, button { font-family: 'Poppins', sans-serif !important; }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# 🛠️ ZONE DE CONFIGURATION PAYPAL DEVELOPER (À CHANGER PLUS TARD)
# ------------------------------------------------------------------
# Remplace "sandbox" par ton vrai Client ID de production PayPal plus tard
PAYPAL_CLIENT_ID = "sandbox"  
# Remplace "P-XXXXXXXXXX" par l'ID exact de ton plan d'abonnement à 500$/mois créé sur PayPal
PAYPAL_PLAN_ID = "P-XXXXXXXXXX"  

# ------------------------------------------------------------------
# ÉCRAN DE VERROUILLAGE (L'UTILISATEUR N'A PAS PAYÉ)
# ------------------------------------------------------------------
if not st.session_state.est_abonne_global:
    st.title("🚀 Suite Entreprise IA — Plateforme Tout-en-Un")
    st.warning("🔒 L'accès à cet écosystème est réservé aux membres Premium.")
    
    col_offre, col_connexion = st.columns(2, gap="large")
    
    with col_offre:
        st.subheader("💎 Accès Illimité à vos 20 Applications pour 500 $/mois")
        st.write("Centralisez tous vos outils de croissance au même endroit.")
        st.write("Un seul abonnement unique. Paiement entièrement sécurisé par **PayPal**.")
        
        # Intégration du SDK intelligent PayPal officiel pour les abonnements
        paypal_button_html = f"""
        <div id="paypal-button-container-suite" style="max-width: 350px; margin-top: 20px;"></div>
        <script src="https://paypal.com{PAYPAL_CLIENT_ID}&vault=true&intent=subscription" data-sdk-integration-source="button-factory"></script>
        <script>
          paypal.Buttons({{
              style: {{
                  shape: 'rect',
                  color: 'gold',
                  layout: 'vertical',
                  label: 'subscribe'
              }},
              createSubscription: function(data, actions) {{
                return actions.subscription.create({{
                  'plan_id': '{PAYPAL_PLAN_ID}'
                }});
              }},
              onApprove: function(data, actions) {{
                // Cette alerte s'affiche dès que l'abonnement est validé avec succès
                alert('Félicitations ! Abonnement PayPal validé avec succès. ID de transaction : ' + data.subscriptionID);
              }}
          }}).render('#paypal-button-container-suite');
        </script>
        """
        components.html(paypal_button_html, height=180, scrolling=False)
        
    with col_connexion:
        st.subheader("🔑 Connexion Client Entreprise")
        st.write("Entrez vos identifiants pour débloquer votre accès à vie.")
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
# ÉCRAN DE BIENVENUE (L'UTILISATEUR EST CONNECTÉ)
# ------------------------------------------------------------------
else:
    st.title("⚡ Bienvenue dans votre Espace Centralisé")
    st.success("🔓 Vos accès globaux sont actifs. Utilisez la barre latérale qui vient d'apparaître à gauche pour basculer d'une application à une autre !")
    
    st.write("---")
    if st.button("🚪 Se déconnecter de la plateforme", use_container_width=True):
        st.session_state.est_abonne_global = False
        st.rerun()





