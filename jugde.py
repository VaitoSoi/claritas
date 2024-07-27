import enum
import os
import typing

import pydantic

try:
    from . import utils
except ImportError:
    import utils

__all__ = [
    "Language",
    "Compiler",
    "TestType",
    "Status",
    "Limit",
    "JudgeMode",
    "JudgeResult",
]


class BaseCompiler(utils.Indexable):
    name: str
    language: typing.List[str]
    compile: str
    execute: str
    image: str
    version: typing.List[str]


class BaseLanguage(utils.Indexable):
    name: str
    file: str
    executable: str
    version: typing.Optional[typing.List[str]]

    def model_post_init(self, *args):
        self.executable = (
            self.executable.format(ext=".exe" if os.name == "nt" else "")
            if self.executable.endswith("{ext}")
            else self.executable
        )


language_json = os.path.join(utils.data, "language.json")
compiler_json = os.path.join(utils.data, "compiler.json")

Language: typing.Union[
    typing.Dict[str, BaseLanguage],
    typing.Dict[typing.Literal["all"], typing.List[str]]
] = pydantic.create_model(
    "Language", **{
        key:
            (BaseLanguage, BaseLanguage(**val))
            if isinstance(val, dict) else
            (type(val), val)
        for key, val in
        utils.read_json(language_json).items()
    })
Compiler: typing.Union[
    typing.Dict[str, BaseCompiler],
    typing.Dict[typing.Literal["all"], typing.List[str]]
] = pydantic.create_model(
    "Compiler", **{
        key:
            (BaseCompiler, BaseCompiler(**val))
            if isinstance(val, dict) else
            (type(val), val)
        for key, val in
        utils.read_json(compiler_json).items()
    })


class TestType(str, enum.Enum):
    FILE = 'file'
    STD = 'std'


class Status(enum.Enum):
    ABORTED = -1
    ACCEPTED = 0
    WRONG_ANSWER = 1
    TIME_LIMIT_EXCEEDED = 2
    MEMORY_LIMIT_EXCEEDED = 3
    COMPILE_WARN = 4
    RUNTIME_ERROR = 5
    COMPILE_ERROR = 6
    SYSTEM_ERROR = 7


class Limit(utils.Indexable):
    time: int
    memory: str


class JudgeMode(utils.Indexable):
    mode: typing.Literal[0, 1]
    case: bool = pydantic.Field(default=None)
    trim_endl: bool = pydantic.Field(default=False)


class JudgeSession(utils.Indexable):
    submission_id: str
    language: typing.Tuple[str, typing.Optional[int]]
    compiler: typing.Tuple[str, typing.Union[typing.Literal["latest"], str]]
    test_range: typing.Tuple[int, int]
    test_file: typing.Tuple[str, str]
    test_type: typing.Literal["file", "std"]
    judge_mode: JudgeMode
    limit: Limit


class JudgeResult(utils.Indexable):
    id: int
    status: int
    time: typing.Optional[float] = pydantic.Field(default=None)
    warn: typing.Optional[str] = pydantic.Field(default=None)
    error: typing.Optional[str] = pydantic.Field(default=None)
