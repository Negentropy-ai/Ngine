"""Base asset loader interface."""

from abc import ABC, abstractmethod
from typing import Optional, Any

class AssetLoaderBase(ABC):
    """Base interface for asset loaders - enables multiple backends."""

    @abstractmethod
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
        pass

    @abstractmethod
    def acquire_by_registry(
        self,
        asset_type: str,
        source: str,
        **kwargs
    ) -> tuple:
        """Acquire asset by registry lookup."""
        pass

    @property
    @abstractmethod
    def host(self) -> str:
        """API endpoint."""
        pass

    @host.setter
    @abstractmethod
    def host(self, value: str):
        """Set API endpoint."""
        pass
