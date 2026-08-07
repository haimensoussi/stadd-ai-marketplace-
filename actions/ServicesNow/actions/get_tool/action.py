from logs.logs import logger

from aistudio.model.run.RunContext import RunContext

from utils.inputs import get_input_value
from utils.exceptions import AppException

from clients.ServiceNowMCPClient import ServiceNowMCPClient


async def action(context: RunContext):

    logger.info("ServiceNow MCP - Get Tool")

    try:

        tool_name = get_input_value(context, "tool_name")

        context.trace(f"Recherche de l'outil MCP : {tool_name}")

        client = ServiceNowMCPClient(context)

        tool = await client.get_tool(tool_name)

        context.addValue(
            "tool",
            tool,
            type="object"
        )

        context.bot = f"Outil '{tool_name}' récupéré avec succès."

        context.trace("Tool récupéré")

        return context

    except AppException:
        raise

    except Exception as ex:

        logger.exception(ex)

        context.traceError(str(ex))

        raise AppException(
            status_code=500,
            app_code="SERVICENOW_MCP_GET_TOOL_ERROR",
            message=str(ex)
        )
