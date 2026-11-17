import uuid

vault = {}

def tokenize(pan):
    token = str(uuid.uuid4())
    vault[token] = pan
    return token

def detokenize(token):
    return vault.get(token, "UNKNOWN_TOKEN")

pan = "4111-2222-3333-4444"
token = tokenize(pan)
print(f"Cleartext PAN (stays in secure vault only): {pan}")
print(f"Token sent to payment gateway: {token}")
print(f"Vault lookup during settlement: {detokenize(token)}")
