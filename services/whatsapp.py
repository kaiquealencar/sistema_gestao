import os
import requests
from apps.configuracoes.models import ConfiguracoesWhatsapp

def enviar_mensagem_whatsapp(numero_destino, mensagem):    

    dados = buscar_dados_api()    

    if not dados:
        return {"status": "erro", "detalhes": "Nenhuma configuração encontrada!"}

    headers = {
        "Content-Type": "application/json",
        "Client-Token": dados["client_token"]  
    }
    payload = {
        "phone": numero_destino,
        "message": mensagem
    }

    try:
        response = requests.post(dados["url"], json=payload, headers=headers, timeout=15)

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

    if not dados_api:
        return None

    return {
        "instance_id": dados_api.instancia_id, 
        "token": dados_api.token, 
        "client_token": dados_api.client_token,
        "url": dados_api.url_base}