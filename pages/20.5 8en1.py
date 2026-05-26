import streamlit as st
import pandas as pd
import json
import os

# 🔒 Sécurité globale ajustée à votre panneau principal à 500$/mo
if "est_abonne_global" not in st.session_state or not st.session_state.est_abonne_global:
    st.error("⛔ Accès refusé. Veuillez activer votre licence sur la page d'accueil.")
    st.stop()

st.title("📦 Gestionnaire de Stock Intelligent (Version PRO)")
st.write("✨ **Mode SaaS Connecté** — Sauvegarde automatique instantanée.")

# Fichier local qui va servir de base de données automatique
FICHIER_STOCK = "stock_entreprise.json"

# Fonctions magiques pour charger et sauvegarder automatiquement
def charger_stock():
    if not os.path.exists(FICHIER_STOCK):
        # Si le fichier n'existe pas encore, on crée un stock de démonstration
        donnees_demo = [
            {"produit": "Ordinateur Portable Pro", "quantite": 15, "seuil": 5},
            {"produit": "Souris Sans Fil VIP", "quantite": 3, "seuil": 10}
        ]
        with open(FICHIER_STOCK, "w", encoding="utf-8") as f:
            json.dump(donnees_demo, f, indent=4)
        return pd.DataFrame(donnees_demo)
    
    try:
        with open(FICHIER_STOCK, "r", encoding="utf-8") as f:
            donnees = json.load(f)
        return pd.DataFrame(donnees)
    except Exception as e:
        return pd.DataFrame(columns=["produit", "quantite", "seuil"])

def sauvegarder_stock(df):
    try:
        # Convertit le tableau en dictionnaire et l'enregistre tout seul en tâche de fond !
        donnees = df.to_dict(orient="records")
        with open(FICHIER_STOCK, "w", encoding="utf-8") as f:
            json.dump(donnees, f, indent=4)
        st.success("💾 Base de données synchronisée automatiquement !")
    except Exception as e:
        st.error(f"Erreur de sauvegarde automatique : {e}")

# --- Chargement initial des données ---
if "donnees_inventaire" not in st.session_state:
    st.session_state.donnees_inventaire = charger_stock()

# --- Interface d'Ajout ---
with st.expander("➕ Ajouter un nouveau produit au catalogue", expanded=False):
    nom = st.text_input("Nom du produit")
    col_qte, col_seuil = st.columns(2)
    with col_qte:
        quantite = st.number_input("Quantité initiale", min_value=0, step=1, value=10)
    with col_seuil:
        seuil = st.number_input("Seuil d’alerte critique", min_value=0, step=1, value=5)

    if st.button("Enregistrer le produit", use_container_width=True):
        if not nom:
            st.error("⚠️ Le nom du produit est obligatoire.")
        else:
            nouveau = pd.DataFrame([{
                "produit": nom,
                "quantite": int(quantite),
                "seuil": int(seuil)
            }])
            st.session_state.donnees_inventaire = pd.concat([st.session_state.donnees_inventaire, nouveau], ignore_index=True)
            sauvegarder_stock(st.session_state.donnees_inventaire)
            st.rerun()

# --- Affichage et Modification ---
st.subheader("📋 État du Stock en Temps Réel")

if st.session_state.donnees_inventaire.empty:
    st.info("Aucun produit en stock actuellement.")
else:
    # 🌟 LE TRUC INCROYABLE : st.data_editor permet au client de modifier les quantités 
    # en double-cliquant directement dans le tableau, comme sur Excel !
    stock_edite = st.data_editor(
        st.session_state.donnees_inventaire,
        use_container_width=True,
        num_rows="dynamic", # Permet au client de supprimer des lignes s'il veut
        key="editeur_stock"
    )
    
    # Si le client a modifié une case du tableau, on sauvegarde les changements d'un coup
    if not stock_edite.equals(st.session_state.donnees_inventaire):
        st.session_state.donnees_inventaire = stock_edite
        sauvegarder_stock(stock_edite)
        st.rerun()

    # --- Alertes de réapprovisionnement ---
    st.subheader("⚠️ Alertes de Rupture")
    # Forcer la conversion numérique pour éviter les bugs de comparaison
    df_verif = st.session_state.donnees_inventaire.copy()
    df_verif["quantite"] = pd.to_numeric(df_verif["quantite"])
    df_verif["seuil"] = pd.to_numeric(df_verif["seuil"])
    
    alertes = df_verif[df_verif["quantite"] <= df_verif["seuil"]]

    if not alertes.empty:
        st.error(f"🚨 Attention : {len(alertes)} produit(s) ont atteint le seuil critique !")
        st.dataframe(alertes, use_container_width=True)
    else:
        st.success("✅ Tout est sous contrôle. Aucun produit en rupture de stock.")
