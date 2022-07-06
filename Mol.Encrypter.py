# -*- coding: utf-8 -*-
import os
import argparse
import binascii
import secrets
from Cryptodome.Cipher import AES


def GetArgs():
    '''
    parses script arguments to make running this script more intuitive

    Raises
    ------
    FileNotFoundError
        raises error if file cannot be found.

    Returns
    -------
    args : string
        returns the filename of the txt to be encrypted.

    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', metavar='\b',
                        help="name of file to be encrypted", action="store", dest="filename")
    args = parser.parse_args()

    args.filename = "C:\\Github\\Mol.E-Crypter\\TheWonderfulWizardofOz.txt"

    # Check if file exists
    if os.path.exists('{}'.format(args.filename)) is False:
        print('{}'.format(args.filename))
        raise FileNotFoundError('Cannot find {}'.format(args.filename))

    return args


def main():
    # get name of csv to read in and write out
    #script, txt_file_name = argv

    args = GetArgs()
    txt_file_name = args.filename

    # open txt to be encrypted
    txt_to_encrypt = open(txt_file_name, "r", encoding="utf-8-sig")
    txt_to_encrypt = txt_to_encrypt.read()
    txt_to_encrypt = txt_to_encrypt.encode("utf-8")

    # randomly generate 32 bytes to encrypt the file with
    #key = secrets.token_bytes(32)

    # add hex code here if using a existing key
    key = b'0d3d0288b7a9d0a66af7a1cc134476f53c6e399bb92cd1a6006142c335a8e47d'


    # convert the files to monomers and output key as a txtfile to synthesize the key
    monomer_string = str(binascii.b2a_hex(key))
    monomer_string = monomer_string[2:(len(monomer_string) - 1)]
    #print(monomer_string)
    
    key_file = open("secret_key.txt", 'w+')
    key_file.write(monomer_string)
    key_file.close()

    
    
    print(binascii.a2b_hex(key))
    key = binascii.a2b_hex(key)
    
    # create cipher and encrypt
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(txt_to_encrypt)

    # write out encrypted file as a .bin file
    file_out = open("encrypted.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()


main()
