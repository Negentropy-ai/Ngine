"""Local asset loader - filesystem-based backend."""

from pathlib import Path
from typing import Optional, Any
import os
from .base import AssetLoaderBase

class LocalAssetLoader(AssetLoaderBase):
    """Loads assets from local filesystem."""

    def __init__(self, base_path: Optional[str] = None):
        self.base_path = Path(base_path or os.environ.get("NGINE_ASSET_PATH", "./assets"))
        self._cache = {}

    def acquire_usd(
        self,
        backend: str,
        scene: str,
        layout_id: Optional[int] = None,
        style_id: Optional[int] = None,
        version: Optional[str] = None,
        **kwargs
    ) -> Any:
        """Acquire USD file for floorplan/scene."""
        if layout_id and style_id:
            usd_path = self.base_path / f"scenes/{backend}/{layout_id}_{style_id}.usd"
        elif layout_id:
            usd_path = self.base_path / f"scenes/{backend}/layout_{layout_id}.usd"
        else:
            usd_path = self.base_path / f"scenes/{backend}/default.usd"

        if not usd_path.exists():
            raise FileNotFoundError(f"Asset not found: {usd_path}")

        class Result:
            def result(self):
                return (usd_path, {
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
        """Acquire asset by registry lookup."""
        asset_path = self.base_path / asset_type / source
        if not asset_path.exists():
            raise FileNotFoundError(f"Asset not found: {asset_path}")
        return (str(asset_path), source, None)

    @property
    def host(self) -> str:
        """API endpoint placeholder."""
        return os.environ.get("NGINE_API_ENDPOINT", "http://localhost:8080")

    @host.setter
    def host(self, value: str):
        """Set API endpoint."""
        os.environ["NGINE_API_ENDPOINT"] = value

    def list_registry(self):
        """List available registry entries."""
        # Return empty list for local loader - registry is file-based
        return []
