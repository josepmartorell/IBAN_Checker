# IBAN_Checker :credit_card:
IBAN checker is a python software designed to validate an International Bank Account Number

# How to Install
First you must access from your terminal to the directory where you want to save the project. Install this project on your local computer by typing the following in the command prompt of the linux command interpreter:

git clone https://github.com/josepmartorell/IBAN_Checker.git

# Table of Contents
- Description
- Algorithm
- Credits
- Script usage
- License
 
# Description
The IBAN_Checker script implements in a slightly simplified form an algorithm used by European banks to specify account numbers. 
The standard provides a simple and fairly reliable method of validating the account numbers against simple typos that can occur during  -   rewriting of the number e.g., from paper documents, like invoices or bills, into computers...
 
# Algorithm
* An IBAN-compliant account number consists of:

    * a two-letter country code taken from the ISO 3166-1 (e.g., KZ for Kazakhstan :kneeling_woman:, KY for Cayman Islands :crocodile:);
    * two check digits used to perform the validity checks :euro:;
    * the actual account number (up to 30 alphanumeric characters – the length of that part depends on the country)

* The standard says that validation requires the following steps (according to Wikipedia):

    * (step 1) Check that the total IBAN length is correct as per the country; 
    * (step 2) Move the four initial characters to the end of the string (i.e., the country code and the check digits)
    * (step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11 .. Z = 35;
    * (step 4) Interpret the string as a decimal integer and compute the remainder of that number on division by 97; 
          * If the remainder is 1, the check digit test is passed and the IBAN might be valid.
          
```javascript
iban = input("Please enter your iban number").replace(' ','')
if not iban isalnum():
    print("invalid characters inside") 
elif len(iban) < 15:
    print("iban too short") 
elif len(iban) < 31:
    print("iban too long") 
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for char in iban:
        if char.isdigit():
            iban2 += char
        else:
            iban2 += str(10 + ord(char) - ord'A')
     iban3 = int(iban2)
     if iban3 % 97 == 1:
         print("seems legit!")
     else:
         print("I don't think it's a valid IBAN, sorry")
```
# Credits
- [ ] [wikipedia International Bank Account Number](https://en.wikipedia.org/wiki/International_Bank_Account_Number)
- [ ] [Cisco Networking Academy - PCAP: Programming Essentials in Python](https://www.netacad.com/courses/programming/pcap-programming-essentials-python)

# Script usage :roll_of_paper:
To run the script you should first access the src folder and type this line in the interpreter's order indicator to run the script:

user@hostname:~/PycharmProjects/IBAN_Checker/src$ python3 main.py

The terminal will ask you for the execution mode script. Type an lowercase "c" and press enter to display _cli_ mode and just press enter to _INTERFACE_ mode. If the validation it's OK, the script displays:

    "Iban number" (matching of four numbers starting on the left).
    "Bank code" (the actual country code format for the iban account).

# License
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
