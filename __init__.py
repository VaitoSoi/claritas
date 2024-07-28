try:
    from . import utils
except ImportError:
    import utils

# Missing data handler
utils.write_default()

try:
    # from .db import Problems, Submissions
    from . import judge
    from .judge import JudgeMode, JudgeResult, Limit, Language, Compiler, JudgeSession, Status, TestType
    from .utils import Indexable
except ImportError:
    # from db import Problems, Submissions
    import judge
    from judge import JudgeMode, JudgeResult, Limit, Language, Compiler, JudgeSession, Status, TestType
    from utils import Indexable

__all__ = [
    "utils",
    "judge",
    "Indexable",
    # "Problems",
    # "Submissions",
    "JudgeMode",
    "JudgeSession",
    "JudgeResult",
    "Limit",
    "TestType",
    "Language",
    "Compiler",
    "Status"
]
