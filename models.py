import typing

import pydantic
import sqlmodel
import platform
import psutil


class Indexable(sqlmodel.SQLModel):
    """
    sqlmodel.SQLModel but allows for indexing like a dictionary :D
    """

    def __getitem__(self, item):
        return getattr(self, item)


class PydanticIndexable(pydantic.BaseModel):
    """
    pydantic.BaseModel but allows for indexing like a dictionary :D
    """

    def __getitem__(self, item):
        return getattr(self, item)


class SystemMemory(PydanticIndexable):
    total: int = pydantic.Field(default_factory=lambda: psutil.virtual_memory().total)
    available: int = pydantic.Field(default_factory=lambda: psutil.virtual_memory().available)
    percent: float = pydantic.Field(default_factory=lambda: psutil.virtual_memory().percent)
    used: int = pydantic.Field(default_factory=lambda: psutil.virtual_memory().used)
    free: int = pydantic.Field(default_factory=lambda: psutil.virtual_memory().free)


class SystemCPU(PydanticIndexable):
    count: int = pydantic.Field(default_factory=lambda: psutil.cpu_count())
    percent: float = pydantic.Field(default_factory=lambda: psutil.cpu_percent())
    times: dict = pydantic.Field(default_factory=lambda: psutil.cpu_times()._asdict())


class SystemInformation(PydanticIndexable):
    name: str = pydantic.Field(default_factory=lambda: f"{platform.system()} {platform.release()}")
    python: str = pydantic.Field(default_factory=lambda: platform.python_version())
    memory: SystemMemory = pydantic.Field(default_factory=lambda: SystemMemory())
    cpu: SystemCPU = pydantic.Field(default_factory=lambda: SystemCPU())


class Status(PydanticIndexable):
    status: typing.Literal["idle", "busy"]
    progress: str = pydantic.Field(default=None)
    system: SystemInformation = pydantic.Field(default_factory=lambda: SystemInformation())
