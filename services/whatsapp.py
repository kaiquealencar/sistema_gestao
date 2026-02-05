import os
from twilio.rest import Client

def enviar_whatsapp_mensagem(numero_destino, mensagem):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    whatsapp_from = os.getenv("TWILIO_WHATSAPP_NUMBER")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=mensagem,
        from_=whatsapp_from,
        to= f'whatsapp:{numero_destino}'
    )

    print(f"--- TENTANDO ENVIAR WHATSAPP ---")
    print(f"DE: {whatsapp_from}")
    print(f"PARA: whatsapp:{numero_destino}")
    
    try:
        message = client.messages.create(
            body=mensagem,
            from_=whatsapp_from,
            to=f'whatsapp:{numero_destino}'
        )
        print(f"SUCESSO NA TWILIO! SID: {message.sid}")
        return message.sid
    except Exception as e:
        print(f"ERRO FATAL NA TWILIO: {e}")
        raise e # Repassa o erro para a View capturar

    return message.sid