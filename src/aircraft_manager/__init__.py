import toml
import pathlib


__all__ = ["get_version"]


def get_version():
    pyproject_path = pathlib.Path(__file__).parent.parent.parent / "pyproject.toml"
    return toml.load(pyproject_path)["project"]["version"]
