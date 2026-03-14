# This sample tests the detection of deprecated classes from the typing
# module.

from typing import (
    DefaultDict,
    Deque,
    Dict,
    FrozenSet,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    Union,
)


# These should be marked deprecated for Python >= 3.9
v1: List[int] = [1, 2, 3]
v2: Dict[int, str] = {}
v3: Set[int] = set()
v4: Tuple[int] = (3,)
v5: FrozenSet[int] = frozenset()
v6: Type[int] = int
v7 = Deque()
v8 = DefaultDict()

# These should be marked deprecated for Python >= 3.10
v20: Union[int, str]
v21: Optional[int]
