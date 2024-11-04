import os
from api import Helix
from dotenv import load_dotenv

load_dotenv()



company = Helix(
    'mxdr',
    os.getenv('client_id'),
    os.getenv('client_secret'),
    os.getenv('scope'))

print(company.helix_t())

# print(os.getenv('api_key_trellix'))