import json
import requests

from threading import Lock
from typing import Any, Dict, List, Optional

from logs.logs import logger
from aistudio.model.run.RunContext import RunContext


class ServiceNowMCPClient:

    def __init__(self, context: RunContext):

        self.base_url = context.SERVICENOW_MCP_URL
        self.api_token = context.SERVICENOW_MCP_API_TOKEN
        self.proxy = context.SERVICENOW_MCP_PROXY
        self.timeout = int(context.SERVICENOW_MCP_TIMEOUT) if context.SERVICENOW_MCP_TIMEOUT else 120

        self._context = context

        self._tools_cache: Optional[List[Dict]] = None

        self._cache_lock = Lock()

    def _send_request(
        self,
        route: str,
        method: str = "POST",
        data: Dict = None
    ) -> requests.Response:

        url = f"{self.base_url}/{route}"

        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

        proxies = {
            "http": self.proxy,
            "https": self.proxy
        } if self.proxy else None

        try:

            if method == "GET":

                response = requests.get(
                    url,
                    headers=headers,
                    proxies=proxies,
                    timeout=self.timeout,
                    verify=False
                )

            else:

                response = requests.post(
                    url,
                    headers=headers,
                    json=data,
                    proxies=proxies,
                    timeout=self.timeout,
                    verify=False
                )

            response.raise_for_status()

            return response

        except requests.exceptions.Timeout:

            logger.error(f"Timeout MCP : {url}")

            self._context.throw(
                http_code=504,
                app_code="SERVICENOW_MCP_TIMEOUT",
                message="Timeout lors de l'appel du serveur MCP."
            )

        except requests.exceptions.HTTPError as ex:

            logger.error(f"Erreur HTTP MCP : {ex}")

            self._context.throw(
                http_code=ex.response.status_code if ex.response else 500,
                app_code="SERVICENOW_MCP_HTTP_ERROR",
                message=str(ex)
            )

        except requests.exceptions.RequestException as ex:

            logger.error(f"Erreur MCP : {ex}")

            self._context.throw(
                http_code=500,
                app_code="SERVICENOW_MCP_REQUEST_ERROR",
                message=str(ex)
            )

    def health_check(self) -> Dict[str, Any]:

        response = self._send_request(
            route="health",
            method="GET"
        )

        return response.json()

    def list_tools(self) -> List[Dict]:

        with self._cache_lock:

            if self._tools_cache is not None:
                return self._tools_cache

            response = self._send_request(
                route="tools/list"
            )

            data = response.json()

            self._tools_cache = data.get("tools", [])

            logger.info(
                f"{len(self._tools_cache)} outils MCP chargés."
            )

            return self._tools_cache

    def get_tool(
        self,
        tool_name: str
    ) -> Dict[str, Any]:

        response = self._send_request(

            route="tools/get",

            data={
                "name": tool_name
            }

        )

        return response.json()

    def execute_tool(
        self,
        tool_name: str,
        arguments: Dict[str, Any]
    ) -> Dict[str, Any]:

        response = self._send_request(

            route="tools/call",

            data={
                "name": tool_name,
                "arguments": arguments
            }

        )

        return response.json()
