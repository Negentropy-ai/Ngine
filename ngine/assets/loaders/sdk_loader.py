"""External SDK loader - optional backend for users with SDK access."""

from typing import Optional, Any
from .base import AssetLoaderBase

class SDKAssetLoader(AssetLoaderBase):
    """Wrapper around external SDK for users with valid access."""

    def __init__(self):
        try:
            from lightwheel_sdk.loader import floorplan_loader, object_loader, ENDPOINT
            self._floorplan_loader = floorplan_loader
            self._object_loader = object_loader
            # ENDPOINT can be either a string URL or an object with host property
            if isinstance(ENDPOINT, str):
                self._endpoint = ENDPOINT
            else:
                self._endpoint = ENDPOINT
            self._available = True
        except ImportError:
            self._available = False
            raise ImportError(
                "External SDK not installed. This is an optional dependency."
            )

    def acquire_usd(
        self,
        backend: str,
        scene: str,
        layout_id: Optional[int] = None,
        style_id: Optional[int] = None,
        version: Optional[str] = None,
        **kwargs
    ) -> Any:
        """Acquire USD file via external SDK."""
        if not self._available:
            raise RuntimeError("External SDK not available")

        return self._floorplan_loader.acquire_usd(
            backend=backend,
            scene=scene,
            layout_id=layout_id,
            style_id=style_id,
            version=version,
            **kwargs
        )

    def acquire_by_registry(
        self,
        asset_type: str,
        source: str = None,
        file_name: str = None,
        registry_name: list = None,
        eqs: dict = None,
        projects: list = None,
        contains: dict = None,
        exclude_registry_name: list = None,
        **kwargs
    ) -> tuple:
        """Acquire asset via external SDK."""
        if not self._available:
            raise RuntimeError("External SDK not available")

        # Map parameters to SDK signature
        return self._object_loader.acquire_by_registry(
            registry_type=asset_type,
            registry_name=registry_name or [],
            exclude_registry_name=exclude_registry_name or [],
            eqs=eqs,
            contains=contains,
            file_type='USD',
            file_name=file_name or '',
            source=source or [],
            projects=projects or [],
            quality_levels=[]
        )

    def acquire_by_file_version(self, version: str) -> tuple:
        """Acquire asset by file version via external SDK."""
        if not self._available:
            raise RuntimeError("External SDK not available")

        return self._object_loader.acquire_by_file_version(version)

    @property
    def host(self) -> str:
        """API endpoint from external SDK."""
        if isinstance(self._endpoint, str):
            return self._endpoint
        else:
            return getattr(self._endpoint, 'host', '')

    @host.setter
    def host(self, value: str):
        """Set API endpoint."""
        if isinstance(self._endpoint, str):
            # Can't set host on string, store it separately
            self._endpoint = value
        else:
            self._endpoint.host = value

    def list_registry(self):
        """List available registry entries."""
        try:
            return self._object_loader.list_registry()
        except:
            return []
