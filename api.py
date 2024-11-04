from dataclasses import dataclass
from typing import Optional
import requests
import base64

@dataclass
class Helix:
    company: Optional[str] = 'MXDR'
    client_id: Optional[str] = 'None'
    client_secret: Optional[str] = 'None'
    scope: Optional[str] = 'None'

    def helix_f(self):
        return {'message':f'{self.client_id} dentro de fireeye'}, 200
    
    def helix_t(self):
        endpoint_token = 'https://auth.trellix.com/auth/realms/IAM/protocol/openid-connect/token'
        
        base64_client_cred = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()
        
        headers = {
        'Authorization': f'Basic {base64_client_cred}',
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
        'scope': self.scope,
        'grant_type': 'client_credentials'
        }

        try:
            # Envio da requisição POST
            response = requests.post(url=endpoint_token, headers=headers, data=data)
            
            # Verifica se a requisição foi bem-sucedida
            response.raise_for_status()  # Levanta um erro para códigos de status não 200
            
            return response.json()['access_token']  # Retorna o JSON da resposta

        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP: {http_err}')
        except requests.exceptions.RequestException as req_err:
            print(f'Erro na requisição: {req_err}')
        except Exception as e:
            print(f'Erro inesperado: {e}')
    
        