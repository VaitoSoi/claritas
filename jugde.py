import pydantic
import enum
import typing
import utils
import os

__all__ = [
    "Language",
    "Compiler",
    "TestType",
    "Status",
    "Limit",
    "JudgeMode",
    "JudgeResult",
]


class BaseCompiler(pydantic.BaseModel):
    language: typing.List[str]
    compile: str
    execute: str
    image: str
    version: typing.List[str]


class BaseFile(pydantic.BaseModel):
    file: str
    executable: str

    def model_post_init(self, *args):
        self.executable = (
            self.executable.format(ext=".exe" if os.name == "nt" else "")
            if self.executable.endswith("{ext}")
            else self.executable
        )


TestType = typing.Literal["file", "std"]
Language: typing.List[str] = utils.read_json("data/language.json")
Compiler = utils.read_json("data/compiler.json")
Compiler: typing.Dict[str, BaseCompiler] = {
    key: BaseCompiler(**value) for key, value in Compiler.items()
}
File = utils.read_json("data/file.json")
File: typing.Dict[str, BaseFile] = {
    key: BaseFile(**value) for key, value in File.items()
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


class Limit(pydantic.BaseModel):
    time: int
    memory: str


class JudgeMode(pydantic.BaseModel):
    mode: typing.Literal[0, 1]
    case: bool = pydantic.Field(default=None)
    trim_endl: bool = pydantic.Field(default=False)


class JudgeSession(pydantic.BaseModel):
    submission_id: str
    language: typing.Tuple[str, typing.Optional[int]]
    compiler: typing.Tuple[str, typing.Union[typing.Literal["latest"], int]]
    test_range: typing.Tuple[int, int]
    test_file: typing.Tuple[str, str]
    test_type: typing.Literal["file", "std"]
    judge_mode: JudgeMode
    limit: Limit


class JudgeResult(pydantic.BaseModel):
    id: int
    status: int
    time: typing.Optional[float] = pydantic.Field(default=None)
    warn: typing.Optional[str] = pydantic.Field(default=None)
    error: typing.Optional[str] = pydantic.Field(default=None)
