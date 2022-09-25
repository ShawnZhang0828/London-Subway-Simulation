from dataclasses import dataclass, field
from subway.structures.station import Station 


@dataclass(order=True)
class PrioritizedItem:
    '''
        PrioritiedItem class define a dataclass to compare edges
    '''
    priority: int
    item: Station=field(compare=False)