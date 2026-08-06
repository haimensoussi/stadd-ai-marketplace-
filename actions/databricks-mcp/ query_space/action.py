"""
HORIZON

Databricks MCP Provider

Action : Query Space
"""

from horizon.runtime.context import RunContext
from horizon.runtime.exceptions import AppException
from horizon.runtime.logger import logger

from ..clients.databricks_mcp_client import DatabricksMCPClient


async def action(context: RunContext):

    logger.info("Databricks MCP - Query Space")

    try:

        query = context.get_input_value("query")

        conversation_id = context.get_input_value("conversation_id")

        client = DatabricksMCPClient(context)

        response = await client.query_space(

            query=query,

            conversation_id=conversation_id

        )

        context.addValue("conversation_id", response["conversation_id"])

        context.addValue("message_id", response["message_id"])

        context.addValue("status", response["status"])

        return context

    except Exception as ex:

        logger.exception(ex)

        raise AppException(

            "DATABRICKS_MCP_QUERY_ERROR",

            str(ex)

        )
