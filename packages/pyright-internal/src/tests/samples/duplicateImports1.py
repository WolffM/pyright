# This sample tests the duplicate import detection.

import sys

# This should generate an error because Any is duplicated
from typing import Dict, Any

# This should generate an error because sys is duplicated


a: Dict[Any, Any]
b = sys.api_version
