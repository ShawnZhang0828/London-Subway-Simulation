from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    '''
        PrioritiedItem class define a dataclass to compare edges
    '''
    priority: int
    item: Any=field(compare=False)