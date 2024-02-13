import os, sys

try:
    import requests
except ImportError as e:
    print('\n [\x1b[1;91m!\x1b[0m]  {str(e).title()}')
    os.system('pip install requests')
try:
    import rich
except ImportError as e:
    print('\n [\x1b[1;91m!\x1b[0m]  {str(e).title()}')
    os.system('pip install rich')
try:
    import bs4
except ImportError as e:
    print('\n [\x1b[1;91m!\x1b[0m]  {str(e).title()}')
    os.system('pip install bs4')
try:
    import Cryptodome
except ImportError as e:
    print('\n [\x1b[1;91m!\x1b[0m]  {str(e).title()}')
    os.system('pip install pycryptodomex')
try:
    import nacl
except ImportError as e:
    print('\n [\x1b[1;91m!\x1b[0m]  {str(e).title()}')
    os.system('pkg install clang python libffi openssl libsodium && SODIUM_INSTALL=system pip install pynacl')
  
from asset.instagram import Instagram as Zora_ID
   
if __name__=='__main__':
    try: os.system("git pull")
    except: pass
    try: Zora_ID().menuinsta()
    except Exception as e: exit(str(e).title())
