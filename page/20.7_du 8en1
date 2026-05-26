import streamlit as st
import requests
from bs4 import BeautifulSoup
from groq import Groq

# 🔒 Sécurité : synchronisé avec l'écran d'accueil global
if "est_abonne_global" not in st.session_state or not st.session_state.est_abonne_global:
    st.warning("🔒 Veuillez vous connecter sur la page d'accueil.")
    st.stop()

st.title("🔍 Scraper Web PRO (Scrape.do + IA)")
st.write("Scrape n'importe quelle page web et laisse l'IA analyser automatiquement le contenu.")

# 🔑 Clés API sécurisées
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    SCRAPEDO_API_KEY = st.secrets["SCRAPEDO_API_KEY"]
except:
    st.error("❌ Clés API manquantes dans les secrets Streamlit (GROQ_API_KEY, SCRAPEDO_API_KEY).")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

# --- Interface ---
url = st.text_input("URL de la page web à scraper :", placeholder="https://example.com...")

def scrape_url(url):
    """Scrape via Scrape.do"""
    try:
        r = requests.get(
            "https://api.scrape.do",
            params={"token": SCRAPEDO_API_KEY, "url": url},
            timeout=30
        )
        return r.text
    except Exception as e:
        st.error(f"Erreur Scrape.do : {e}")
        return ""

def extract_info(html):
    """Extraction automatique du contenu"""
    soup = BeautifulSoup(html, "html.parser")

    titre = soup.title.text.strip() if soup.title else "Aucun titre trouvé"
    paragraphs = [p.text.strip() for p in soup.find_all("p") if p.text.strip()]
    images = [img.get("src") for img in soup.find_all("img") if img.get("src")]

    return titre, paragraphs[:5], images[:5]

def analyse_ia(titre, paragraphs):
    """Analyse IA via Groq"""
    texte = "\n".join(paragraphs)

    prompt = f"""
    Analyse cette page web et résume-la en français.

    Titre : {titre}

    Contenu :
    {texte}

    Donne :
    1. Un résumé clair et professionnel
    2. Les points importants à retenir
    3. Le type de page (blog, fiche produit, article, etc.)
    4. Une recommandation SEO stratégique (mots-clés, structure)
    """

    chat = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Tu es un expert en analyse web et SEO."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=600
    )

    # CORRIGÉ : Ajout du [0] pour éviter le crash technique
    return chat.choices[0].message.content

# --- Action ---
if st.button("Lancer le Scraping & l'Analyse IA", use_container_width=True):
    if not url.strip():
        st.error("⚠️ Veuillez entrer une URL valide.")
    else:
        with st.spinner("⏳ Récupération du site web et analyse par l'IA..."):
            html = scrape_url(url)

            if html:
                titre, paragraphs, images = extract_info(html)

                st.success("✅ Extraction réussie !")
                
                # Onglets pour trier les informations proprement
                tab1, tab2, tab3 = st.tabs(["🧠 Analyse IA", "📝 Contenu Extrait", "💻 Code Source Brut"])
                
                with tab1:
                    st.subheader("🧠 Analyse Stratégique IA & SEO")
                    try:
                        analyse = analyse_ia(titre, paragraphs)
                        st.info(analyse)
                    except Exception as e:
                        st.error(f"Erreur IA : {e}")
                
                with tab2:
                    st.subheader("📝 Données Textuelles")
                    st.write(f"**Titre de la page :** {titre}")
                    st.write("**Extraits textuels (Paragraphes) :**")
                    for p in paragraphs:
                        st.markdown(f"- {p}")
                    
                    if images:
                        st.write("---")
                        st.subheader("🖼️ Liens d'images détectés")
                        for img in images:
                            st.caption(img)

                with tab3:
                    st.subheader("💻 Code HTML Brut (5000 premiers caractères)")
                    st.code(html[:5000], language="html")
