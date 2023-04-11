from dataclasses import dataclass

from app.clients.base_api import BaseApiClient
from app.dtos.thingspeak import ThingspeakResponse


@dataclass
class ThingspeakApiClient(BaseApiClient):
    def get_data(self, size: int = 10000) -> ThingspeakResponse:
        response = self.get(f"/channels/1293177/feeds.json?results={size}")
        if response.get("error"):
            raise response.get("error")

        return ThingspeakResponse.schema().loads(response.get("body"))
