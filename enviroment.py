import os

# Get this file full path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# To initialize paths to directories
TEMP_DIR = os.path.join(ROOT_DIR, 'temp')
LOGS_DIR = os.path.join(ROOT_DIR, 'files', 'logs')

# The path to the dir with hashcat restore files
HASHCAT_RESTORES_DIR = os.path.join(ROOT_DIR, 'files', 'restores')

# The path to the dir with bruted hashes
HASHCAT_BRUTED_HASHES_DIR = os.path.join(ROOT_DIR, 'files', 'bruted_hashes')
