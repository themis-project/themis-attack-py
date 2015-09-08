import sys
import os
from . import Carrier


def run():
    host = os.getenv('THEMIS_HOST')
    port = int(os.getenv('THEMIS_PORT', '80'))
    url = os.getenv('THEMIS_URL', 'api/submit')

    carrier = Carrier(host, port, url)
    flags = sys.argv[1:]
    try:
        results = carrier.attack(*flags)
        carrier.logger.info(results)
    except Exception:
        sys.exit(1)
