# Provider Databricks HORIZON

## Présentation

Le **Provider Databricks HORIZON** expose les fonctionnalités de Databricks sous forme d'Actions réutilisables par la plateforme HORIZON.

Chaque Action représente une capacité métier et délègue toute la communication technique au **DatabricksClient**, qui utilise le SDK officiel Databricks.

Le Provider peut être utilisé par :

- Les Agents HORIZON
- Langflow
- n8n
- Les serveurs MCP
- Les API REST HORIZON

---

# Architecture

```
Agent

    │

    ▼

Action

    │

    ▼

DatabricksClient

    │

    ▼

SDK Databricks

    │

    ▼

Workspace Databricks
```

Les Actions ne communiquent jamais directement avec l'API Databricks.

Toute la logique technique est centralisée dans le **DatabricksClient**.

---

# Structure du projet

```
horizon-provider-databricks/

├── clients/
│   └── databricks_client.py
│
├── list_catalogs/
│
├── list_schemas/
│
├── list_tables/
│
├── execute_sql/
│
└── README.md
```

---

# Actions disponibles

| Action | Description |
|---------|-------------|
| List Catalogs | Retourne la liste des catalogues Unity Catalog |
| List Schemas | Retourne la liste des schémas d'un catalogue |
| List Tables | Retourne la liste des tables d'un schéma |
| Execute SQL | Exécute une requête SQL sur Databricks |

---

# Client SDK

Toutes les Actions utilisent le même client SDK :

```
DatabricksClient
```

Le client est responsable de :

- l'authentification ;
- la gestion de la connexion ;
- l'utilisation du SDK officiel Databricks ;
- la gestion des erreurs ;
- la transformation des résultats.

---

# Configuration

Le Provider nécessite les paramètres suivants :

| Paramètre | Description |
|-----------|-------------|
| DATABRICKS_HOST | URL du Workspace Databricks |
| DATABRICKS_TOKEN | Jeton d'accès personnel (PAT) |
| DATABRICKS_PROXY | Proxy HTTP/HTTPS (optionnel) |
| DATABRICKS_TIMEOUT | Temps d'attente des requêtes |

Ces paramètres sont automatiquement injectés par le Runtime HORIZON.

---

# Capacités du Provider

```
Catalogue

    ├── List Catalogs

Schéma

    ├── List Schemas

Table

    ├── List Tables

SQL

    ├── Execute SQL
```

---

# Flux d'exécution

```
Agent

↓

Action

↓

DatabricksClient

↓

SDK Databricks

↓

Workspace Databricks
```

---

# Dépendances

- Python 3.11
- SDK officiel Databricks (`databricks-sdk`)

---

# Bonnes pratiques

- Les Actions ne contiennent aucune logique technique.
- Toutes les communications avec Databricks passent par le `DatabricksClient`.
- Les paramètres de connexion sont fournis par le Runtime HORIZON.
- Les secrets (jetons, mots de passe) ne doivent jamais être codés en dur.

---

# Version

| Version | Description |
|----------|-------------|
| 1.0.0 | Première version du Provider Databricks |

---

# Licence

Ce Provider fait partie de la plateforme **HORIZON**.
