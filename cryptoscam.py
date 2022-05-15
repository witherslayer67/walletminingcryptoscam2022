import secrets, time
for i in range(200):
    print(secrets.token_hex(nbytes=32), ' - 0 btc')
    time.sleep(0.05)
print(secrets.token_hex(nbytes=32), ' - 0.1 btc')
input('press any button to continue') 