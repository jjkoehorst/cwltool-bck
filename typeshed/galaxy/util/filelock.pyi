# Stubs for galaxy.util.filelock (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class FileLockException(Exception): ...

class FileLock:
    is_locked = ...  # type: bool
    lockfile = ...  # type: Any
    file_name = ...  # type: Any
    timeout = ...  # type: Any
    delay = ...  # type: Any
    def __init__(self, file_name, timeout: int = ..., delay: float = ...) -> None: ...
    fd = ...  # type: Any
    def acquire(self): ...
    def release(self): ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback): ...
    def __del__(self): ...
