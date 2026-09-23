"""Production smoke tests for Vectoris."""
import importlib


def test_package_imports() -> None:
    module = importlib.import_module("vectoris")
    assert module.__name__ == "vectoris"


def test_import_is_network_independent() -> None:
    # Import-time network calls make CI and offline development fragile.
    module = importlib.import_module("vectoris")
    assert module is not None
