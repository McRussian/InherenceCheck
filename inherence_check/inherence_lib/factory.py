from typing import Dict, Any

from .sequency_parser import SequencyParser
from .sequency_comparator import PatternComparator


FactoryParser: Dict[str, Any] = {
    'sequency': SequencyParser(),
}


FactorComparator: Dict[str, Any] = {
    'sequency': PatternComparator(),
}
