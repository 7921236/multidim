from sys import platform
from typing import Tuple
from collections import namedtuple


def resolve_stata(version: int = 17, stype: str = "se") -> Tuple[str]:
    """Resolve the STATA version and type

    Args:
        version (int, optional): _description_. Defaults to 17.
        stype (str, optional): _description_. Defaults to "se".

    Returns:
        Tuple[str]: _description_
    """
    assert stype in ["se", "be", "mp"], 'stype has to be one of "se", "be", "mp"'
    assert isinstance(version, int), "version has to be an integer"
    stata_path: str
    if platform == "linux" or platform == "linux2":
        stata_path = f"/usr/local/stata{version}"
    elif platform == "darwin":
        stata_path = "/Applications/Stata"
    elif platform == "win32":
        stata_path = f"C:\Program Files\Stata{version}"

    stata_setup = namedtuple("stata_setup", ["path", "type"])
    return stata_setup(stata_path, stype)
