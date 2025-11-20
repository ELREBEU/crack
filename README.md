# 🔐 Crack — Outil pédagogique d’analyse et compréhension des hash

Crack est un projet écrit en Python conçu **dans un cadre purement éducatif**.  
Il permet de comprendre :

- le fonctionnement des algorithmes de hachage
- comment les attaques basées sur dictionnaires parviennent à retrouver des mots de passe faibles
- pourquoi le salage, les itérations et les mots de passe robustes sont indispensables
- comment structurer un petit outil d'analyse dans un environnement de cybersécurité

> ⚠️ **Avertissement :**  
> Ce projet est **strictement éducatif**.  
> Ne l'utilisez jamais sur un système ou des données pour lesquelles vous n'avez pas une autorisation explicite.

---

## 🎯 Objectifs du projet

- Illustrer les limites des hash classiques (MD5, SHA-1, SHA-256…)
- Montrer comment fonctionne une attaque par dictionnaire dans un environnement contrôlé
- Sensibiliser aux bonnes pratiques de sécurité
- Servir de support pédagogique pour l’apprentissage de la cybersécurité

---

## 🧠 Fonctionnalités

- 🔍 **Identification naïve du type de hash**
- 📂 **Support des wordlists personnalisées**
- ⚙️ Architecture modulaire :
  - `identify_hash.py` → identification du hash
  - `crack.py` → logique de comparaison
  - `interface.py` → interactions utilisateur
  - `main.py` → lancement du programme
- 📊 **Affichage clair et pédagogique des résultats**
- 🧪 Permet d’expérimenter différents scénarios :
  - types de hash
  - wordlists variées
  - comparaison entre mots de passe faibles / forts

---

## 🗂️ Structure du projet

crack/
├── crack.py # Logique de l'attaque par dictionnaire
├── identify_hash.py # Détection du type de hash
├── interface.py # Interface CLI
├── main.py # Point d'entrée
└── wordlists/ # Dictionnaires (personnalisables)


---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ELREBEU/crack
cd crack
```
### 2. (Optionnel) Créer un environnement virtuel
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
### 3. Dépendances
Aucune dépendance externe :
tout est basé sur les modules natifs Python (hashlib, sys, os...).

## ⚠️ Avertissement légal

Ce projet ne doit être utilisé que dans un cadre éducatif.
Toute utilisation non autorisée sur des systèmes tiers est illégale.
Vous êtes entièrement responsable de votre propre usage.
