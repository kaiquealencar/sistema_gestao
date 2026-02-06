import os
import requests
from apps.configuracoes.models import ConfiguracoesWhatsapp

def enviar_mensagem_whatsapp(numero_destino, mensagem):    


    zapi_instance_id = os.getenv("ZAPI_INSTANCE_ID")
    zapi_token = os.getenv("ZAPI_TOKEN")
    zapi_client_token = os.getenv("ZAPI_CLIENT_TOKEN")
    zapi_url = f"https://api.z-api.io/instances/{zapi_instance_id}/token/{zapi_token}/send-text"

    headers = {
        "Content-Type": "application/json",
        "Client-Token": zapi_client_token  
    }
    payload = {
        "phone": numero_destino,
        "message": mensagem
    }

    try:
        response = requests.post(zapi_url, json=payload, headers=headers, timeout=15)

        if response.status_code != 200:
            print(f"❌ Erro Z-API ({response.status_code}): {response.text}")

        response.raise_for_status()
        return response.json()    
    except requests.exceptions.HTTPError as e:
        return {"status": "erro", "detalhes": f"HTTPError: {str(e)}"}
    except requests.exceptions.RequestException as e:
        return {"status": "erro", "detalhes": f"RequestException: {str(e)}"}


def buscar_dados_api():
    dados_api = ConfiguracoesWhatsapp.objects.first()

    return {"instance_id": dados_api.token}