#/usr/bin/env python3
import sys
from urllib.parse import urlparse

domains = []
for line in sys.stdin.buffer:
    try:
        decoded_line = line.decode("utf-8")  # Próbáld UTF-8-ként dekódolni
    except UnicodeDecodeError:
        decoded_line = line.decode("latin-1", errors="replace")  
    
    
    parsed = urlparse(decoded_line.strip())
    if parsed.netloc not in domains:
        domains.append(parsed.netloc)
        print(parsed.netloc)
    