# HORIZON - Provider Databricks MCP

## Présentation

Le **Provider Databricks MCP** permet à la plateforme **HORIZON** d'interagir avec les serveurs **Model Context Protocol (MCP)** exposés par Databricks.

Ce provider encapsule les capacités d'un **Databricks Genie Space** sous forme d'Actions HORIZON afin qu'elles puissent être utilisées par :

- Les Agents HORIZON
- Langflow
- n8n
- Les API REST
- Les futurs Agents MCP

Le provider ne communique jamais directement avec les services Databricks depuis les Actions.

Toute la communication est centralisée dans le **DatabricksMCPClient**.

---

# Architecture

```
                 Agent HORIZON

                        │

                        ▼

                Action HORIZON

                        │

                        ▼

            DatabricksMCPClient

                        │

                        ▼

           Databricks MCP Server

                        │

                        ▼

                Databricks Genie
```

---

# Structure du projet

```
horizon-provider-databricks-mcp/

│
├── README.md
├── provider.yaml
├── requirements.txt
├── pyproject.toml
│
├── clients/
│   ├── __init__.py
│   └── databricks_mcp_client.py
│
├── actions/
│
│   ├── query_space/
│   │   ├── action.py
│   │   ├── manifest.yaml
│   │   ├── input.yaml
│   │   ├── output.yaml
│   │   ├── README.md
│   │   └── examples/
│   │       ├── request.json
│   │       └── response.json
│   │
│   ├── poll_response/
│   │   ├── action.py
│   │   ├── manifest.yaml
│   │   ├── input.yaml
│   │   ├── output.yaml
│   │   ├── README.md
│   │   └── examples/
│   │       ├── request.json
│   │       └── response.json
│   │
│   ├── list_tools/
│   │   ├── action.py
│   │   ├── manifest.yaml
│   │   ├── input.yaml
│   │   ├── output.yaml
│   │   └── README.md
│   │
│   └── call_tool/
│       ├── action.py
│       ├── manifest.yaml
│       ├── input.yaml
│       ├── output.yaml
│       └── README.md
│
├── tests/
│
└── docs/
```

---

# Composants

## DatabricksMCPClient

Le **DatabricksMCPClient** est responsable de :

- l'authentification ;
- la connexion au serveur MCP ;
- l'exécution des requêtes JSON-RPC ;
- la découverte des Tools ;
- l'appel des Tools ;
- la gestion des erreurs ;
- la gestion des proxys.

Toutes les Actions utilisent ce client.

---

# Actions disponibles

## Query Space

Interroge un **Databricks Genie Space** en langage naturel.

Entrées

- query
- conversation_id (optionnel)

Sorties

- conversation_id
- message_id
- status

---

## Poll Response

Interroge le serveur MCP afin de récupérer la réponse d'une requête asynchrone.

Entrées

- conversation_id
- message_id

Sorties

- response

---

## List Tools

Retourne la liste des Tools disponibles sur le serveur MCP.

Entrées

Aucune.

Sorties

- tools

---

## Call Tool

Permet d'appeler dynamiquement n'importe quel Tool MCP.

Entrées

- tool_name
- arguments

Sorties

- result

---

# Paramètres de configuration

Le Provider utilise les paramètres HORIZON suivants.

| Paramètre | Description |
|-----------|-------------|
| DATABRICKS_MCP_ENDPOINT | URL du serveur MCP Databricks |
| DATABRICKS_TOKEN | Token Databricks |
| DATABRICKS_PROXY | Proxy HTTP/HTTPS |
| DATABRICKS_TIMEOUT | Timeout des requêtes |

Ces paramètres sont injectés automatiquement par le Runtime HORIZON.

---

# Flux d'exécution

```
RunContext

↓

Action

↓

DatabricksMCPClient

↓

JSON-RPC

↓

Databricks MCP

↓

Genie Space
```

---

# Bonnes pratiques

Les Actions :

- ne contiennent aucune logique réseau ;
- ne réalisent aucun appel HTTP ;
- ne manipulent jamais les tokens ;
- délèguent toutes les opérations au DatabricksMCPClient.

Le DatabricksMCPClient :

- gère l'authentification ;
- exécute les appels JSON-RPC ;
- transforme les réponses ;
- gère les erreurs.

---

# Dépendances

- Python 3.11
- requests
- Databricks MCP Server

---

# Cas d'utilisation

Le Provider permet notamment de :

- interroger un Genie Space
- analyser des données en langage naturel
- automatiser des analyses métier
- intégrer Databricks Genie dans un Agent HORIZON
- utiliser Databricks Genie depuis Langflow
- utiliser Databricks Genie depuis n8n

---

# Évolution du Provider

Les prochaines Actions pourront inclure :

- Get Space
- Get Message
- Create Message
- Start Conversation
- Execute Attachment Query
- Download Query Result

sans modifier le DatabricksMCPClient.

---

# Philosophie HORIZON

Chaque Provider HORIZON respecte la même architecture.

```
Agent

↓

Action

↓

Client SDK

↓

Provider Externe
```

Le Provider Databricks MCP applique exactement cette règle.

Les Actions représentent les capacités métier.

Le DatabricksMCPClient représente la couche technique.

---

# Version

Version actuelle

```
1.0.0
```

---

# Licence

Projet HORIZON

Provider officiel Databricks MCP.
