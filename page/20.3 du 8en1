import streamlit as st
from groq import Groq

# 🔒 Sécurité : synchronisé avec l'écran d'accueil global
if "est_abonne_global" not in st.session_state or not st.session_state.est_abonne_global:
    st.warning("🔒 Veuillez vous connecter sur la page d'accueil.")
    st.stop()

st.title("📊 Calculateur de Marge & Profits (Version PRO)")
st.write("Calculez automatiquement votre marge, votre profit, votre ROI et obtenez une analyse IA.")

# 🔑 Clé IA sécurisée
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_API_KEY)
except:
    client = None  # L’IA sera désactivée si la clé n’est pas trouvée

# --- Interface ---
prix_vente = st.number_input("Prix de vente ($)", min_value=0.0, step=0.01)
prix_achat = st.number_input("Prix d'achat ($)", min_value=0.0, step=0.01)
frais_plateforme = st.number_input("Frais plateforme (%)", min_value=0.0, max_value=100.0, value=10.0, step=0.5)
frais_pub = st.number_input("Coût pub par vente ($)", min_value=0.0, step=0.01)

if st.button("Calculer", use_container_width=True):
    if prix_vente == 0 or prix_achat == 0:
        st.error("⚠️ Le prix de vente et le prix d'achat doivent être supérieurs à 0.")
    else:
        # --- Calculs ---
        frais_plateforme_val = prix_vente * (frais_plateforme / 100)
        profit = prix_vente - prix_achat - frais_plateforme_val - frais_pub
        marge = (profit / prix_vente) * 100 if prix_vente > 0 else 0
        marge_brute = ((prix_vente - prix_achat) / prix_vente) * 100 if prix_vente > 0 else 0
        roi = (profit / (prix_achat + frais_pub)) * 100 if (prix_achat + frais_pub) > 0 else 0
        break_even = prix_achat + frais_plateforme_val + frais_pub

        # --- Affichage des résultats ---
        st.subheader("📈 Résultats détaillés")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Profit par vente", value=f"{profit:.2f} $")
            st.metric(label="Point mort (break-even)", value=f"{break_even:.2f} $")
        with col2:
            st.metric(label="Marge nette", value=f"{marge:.2f} %")
        with col3:
            st.metric(label="Marge brute", value=f"{marge_brute:.2f} %")
            st.metric(label="ROI", value=f"{roi:.2f} %")

        if profit > 0:
            st.success("✅ Produit rentable")
        else:
            st.error("❌ Produit non rentable")

        st.markdown("---")

        # --- Analyse IA ---
        if client:
            st.subheader("🧠 Analyse IA du produit")
            with st.spinner("L'IA analyse vos marges..."):

                prompt = f"""
                Analyse ce produit en termes de rentabilité.

                Données :
                - Prix de vente : {prix_vente} $
                - Prix d'achat : {prix_achat} $
                - Frais plateforme : {frais_plateforme} %
                - Coût pub : {frais_pub} $
                - Profit : {profit:.2f} $
                - Marge nette : {marge:.2f} %
                - Marge brute : {marge_brute:.2f} %
                - ROI : {roi:.2f} %
                - Break-even : {break_even:.2f} $

                Donne de manière courte et directe :
                1. Une analyse rapide de la rentabilité
                2. Un conseil pour améliorer la marge
                3. Un prix de vente recommandé si nécessaire
                """

                try:
                    chat = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[
                            {"role": "system", "content": "Tu es un expert en pricing e-commerce."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.4,
                        max_tokens=500
                    )

                    # Utilisation du format choices corrigé
                    st.info(chat.choices[0].message.content)

                except Exception as e:
                    st.error(f"Erreur IA : {e}")
        else:
            st.info("L'analyse IA est désactivée (clé GROQ_API_KEY manquante).")
