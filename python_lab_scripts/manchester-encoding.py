import manchester_code
from manchester_code import encode, decode


#used to encode data already listed in bytes
manchester_code = encode([0b00001111, 0b01101001])
print(''.join(['{:08b}'.format(m) for m in manchester_code]))
# 01010101101010100110100110010110

#decode message and list in bytes
dmsg= decode([0b01010101, 0b10101010, 0b01101001, 0b10010110])
print(''.join(['{:08b}'.format(m) for m in dmsg]))


#used to take a user string message and encode and decode it
message= input("what is the message that is being encoded:")

msg =(message.encode(encoding = 'UTF-8'))
encoded = encode(msg)
print("The encoded message is:" , encoded)

decoded= decode(encoded)

print(decoded)

