# Mol.E-Crypter

Mol.E-Crypter works to convert a plain text document into an encrypted file (extension .bin) using the Pycryptodome python library (https://github.com/Legrandin/pycryptodome/blob/master/Doc/src/features.rst) and subsequently decode the encrypted file if the user enters in the correct secret key. The secret key is entered via sequencing oligourethanes and entering the masses into a spreadsheet, that is read by the decrypting program and if the key is correct, the unencrypted text file is output.

### Mol.Encrypter Usage
The first part of Mol.Encrypter.py uses a secure random number generator to be the secret key. A text document is the read in and undergoes AES-256 encryption and is then output as a .bin in addition to the secret key being output as a .txt file.   

To run this program the program takes a single input: a text document containing the text to be encoded.

The following is an example input:

```bash
run Mol.Encrypter.py -f NAMEOFTXTDOC.txt
```


The program then outputs two files, encrypted.bin and secretkey.txt. The first file, encrypted.bin, contains an AES encrypted file that can only be deciphered using the secret key. The second file is the secret key, converted from binary into its hexadecimal representation to be encoded into oligourethanes. 

For additional help running this program, use the -h flag.

### Mol.Decrypter Usage
The second part of Mol.E-Crypter is Mol.Decoder.py. This program takes in three inputs, the encrypted file, the file containing the monomers correlation to hexadecimal, and the masses determining from sequencing the oligourethanes.
The program first reads in the monomers from the excel file containing the sequenced masses and generates the corresponding hexadecimal representation that is then converted to binary to decrypt the file. If it is the correct secret key, the file will be decrypted and a txt file containing the information will be created.
The following is an example input and output:

```bash
run Mol.Decrypter.py -e encrypted.bin -m MonomerToHexCodes.xlsx -t NAMEOFDECRYPTEDMONOMERSFILE.xlsx
```

If this was the correct secret key the output will be:

```python
Successfully Decrypted```

If not, the program will print out:
```python
Incorrect Key
```

For additional help running this program, use the -h flag.
