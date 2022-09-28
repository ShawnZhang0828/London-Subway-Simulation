import sys
sys.path.append(sys.path[0] + '\\subway\\structures')

from dataclasses import dataclass, field
from station import Station 


@dataclass(order=True)
class PrioritizedItem:
    '''
        PrioritiedItem class define a dataclass to compare edges
    '''
    priority: int
    item: Station=field(compare=False)