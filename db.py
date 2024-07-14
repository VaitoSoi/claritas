from jugde import JugdeMode, JudgeResult, Limit
import pydantic
import uuid
import typing

class Problems(pydantic.BaseModel):
    id: str = pydantic.Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str = pydantic.Field(default="")
    accept_language: typing.List[str]
    test_name: typing.List[str]
    total_testcases: int
    test_type: typing.Literal["file", "std"]
    roles: typing.Optional[typing.List[str]] | str
    dir: str = pydantic.Field(default=None)
    limit: Limit
    mode: JugdeMode

class Submissions(pydantic.BaseModel):
    id: str = pydantic.Field(default_factory=lambda: str(uuid.uuid4()))
    problem: str
    lang: typing.Tuple[str, typing.Optional[int]]
    compiler: typing.Tuple[str, typing.Optional[int | str]]
    file_path: str = pydantic.Field(default=None)
    result: JudgeResult = pydantic.Field(default=None)
    code: str