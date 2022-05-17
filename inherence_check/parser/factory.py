from typing import Dict, Any

from inherence_check.parser.sequency_parser import SequencyParser


FactoryParser: Dict[str, Any] = {
    'sequency': SequencyParser(),
}
