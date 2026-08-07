from logs.logs import logger

from aistudio.model.run.RunContext import RunContext

from utils.inputs import get_input_value
from utils.exceptions import AppException

from clients.ServiceNowMCPClient import ServiceNowMCPClient


async def action(context: RunContext):

    logger.info("Exécution de l'action ServiceNow MCP - List Tools")

    try:

        context.trace("Initialisation du client ServiceNow MCP")

        client = ServiceNowMCPClient(context)

        tools = await client.list_tools()

        context.addValue(
            "tools",
            tools,
            type="object"
        )

        context.addValue(
            "count",
            len(tools),
            type="int"
        )

        context.bot = f"{len(tools)} outil(s) MCP ServiceNow disponible(s)."

        context.trace("Liste des outils récupérée avec succès")

        return context

    except AppException:
        raise

    except Exception as e:

        logger.exception(e)

        context.traceError(str(e))

        raise AppException(
            status_code=500,
            app_code="SERVICENOW_MCP_LIST_TOOLS_ERROR",
            message=f"Erreur lors de la récupération des outils MCP ServiceNow : {str(e)}"
        )
