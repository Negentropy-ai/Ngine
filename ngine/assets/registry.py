"""Central asset registry with pluggable backends."""

from typing import Optional
import os

_loaders = {
    "local": None,
    "cloud": None,
    "sdk": None
}
_current_backend = None

def get_loader(backend: Optional[str] = None):
    """Get asset loader for specified backend."""
    global _loaders, _current_backend

    backend = backend or os.environ.get(
        "NGINE_ASSET_BACKEND",
        "local"  # Default to local for decoupling
    )

    if backend not in _loaders:
        raise ValueError(f"Unknown backend: {backend}. Available: {list(_loaders.keys())}")

    if _loaders[backend] is None:
        if backend == "local":
            from ngine.assets.loaders.local_loader import LocalAssetLoader
            _loaders[backend] = LocalAssetLoader()
        elif backend == "cloud":
            from ngine.assets.loaders.cloud_loader import CloudAssetLoader
            _loaders[backend] = CloudAssetLoader()
        elif backend == "sdk":
            from ngine.assets.loaders.sdk_loader import SDKAssetLoader
            _loaders[backend] = SDKAssetLoader()

    _current_backend = backend
    return _loaders[backend]

def get_current_loader():
    """Get currently active loader."""
    if _current_backend is None:
        return get_loader()
    return _loaders[_current_backend]

# Convenience functions for backward compatibility
def get_local_loader():
    """Get local loader (for compatibility)."""
    return get_loader("local")

def get_cloud_loader():
    """Get cloud loader (for compatibility)."""
    return get_loader("cloud")

def get_sdk_loader():
    """Get SDK loader (for compatibility)."""
    return get_loader("sdk")
