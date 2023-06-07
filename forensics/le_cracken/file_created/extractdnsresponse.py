from scapy.all import rdpcap, DNSQR, DNSRR
import base64
from Crypto.Cipher import AES

def decrypt_aes_cbc_no_padding(key, iv, ciphertext):
    # Convert key and IV from hexadecimal to bytes
    key = bytes.fromhex(key)
    iv = bytes.fromhex(iv)
    
    # Base64 decode the ciphertext
    ciphertext = base64.b64decode(ciphertext)
    
    # Create AES cipher object with CBC mode and no-padding
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the ciphertext
    plaintext = cipher.decrypt(ciphertext)
    
    # Return the decrypted plaintext
    return plaintext.decode('utf-8')

def extract_dns_txt_fields(pcap_file):
    dns_txt_fields = []

    packets = rdpcap(pcap_file)
    for packet in packets:
        if DNSQR in packet and DNSRR in packet:
            if packet.qd.qtype == 16:  # Check if it's a TXT record query
                dns_txt_fields.append(packet[DNSRR].rdata)

    return dns_txt_fields

key_hex = '6cbbf2a39fc7a2a64e9217c872485e4151ecfef9e348e20707ec1bd365b1122d'
iv_hex = '000102030405060708090A0B0C0D0E0F'

pcap_file = 'only_dns_response.pcap'

dns_txt_fields = extract_dns_txt_fields(pcap_file)
all_dns_response = []
for field in dns_txt_fields: # field = list of list
    if field[0].decode() in all_dns_response:
        continue
    else:
        all_dns_response.append(field[0].decode()) # get each command

for one_response in all_dns_response:
    ciphertext_base64 = one_response
    plaintext = decrypt_aes_cbc_no_padding(key_hex, iv_hex, ciphertext_base64)
    print('Decrypted plaintext:', plaintext)

