from scapy.all import *
from base64 import b32decode
from math import ceil
from Crypto.Cipher import AES

def b32decode_nopad(b32str):
    pad_length = ceil(len(b32str) / 8) * 8 - len(b32str)
    return b32decode(b32str + "=" * pad_length)

def decrypt_aes_cbc_no_padding(key, iv, ciphertext):
    # Convert key and IV from hexadecimal to bytes
    key = bytes.fromhex(key)
    iv = bytes.fromhex(iv)
    
    ciphertext = b32decode_nopad(ciphertext)
    # Create AES cipher object with CBC mode and no-padding
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the ciphertext
    plaintext = cipher.decrypt(ciphertext)
    
    # Return the decrypted plaintext
    size = plaintext[0]
    plaintext = plaintext[9: size + 1]
    return plaintext

def extract_dns_requests(pcap_file):
    dns_requests = []

    # Read the pcap file
    packets = rdpcap(pcap_file)

    # Extract DNS requests from DNS layers in each packet
    for packet in packets:
        if packet.haslayer(DNS) and packet[DNS].qr == 0:
            dns_request = packet[DNS].qd.qname.decode('utf-8')
            dns_requests.append(dns_request)

    return dns_requests

key_hex = '6cbbf2a39fc7a2a64e9217c872485e4151ecfef9e348e20707ec1bd365b1122d'
iv_hex = '000102030405060708090A0B0C0D0E0F'

pcap_file = 'only_dns_request.pcap'

dns_requests = extract_dns_requests(pcap_file)
exfiltrated_data = []
for request in dns_requests:
    b32encoded_data = request.split('.')[0] 
    if b32encoded_data in exfiltrated_data:
        continue
    else:
        #decoded_data = b32decode_nopad(b32encoded_data)
        exfiltrated_data.append(b32encoded_data)

for data  in exfiltrated_data:
#   ciphertext_base32 = one_request
    plaintext = decrypt_aes_cbc_no_padding(key_hex, iv_hex, data)
    print(plaintext)


