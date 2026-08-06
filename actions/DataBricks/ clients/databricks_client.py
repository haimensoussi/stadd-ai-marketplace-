"""
HORIZON Databricks Provider

SDK Client
"""

from databricks.sdk import WorkspaceClient


class DatabricksClient:

    def __init__(self, context):

        self.context = context

        self.host = context.DATABRICKS_HOST
        self.token = context.DATABRICKS_TOKEN
        self.timeout = int(getattr(context, "DATABRICKS_TIMEOUT", 120))
        self.proxy = getattr(context, "DATABRICKS_PROXY", None)

        self.client = WorkspaceClient(
            host=self.host,
            token=self.token
        )

    ####################################################################
    # Catalogs
    ####################################################################

    async def list_catalogs(self):

        result = []

        for catalog in self.client.catalogs.list():

            result.append({
                "name": catalog.name,
                "comment": catalog.comment,
                "owner": catalog.owner,
                "created_at": getattr(catalog, "created_at", None),
                "updated_at": getattr(catalog, "updated_at", None)
            })

        return result

    ####################################################################
    # Schemas
    ####################################################################

    async def list_schemas(self, catalog_name):

        result = []

        for schema in self.client.schemas.list(
            catalog_name=catalog_name
        ):

            result.append({
                "catalog_name": schema.catalog_name,
                "name": schema.name,
                "comment": schema.comment,
                "owner": schema.owner
            })

        return result

    ####################################################################
    # Tables
    ####################################################################

    async def list_tables(self, catalog_name, schema_name):

        result = []

        for table in self.client.tables.list(
            catalog_name=catalog_name,
            schema_name=schema_name
        ):

            result.append({
                "catalog_name": table.catalog_name,
                "schema_name": table.schema_name,
                "name": table.name,
                "table_type": table.table_type,
                "owner": table.owner
            })

        return result

    ####################################################################
    # SQL
    ####################################################################

    async def execute_sql(
        self,
        warehouse_id,
        statement
    ):

        return self.client.statement_execution.execute_statement(
            warehouse_id=warehouse_id,
            statement=statement
        )
