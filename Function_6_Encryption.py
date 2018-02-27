import string


# skapar en lista med alla letters och digits
KRYP_LISTA = list(string.digits) + list(string.ascii_letters) + list(string.punctuation)

# gör om listan till en dictionary
# första siffra blir key och sissta siffran blir value
kryp_dict = {}
for i in range(len(KRYP_LISTA)):
    kryp_dict[KRYP_LISTA[i]] = KRYP_LISTA[-i-1]


def main ():

    # input om man vill kryptera eller dekryptera
    choice = input("do you want to encrypt a file choose (e),"
                   " or decrypt file choose (d): ")

    # encrypt choice
    if choice == 'e':
        filenamee = input("choose file: ")    # välja vilken fil att kryptera
        enc_filestring = encrypt(filenamee,kryp_dict)
        print(enc_filestring)               # printa en krypterad string av filen man valde(behövs inte)
        write_to_file(enc_filestring)

    # decrypt choice
    if choice == 'd':
        filenamed = input("choose file: ")    #välja vilken fil att dekryptera
        dec_filestring = decrypt(filenamed, kryp_dict)
        print(dec_filestring)               # printa en dekrypterad string av filen man valde(behövs inte)
        write_to_file(dec_filestring)

def encrypt(filenamee,kryp_dict):

    enc_string = ""
    my_file = open(filenamee, 'r')
    readfile = my_file.read().rstrip()      # läser filen

    for letter in readfile.lower():         # går igen varje character från filen
        if letter in kryp_dict:             # kontrollerar ifall character finns i dictionary
            enc_string += kryp_dict[letter] # isf lägg till valuet i stringen
        else:
            enc_string += letter            # annars lägg bara till character -
                                            # annars fungerar inte programet om en symbol dyker upp som inte är med i dict
    my_file.close()
    return enc_string


def decrypt(filenamed, kryp_dict ):


    dec_string = " "
    my_file = open(filenamed, 'r')
    readfile = my_file.read().rstrip()

    for letter in readfile.lower():
        if letter in kryp_dict:
            dec_string += kryp_dict[letter]
        else:
            dec_string += letter

    return dec_string


def write_to_file(to_file):

    # välj vad den nya filen ska heta och skriv det
    # kryterade eller dekrypterad stringen i filen och spara
    filename = input("choose what you want the new file to be named: ")
    myfile = open(filename, 'w')
    myfile.write(to_file)
    myfile.close()

main()
