import os, sys

try:
    import requests
except ImportError:
    os.system('pip install requests')
try:
    import rich
except ImportError:
    os.system('pip install rich')
try:
    import bs4
except ImportError:
    os.system('pip install bs4')
try:
    import Cryptodome
except ImportError:
    os.system('pip install pycryptodomex')
try:
    import nacl
except ImportError:
    os.system('pkg install clang python libffi openssl libsodium && SODIUM_INSTALL=system pip install pynacl')
  
from facebook import Facebook as Zora_ID
   
if __name__=='__main__':
    try: os.system("git pull"); Zora_ID().menuinsta()
    except Exception as e: exit(str(e).title())
