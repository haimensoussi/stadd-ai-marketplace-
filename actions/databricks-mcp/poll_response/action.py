"""
HORIZON

Databricks MCP Provider

Action : Poll Response
"""

from horizon.runtime.context import RunContext
from horizon.runtime.exceptions import AppException
from horizon.runtime.logger import logger

from ..clients.databricks_mcp_client import DatabricksMCPClient


async def action(context: RunContext):

    logger.info("Databricks MCP - Poll Response")

    try:

        conversation_id = context.get_input_value("conversation_id")

        message_id = context.get_input_value("message_id")

        client = DatabricksMCPClient(context)

        response = await client.poll_response(

            conversation_id=conversation_id,

            message_id=message_id

        )

        context.addValue("response", response)

        return context

    except Exception as ex:

        logger.exception(ex)

        raise AppException(

            "DATABRICKS_MCP_POLL_RESPONSE_ERROR",

            str(ex)

        )
