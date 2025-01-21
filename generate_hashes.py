import hashlib

#Eingabe um sha256 hash zu erstellen
Input = ("x")
hash = hashlib.sha256(Input.encode('utf-8'))
print(hash.hexdigest())

