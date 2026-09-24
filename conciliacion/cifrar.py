"""Cifra data.json -> data.enc.json (AES-256-GCM, clave PBKDF2-SHA256).
Uso: python cifrar.py data.json data.enc.json CONTRASEÑA
data.json NO se sube al repo: solo data.enc.json."""
import sys, json, os, base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
src, dst, pw = sys.argv[1], sys.argv[2], sys.argv[3]
ITER = 250000
salt, iv = os.urandom(16), os.urandom(12)
key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER).derive(pw.encode())
ct = AESGCM(key).encrypt(iv, open(src, 'rb').read(), None)
b = lambda x: base64.b64encode(x).decode()
json.dump({"v": 1, "iter": ITER, "salt": b(salt), "iv": b(iv), "ct": b(ct)}, open(dst, 'w'))
