try:
    from .utils import write_default
except ImportError:
    from utils import write_default

# Missing data handler
write_default()

try:
    # from .db import Problems, Submissions
    from .jugde import JudgeMode, JudgeResult, Limit, Language, Compiler, File, JudgeSession, Status, TestType
    from .utils import Indexable
except ImportError:
    # from db import Problems, Submissions
    from jugde import JudgeMode, JudgeResult, Limit, Language, Compiler, File, JudgeSession, Status, TestType
    from utils import Indexable

__all__ = [
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
    "File",
    "Status"
]
