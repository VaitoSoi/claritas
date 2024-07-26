import pydantic
import enum
import typing
import os

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
    language: typing.List[str]
    compile: str
    execute: str
    image: str
    version: typing.List[str]


class BaseFile(utils.Indexable):
    file: str
    executable: str

    def model_post_init(self, *args):
        self.executable = (
            self.executable.format(ext=".exe" if os.name == "nt" else "")
            if self.executable.endswith("{ext}")
            else self.executable
        )


language_json = os.path.join(utils.data, "language.json")
compiler_json = os.path.join(utils.data, "compiler.json")
file_json = os.path.join(utils.data, "file.json")

TestType = typing.Literal["file", "std"]
Language: typing.List[str] = utils.read_json(language_json)
Compiler: typing.Dict[str, BaseCompiler] = {
    key: BaseCompiler(**value) for key, value in utils.read_json(compiler_json).items()
}
File: typing.Dict[str, BaseFile] = {
    key: BaseFile(**value) for key, value in utils.read_json(file_json).items()
}


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
