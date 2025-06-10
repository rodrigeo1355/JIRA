# Jira Connector

Este repositorio contiene un ejemplo simple de conector en Python para la API REST de Jira.

## Requisitos

- Python 3.8 o superior
- La librería `requests` (se puede instalar con `pip install requests`)

## Uso

Antes de ejecutar el script es necesario definir las siguientes variables de entorno:

- `JIRA_BASE_URL`: URL base de tu instancia de Jira (por ejemplo, `https://midominio.atlassian.net`)
- `JIRA_USERNAME`: tu nombre de usuario o correo de Atlassian
- `JIRA_API_TOKEN`: un token de API generado desde tu cuenta de Jira
- `JIRA_JQL` *(opcional)*: consulta JQL para filtrar las incidencias. Si no se define, se utilizará `project=TEST`.

Luego puedes ejecutar el conector con:

```bash
python jira_connector.py
```

El script imprimirá en pantalla las incidencias recuperadas según la JQL proporcionada.
