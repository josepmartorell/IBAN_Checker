import json

# let's read and load json file
with open('iban.json', 'r') as json_file:
    data = json.load(json_file)

# let's initialize variables that are to be globalized within functions
length = 0
country = 0
ibanf = 0


# let's get the length from the json file
def registry_length(code):
    global length
    for p in data['values']:
        if p['code'] == code:
            length = p['length']
    return length


# let's get the country name from the json file
def registry_country(code):
    global country
    for p in data['values']:
        if p['code'] == code:
            country = p['country']
    return country


# let's get the bank code from the json file
def registry_format(code):
    for p in data['values']:
        if p['code'] == code:
            format = p['format']
            return format


# Let's get the IBAN formatted in blocks of 4 digits
def iban_formatted(iban):
    return ' '.join(iban[i:i + 4] for i in range(0, len(iban), 4))


# Let's get the BANK code format
def bank_formatted(iban, chunks):
    # list '!' positions
    # chunks = registry_format(code.upper())
    list = []
    counter = 0
    for i in chunks:
        if (i.find('!')) == 0:
            list.append(counter)
        counter += 1

    # list quantity of digits per cell
    list2 = []
    i = -1
    for j in list:
        if (list[i + 1]) - (list[i]) == 3:
            list2.append(1)
        else:
            list2.append(2)
        i += 1

    i = 1

    list3 = ['0']
    n = 1
    for k in chunks:
        if i in list:
            if i == 3:
                list3.append('4')
            elif list2[n] != 1:
                list3.append('1' + k)
                n += 1
            else:
                list3.append(k)
                n += 1
        i += 1

    # cast into int type
    list4 = [int(x) for x in list3]

    list5 = []
    c = 0
    for i in list4:
        c += i
        list5.append(c)

    try:
        global ibanf
        ibanf = []
        r = -1
        c = 0
        for i in iban:
            x = list5[r - 1]
            y = list5[r]
            if c != 0:
                ibanf.append(iban[x:y])
            r += 1
            c += 1


    except:
        pass

    ibanf.pop(0)
    return ' '.join(ibanf)  # TRACE----


# Let's call the validator
def iban_validator():
    # let's enter the IBAN
    iban = input("Enter IBAN, please: ")

    # let's eliminate the empty spaces
    iban = iban.replace(' ', '')

    # let's control the input data type
    if not iban.isalnum():
        print("Invalid characters inside IBAN - sorry!")

    # (step 1) Check that the total IBAN length is correct
    code2 = (iban[0:2].upper())
    length2 = registry_length(code2)
    name_country = registry_country(code2)
    chunks = registry_format(code2)
    if not code2.isalpha():
        print("Invalid country code")
    elif len(iban) < int(length2):
        print("IBAN too short")
        print("the length for ", name_country, " IBAN is: ", length2)
    elif len(iban) > int(length2):
        print("IBAN too long")
        print("the length for ", name_country, " IBAN is: ", length2)

    # (step 2) Move the four initial characters to the end of the string (i.e., the country code and the check digits)
    else:
        iban_rearranged = (iban[4:] + iban[0:4]).upper()

        # (step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11 .. Z = 35;
        iban2 = ''
        for ch in iban_rearranged:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))

        # (step 4) Interpret the string as a decimal integer and compute the remainder of that number on division by 97;
        # If the remainder is 1, the check digit test is passed and the IBAN might be valid.
        ibann = int(iban2)
        if ibann % 97 == 1:
            print("Seems legit!")
            print('IBAN NUMBER.... ', iban_formatted(iban).upper())
            print('BANK CODE...... ', bank_formatted(iban, chunks))  # TRACE----
        else:
            print("I don't think it's a valid IBAN, sorry")
