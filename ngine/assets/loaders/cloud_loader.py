"""Cloud asset loader - optional backend for remote assets."""

from typing import Optional, Any
import requests
from .base import AssetLoaderBase

class CloudAssetLoader(AssetLoaderBase):
    """Loads assets from cloud storage."""

    def __init__(self, base_url: Optional[str] = None):
        self.base_url = base_url or "https://assets.ngine.io"
        self._session = requests.Session()

    def acquire_usd(
        self,
        backend: str,
        scene: str,
        layout_id: Optional[int] = None,
        style_id: Optional[int] = None,
        version: Optional[str] = None,
        **kwargs
    ) -> Any:
        """Acquire USD file from cloud."""
        if layout_id and style_id:
            url = f"{self.base_url}/scenes/{backend}/{layout_id}_{style_id}.usd"
        elif layout_id:
            url = f"{self.base_url}/scenes/{backend}/layout_{layout_id}.usd"
        else:
            url = f"{self.base_url}/scenes/{backend}/default.usd"

        response = self._session.get(url)
        if response.status_code != 200:
            raise FileNotFoundError(f"Asset not found: {url}")

        class Result:
            def result(self):
                return (url, {
                    "scene": backend,
                    "layout_id": layout_id,
                    "style_id": style_id,
                    "version_id": version
                })

        return Result()

    def acquire_by_registry(
        self,
        asset_type: str,
        source: str,
        **kwargs
    ) -> tuple:
        """Acquire asset from cloud."""
        url = f"{self.base_url}/{asset_type}/{source}"
        response = self._session.get(url)
        if response.status_code != 200:
            raise FileNotFoundError(f"Asset not found: {url}")
        return (url, source, None)

    @property
    def host(self) -> str:
        """API endpoint."""
        return self.base_url

    @host.setter
    def host(self, value: str):
        """Set API endpoint."""
        self.base_url = value
