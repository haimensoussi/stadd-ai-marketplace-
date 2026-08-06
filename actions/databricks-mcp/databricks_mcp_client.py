"""
HORIZON

Databricks MCP Client
"""

import uuid
import requests


class DatabricksMCPClient:

    def __init__(self, context):

        self.endpoint = context.DATABRICKS_MCP_ENDPOINT
        self.token = context.DATABRICKS_TOKEN
        self.timeout = int(context.DATABRICKS_TIMEOUT or 120)
        self.proxy = context.DATABRICKS_PROXY

    ####################################################################
    # Headers
    ####################################################################

    def _headers(self):

        return {

            "Authorization": f"Bearer {self.token}",

            "Accept": "application/json, text/event-stream",

            "Content-Type": "application/json"

        }

    ####################################################################
    # Proxy
    ####################################################################

    def _proxies(self):

        if not self.proxy:

            return None

        return {

            "http": self.proxy,

            "https": self.proxy

        }

    ####################################################################
    # Generic JSON RPC
    ####################################################################

    async def _execute(

        self,

        method,

        params

    ):

        payload = {

            "jsonrpc": "2.0",

            "id": str(uuid.uuid4()),

            "method": method,

            "params": params

        }

        response = requests.post(

            self.endpoint,

            headers=self._headers(),

            json=payload,

            proxies=self._proxies(),

            timeout=self.timeout

        )

        response.raise_for_status()

        result = response.json()

        if "error" in result:

            raise Exception(result["error"])

        return result["result"]

    ####################################################################
    # List Tools
    ####################################################################

    async def list_tools(self):

        return await self._execute(

            "tools/list",

            {}

        )

    ####################################################################
    # Call Tool
    ####################################################################

    async def call_tool(

        self,

        tool_name,

        arguments

    ):

        return await self._execute(

            "tools/call",

            {

                "name": tool_name,

                "arguments": arguments

            }

        )

    ####################################################################
    # Query Space
    ####################################################################

    async def query_space(

        self,

        tool_name,

        query,

        conversation_id=None

    ):

        arguments = {

            "query": query

        }

        if conversation_id:

            arguments["conversation_id"] = conversation_id

        return await self.call_tool(

            tool_name,

            arguments

        )

    ####################################################################
    # Poll Response
    ####################################################################

    async def poll_response(

        self,

        tool_name,

        conversation_id,

        message_id

    ):

        return await self.call_tool(

            tool_name,

            {

                "conversation_id": conversation_id,

                "message_id": message_id

            }

        )
