from horizon.runtime.context import RunContext
from horizon.providers.databricks.clients.databricks_client import DatabricksClient
from horizon.runtime.logger import logger
from horizon.runtime.exceptions import AppException


async def action(context: RunContext):

    logger.info("Databricks - List Catalogs")

    try:

        client = DatabricksClient(context)

        catalogs = await client.list_catalogs()

        context.addValue("catalogs", catalogs)

        return context

    except Exception as ex:

        logger.exception(ex)

        raise AppException(
            "DATABRICKS_LIST_CATALOGS_ERROR",
            str(ex)
        )
