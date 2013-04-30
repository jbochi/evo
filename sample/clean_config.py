"""
Sample file to clean all server configs
"""

import sys
import os
from itertools import chain
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from evo import Evo

if __name__ == '__main__':
    server = Evo("127.0.0.1")
    configs = server.listConfig()
    for config_id in [c['configId'] for c in chain(*configs['data'].values())]:
        server.removeConfig(id=config_id)
    print server.listConfig()