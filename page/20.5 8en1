import streamlit as st
import pandas as pd
import requests

# 🔒 Sécurité : synchronisé avec l'écran d'accueil global
if "est_abonne_global" not in st.session_state or not st.session_state.est_abonne_global:
    st.warning("🔒 Veuillez vous connecter sur la page d'accueil.")
    st.stop()

st.title("📦 Gestionnaire de Stock Intelligent (Version PRO)")
st.write("Gestion des inventaires et alertes de réapprovisionnement.")

# 🔑 Récupération sécurisée du Google Sheet
try:
    SHEET_URL = st.secrets["GOOGLE_SHEET_URL"]
except:
    st.error("❌ GOOGLE_SHEET_URL manquant dans les secrets Streamlit.")
    st.stop()

def charger_stock():
    try:
        # Transformation automatique de l'URL Google Sheets en lien d'export CSV direct
        csv_url = SHEET_URL.replace("/edit?usp=sharing", "/export?format=csv")
        csv_url = csv_url.split("/edit")[0] + "/export?format=csv" if "/edit" in csv_url else csv_url
        
        df = pd.read_csv(csv_url)
        return df
    except Exception as e:
        st.error(f"Erreur lors du chargement de la base de données Google Sheet : {e}")
        return pd.DataFrame(columns=["produit", "quantite", "seuil"])

def sauvegarder_stock(df):
    st.warning("⚠️ Sauvegarde manuelle requise : Copiez/collez ce format CSV dans votre tableur Google Sheet pour enregistrer de manière permanente.")
    st.code(df.to_csv(index=False), language="csv")

# Charge le stock une seule fois au début pour optimiser l'affichage
df_stock = charger_stock()

# --- Interface d'ajout ---
st.subheader("➕ Ajouter ou Mettre à jour un produit")
col_fields1, col_fields2 = st.columns(2)

with col_fields1:
    nom = st.text_input("Nom du produit", placeholder="Ex: T-Shirt Noir XL...")
with col_fields2:
    quantite = st.number_input("Quantité en stock", min_value=0, step=1, value=10)
    seuil = st.number_input("Seuil d’alerte (Rupture)", min_value=0, step=1, value=3)

if st.button("Ajouter ou Mettre à jour le stock", use_container_width=True):
    if not nom.strip():
        st.error("⚠️ Le nom du produit est obligatoire.")
    else:
        # Supprime l'ancien produit s'il existe déjà pour éviter les doublons
        df_stock = df_stock[df_stock["produit"].str.lower() != nom.strip().lower()]
        
        nouveau = pd.DataFrame([{
            "produit": nom.strip(),
            "quantite": int(quantite),
            "seuil": int(seuil)
        }])
        df_stock = pd.concat([df_stock, nouveau], ignore_index=True)
        st.success(f"✅ Le produit '{nom}' a été ajouté à votre base de simulation !")
        sauvegarder_stock(df_stock)

st.write("---")

# --- Affichage des inventaires ---
st.subheader("📋 État de l'inventaire actuel")

if df_stock.empty:
    st.info("Aucun produit enregistré dans votre inventaire Google Sheets.")
else:
    # Métriques globales rapides
    total_produits = len(df_stock)
    alertes = df_stock[df_stock["quantite"] <= df_stock["seuil"]]
    total_alertes = len(alertes)
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric(label="🛍️ Total Références", value=total_produits)
    with col_m2:
        st.metric(label="⚠️ Alertes Ruptures", value=total_alertes, delta=-total_alertes if total_alertes > 0 else 0, delta_color="inverse")

    st.write("")
    st.dataframe(df_stock, use_container_width=True)

    # --- Section Alertes Automatiques ---
    st.subheader("🚨 Système d'Alerte Automatique")

    if total_alertes > 0:
        st.error(f"⚠️ Attention ! Vous avez {total_alertes} produit(s) à réapprovisionner de toute urgence :")
        st.dataframe(alertes, use_container_width=True)
    else:
        st.success("✅ Excellente gestion ! Aucun produit n'est en dessous de son seuil d'alerte.")
