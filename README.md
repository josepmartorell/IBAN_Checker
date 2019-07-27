# IBAN_Checker
IBAN checker is a python software designed to validate an International Bank  Account Number

# How to Install

First you must access from your terminal to the directory where you want to save the project. Install this project on your local computer by typing the following in the command prompt of the linux command interpreter:

git clone https://github.com/josepmartorell/IBAN_Checker.git
 
# Usage

To run the script you should first access the src folder from the terminal within the project folder, similar to the following:
 
(base) hostname@user-VirtualBox:~/PycharmProjects/IBAN_Checker/src$ 

Then type an run this line at the command prompt:

python3 main.py

The terminal will ask you for the iban account number, therefor in the main file you find three accouns for testing the script. If the validation it's OK, the script displays:

-1/. "Iban number" (matching of four numbers starting on the left). 
-2/. the "Bank code", the actual country code format for the iban account.

Contributing/Contribute

Theres two bugs located at the lines 56 and 93. I will greatly thanked for any suggestion or fixes about them.

# Credits

https://en.wikipedia.org/wiki/International_Bank_Account_Number


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
