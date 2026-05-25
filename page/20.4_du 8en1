import streamlit as st
import json
from groq import Groq

# 🔒 Sécurité : synchronisé avec l'écran d'accueil global
if "est_abonne_global" not in st.session_state or not st.session_state.est_abonne_global:
    st.warning("🔒 Veuillez vous connecter sur la page d'accueil.")
    st.stop()

st.title("📈 Analyseur de Produits e‑Commerce (IA PRO)")
st.write("Analyse intelligente basée sur l’IA : demande, concurrence, potentiel, viralité et recommandation.")

# 🔑 Clé IA sécurisée
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except:
    st.error("❌ Clé GROQ_API_KEY manquante dans les secrets Streamlit.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

# --- Interface ---
mot_cle = st.text_input("Nom du produit à analyser :", placeholder="Ex: Mini projecteur 4K, Tapis de yoga écologique...")

if st.button("Analyser avec IA", use_container_width=True):
    if mot_cle.strip() == "":
        st.error("⚠️ Veuillez entrer un mot-clé.")
    else:
        with st.spinner("⏳ Notre IA analyse le marché, la concurrence et la viralité..."):

            prompt = f"""
            Analyse ce produit pour un e-commerce : {mot_cle}

            Donne-moi une analyse complète en format JSON strict UNIQUEMENT. Ne rajoute aucun texte avant ou après.
            Les valeurs numériques de la demande, de la concurrence et de la viralité doivent être des nombres entiers entre 0 et 100 (pas de texte ou de symbole % à l'intérieur).

            Format JSON :
            {{
                "demande": 80,
                "concurrence": 40,
                "prix_moyen": "29.99 $",
                "viralite": 75,
                "risques": "Description des risques",
                "recommandation": "Lancer / Tester / Éviter",
                "resume": "Résumé en 3 lignes"
            }}
            """

            try:
                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": "Tu es un expert en analyse e-commerce. Tu réponds UNIQUEMENT sous forme de code JSON valide."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.2,
                    max_tokens=600
                )

                # Utilisation sécurisée du format choices avec index [0]
                reponse = completion.choices[0].message.content

                st.subheader("📊 Tableau de Bord du Produit")
                
                try:
                    # Tentative de conversion du JSON pour l'afficher proprement
                    data = json.loads(reponse)
                    
                    # Section Métriques Visuelles
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric(label="💰 Prix Moyen du Marché", value=data.get("prix_moyen", "N/A"))
                    with col2:
                        rec = data.get("recommandation", "N/A")
                        if "Lancer" in rec or "lancer" in rec:
                            st.success(f"🚀 Recommandation : {rec.upper()}")
                        elif "Tester" in rec or "tester" in rec:
                            st.warning(f"⚡ Recommandation : {rec.upper()}")
                        else:
                            st.error(f"❌ Recommandation : {rec.upper()}")
                    
                    st.write("---")
                    
                    # Section Barres de Score
                    st.write(f"📈 **Demande estimée :** {data.get('demande')}/100")
                    st.progress(int(data.get('demande', 0)) / 100)
                    
                    st.write(f"⚔️ **Niveau de concurrence :** {data.get('concurrence')}/100")
                    st.progress(int(data.get('concurrence', 0)) / 100)
                    
                    st.write(f"🎵 **Potentiel de viralité (TikTok/Trends) :** {data.get('viralite')}/100")
                    st.progress(int(data.get('viralite', 0)) / 100)
                    
                    st.write("---")
                    
                    # Section Textes
                    st.markdown(f"🔍 **Analyse des risques :** {data.get('risques')}")
                    st.info(f"📝 **Résumé stratégique :**\n{data.get('resume')}")
                    
                except Exception as json_err:
                    # Si le JSON de l'IA a un problème, on affiche quand même le texte brut
                    st.warning("⚠️ Impossible de générer les graphiques. Voici l'analyse brute :")
                    st.write(reponse)

            except Exception as e:
                st.error(f"Erreur IA : {e}")
