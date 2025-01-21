import hashlib


user_hash_dict = {}

#Import Wordlist
with open('10-million-password-list-top-1000000.txt', 'r') as f:
    common_passwords = f.read().splitlines()
#Opens Hash.txt
with open('username_hashes.txt', 'r') as f:
    text = f.read().splitlines()
    for user_hash in text:
        username = user_hash.split(":")[0]
        hash = user_hash.split(":")[1]
        user_hash_dict[username] = hash

for user, hash in user_hash_dict.items():
    print(user,hash)

    for password in common_passwords:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        for username, hash in user_hash_dict.items():
            if hashed_password == hash:
                print(f'HASH FOUND\n{username}:{password}')