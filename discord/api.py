from typing import Dict, Union

import requests

from . import headers


class DiscordSettingsAPI:
    """API Wrapper using a JWT and the default endpoint."""

    ENDPOINT = 'https://discord.com/api/v9/users/@me/settings'

    def __init__(self, auth_token: str):
        self.get_headers = headers.GetRequestMethodHeaders(JWT).headers
        self.patch_headers = headers.PatchRequestMethodHeaders(JWT).headers

    def get(self) -> Dict[str, Union[str, None]]:
        """Perform a GET request."""
        request = requests.get(self.ENDPOINT, headers=self.get_headers)
        return json.loads(request.text)

    def patch(self, data: Dict[str, Union[str, None]]):
        """Perform a PATCH request."""
        requests.patch(self.ENDPOINT, headers=self.patch_headers, json=data)
