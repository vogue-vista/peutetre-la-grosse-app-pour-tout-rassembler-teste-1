import streamlit as st
from bs4 import BeautifulSoup
from groq import Groq

# 🔒 Sécurité : synchronisé avec l'écran d'accueil global
if "est_abonne_global" not in st.session_state or not st.session_state.est_abonne_global:
    st.warning("🔒 Veuillez vous connecter sur la page d'accueil.")
    st.stop()

st.title("🧪 Analyse HTML IA (Version PRO)")
st.write("Colle du HTML et laisse l'IA analyser automatiquement le contenu.")

# 🔑 Clé IA sécurisée
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_API_KEY)
except:
    st.error("❌ Clé GROQ_API_KEY manquante dans les secrets Streamlit.")
    st.stop()

html_input = st.text_area("Colle ton HTML ici :", height=300, placeholder="<html><body><h1>Mon Produit</h1><p>Description...</p></body></html>")

def extract_basic_info(html):
    soup = BeautifulSoup(html, "html.parser")

    # Titre
    titre = soup.find(["h1", "h2", "h3"])
    titre = titre.text.strip() if titre else "Non trouvé"

    # Prix
    prix = soup.find(string=lambda x: "$" in x if x else False)
    prix = prix.strip() if prix else "Non trouvé"

    # Vendeur
    vendeur = soup.find(string=lambda x: any(v in x for v in ["Walmart", "Amazon", "Best Buy", "Etsy"]) if x else False)
    vendeur = vendeur.strip() if vendeur else "Non trouvé"

    # Paragraphes
    paragraphs = [p.text.strip() for p in soup.find_all("p") if p.text.strip()][:5]

    # Images
    images = [img.get("src") for img in soup.find_all("img") if img.get("src")][:5]

    return titre, prix, vendeur, paragraphs, images

def analyse_ia(titre, prix, vendeur, paragraphs):
    texte = "\n".join(paragraphs)

    prompt = f"""
    Analyse ce code HTML et génère une analyse complète.

    Données extraites :
    - Titre : {titre}
    - Prix : {prix}
    - Vendeur : {vendeur}
    - Contenu : {texte}

    Donne :
    1. Un résumé clair du produit ou de la page
    2. Une analyse e-commerce (prix, crédibilité, vendeur)
    3. Une analyse SEO rapide
    4. Une recommandation pour améliorer la page
    5. Une estimation du type de page (fiche produit, article, blog, etc.)
    """

    chat = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Tu es un expert en analyse web, SEO et e-commerce."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=600
    )

    # CORRIGÉ : Ajout du pour éviter le crash technique
    return chat.choices[0].message.content

if st.button("Lancer l'Analyse HTML Pro", use_container_width=True):
    if not html_input.strip():
        st.error("❌ Veuillez coller du code HTML avant de lancer l'analyse.")
    else:
        with st.spinner("⏳ Extraction des balises et analyse stratégique par l'IA..."):
            titre, prix, vendeur, paragraphs, images = extract_basic_info(html_input)

            st.success("✅ Code HTML analysé avec succès !")
            
            # Système d'onglets pour un rendu haut de gamme
            tab1, tab2 = st.tabs(["🧠 Analyse Stratégique IA", "📌 Données Extraites"])
            
            with tab1:
                st.subheader("🧠 Rapport d'Analyse IA")
                try:
                    analyse = analyse_ia(titre, prix, vendeur, paragraphs)
                    st.info(analyse)
                except Exception as e:
                    st.error(f"Erreur IA : {e}")
            
            with tab2:
                st.subheader("📌 Métadonnées et Contenu détectés")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric(label="Titre principal", value=titre)
                with col2:
                    st.metric(label="Prix détecté", value=prix)
                with col3:
                    st.metric(label="Vendeur identifié", value=vendeur)
                
                st.write("---")
                st.write("**Paragraphes analysés :**")
                for p in paragraphs:
                    st.markdown(f"- {p}")

                if images:
                    st.write("---")
                    st.write("**Sources des images détectées :**")
                    for img in images:
                        st.caption(img)
