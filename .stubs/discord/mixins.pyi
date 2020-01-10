from typing import Any

class EqualityComparable:
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class Hashable(EqualityComparable):
    def __hash__(self) -> int: ...