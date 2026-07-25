# stadd-ai-marketplace-
# SNCF--STADD AI Marketplace

## Présentation

SNCF--STADD AI Marketplace est une plateforme dédiée au développement, au partage et à la réutilisation de composants d'Intelligence Artificielle.

L'objectif est d'accélérer la création de solutions IA en s'appuyant sur des briques réutilisables plutôt que de redévelopper chaque projet depuis zéro.

La plateforme repose sur une architecture modulaire où chaque fonctionnalité est encapsulée sous forme d'**Action**, pouvant être assemblée pour construire des workflows et des agents intelligents.

---

# Vision

Notre ambition est de proposer un véritable Marketplace d'IA permettant aux équipes de :

- Découvrir des composants IA prêts à l'emploi
- Réutiliser des Actions existantes
- Construire rapidement de nouveaux agents
- Standardiser les développements IA
- Partager les meilleures pratiques entre équipes

---

# Les concepts de la plateforme

## Action

Une Action est la plus petite unité exécutable de la plateforme.

Une Action réalise une tâche précise.

Exemples :

- Ask Genie
- SQL Query
- RAG Query
- Green AI Metrics
- Run Databricks Job

Toutes les Actions utilisent le même modèle d'exécution basé sur un **RunContext**.

---

## Workflow

Un Workflow est un enchaînement d'Actions permettant d'automatiser un processus métier.

Exemple :

```
Question utilisateur
        │
        ▼
Recherche documentaire
        │
        ▼
Ask Genie
        │
        ▼
Génération de la réponse
```

---

## Agent

Un Agent est une solution métier construite à partir d'un ou plusieurs Workflows et Actions.

Exemples :

- Business Analyst
- Knowledge Assistant
- AI Monitoring
- Green AI Assistant

---

## Marketplace

Le Marketplace permet de :

- Découvrir les Actions disponibles
- Consulter leur documentation
- Installer les composants (installation manuelle dans la première version)
- Tester les Actions
- Réutiliser les composants dans d'autres projets

---

# Architecture du projet

```
stadd-ai-marketplace/

├── actions/
├── marketplace/
├── runtime/
├── ui/
└── docs/
```

---

# Première version (V1)

Cette première version a pour objectif de mettre en place les fondations de la plateforme.

Fonctionnalités prévues :

- Interface Marketplace
- Modèle standard d'Action
- Exécution d'Actions
- Installation manuelle
- Première Action : Ask Genie

---

# Feuille de route

## Version 1

- Marketplace
- Ask Genie
- SQL Query
- RAG Query

## Version 2

- Workflows
- Designer de Workflows

## Version 3

- Agents IA
- Marketplace d'Agents

## Version 4

- Installation automatique
- Gestion des versions
- Publication de composants

---

# Objectif

Construire une plateforme permettant de développer des solutions IA de manière rapide, standardisée et réutilisable, en s'appuyant sur une bibliothèque d'Actions et de composants partageables.
