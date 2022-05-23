from typing import Dict, Any

from inherence_check.parser import SequencyParser, PatternComparator


FactoryParser: Dict[str, Any] = {
    'sequency': SequencyParser(),
}


FactorComparator: Dict[str, Any] = {
    'sequency': PatternComparator(),
}
