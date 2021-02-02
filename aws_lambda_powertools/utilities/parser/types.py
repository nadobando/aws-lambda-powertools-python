"""Generics and other shared types used across parser"""
import sys
from typing import TypeVar

from pydantic import BaseModel

# Workaround for not importing typing_extensions on python ^3.8
if sys.version_info[0] > 3 or (sys.version_info[0] == 3 and sys.version_info[1] >= 8):
    from typing import Literal  # noqa: F401
else:
    try:
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        raise Exception("please install typing-extensions or upgrade to Python >= 3.8")

Model = TypeVar("Model", bound=BaseModel)
