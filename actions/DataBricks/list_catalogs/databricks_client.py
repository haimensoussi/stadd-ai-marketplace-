from databricks.sdk import WorkspaceClient


class DatabricksClient:

    def __init__(self, context):

        self.host = context.DATABRICKS_HOST
        self.token = context.DATABRICKS_TOKEN
        self.timeout = int(context.DATABRICKS_TIMEOUT or 120)
        self.proxy = context.DATABRICKS_PROXY

        self.client = WorkspaceClient(
            host=self.host,
            token=self.token
        )

    async def list_catalogs(self):

        catalogs = self.client.catalogs.list()

        results = []

        for catalog in catalogs:

            results.append({
                "name": catalog.name,
                "comment": catalog.comment,
                "owner": catalog.owner,
                "created_at": getattr(catalog, "created_at", None),
                "updated_at": getattr(catalog, "updated_at", None)
            })

        return results
