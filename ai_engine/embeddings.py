import requests
import os

def embed_text(text: str) -> list[float]:
    account_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
    token = os.environ.get("CLOUDFLARE_API_TOKEN")
    
    response = requests.post(
        f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/baai/bge-base-en-v1.5",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": text}
    )
    return response.json()["result"]["data"][0]