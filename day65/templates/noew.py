a=['Jpgtmu', 'XKYZ', 'lxgskcuxq']
def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
for i in a :
    print(encode(i))