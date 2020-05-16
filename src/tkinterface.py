import tkinter as tkk
import json
import cli

with open('iban.json', 'r') as json_file:
    data = json.load(json_file)


class Application(tkk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.check = tkk.Button(self)
        self.exit = tkk.Button(self)
        self.parameter = tkk.StringVar()
        self.entry = tkk.Entry(textvariable=self.parameter)
        self.entry.pack(side=tkk.RIGHT)
        self.pack(side="left")
        self.create_widgets()
        self.length = 0
        self.country = ""
        master.title("IBAN_Checker")
        master.configure(background="white")
        master.geometry("600x64")

    def create_widgets(self):
        self.check.place(x=0, y=0)
        self.check["text"] = "CHECK IBAN NUMBER"
        self.check["command"] = self.check_iban
        self.check["fg"] = "red"
        self.check.pack(side="top")
        self.exit.config(text="exit iban validator", command=self.master.destroy)
        self.exit.pack(side="left", expand=50, fill="x")
        self.entry.pack(side="right", ipadx=131, fill="x")

    def check_iban(self):
        iban = self.parameter.get()
        # let's eliminate the empty spaces
        iban = iban.replace(' ', '')
        # let's control the input data type
        if not iban.isalnum():
            print("Invalid characters inside IBAN - sorry!")
        # (step 1) Check that the total IBAN length is correct
        code2 = (iban[0:2].upper())
        length2 = self.registry_length(code2)
        name_country = self.registry_country(code2)

        if not code2.isalpha():
            print("Invalid country code")
        elif len(iban) < int(length2):
            print("IBAN too short")
            print("the length for ", name_country, " IBAN is: ", length2)
        elif len(iban) > int(length2):
            print("IBAN too long")
            print("the length for ", name_country, " IBAN is: ", length2)
        # (step 2) Move the four initial characters to the end of the string
        else:
            iban_rearranged = (iban[4:] + iban[0:4]).upper()
            # (step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10,
            # B = 11 .. Z = 35;
            iban2 = ''
            for ch in iban_rearranged:
                if ch.isdigit():
                    iban2 += ch
                else:
                    iban2 += str(10 + ord(ch) - ord('A'))
            # (step 4) Interpret the string as a decimal integer and compute the remainder of that number on division
            # by 97; If the remainder is 1, the check digit test is passed and the IBAN might be valid.
            ibann = int(iban2)
            if ibann % 97 == 1:
                print("Seems legit!")
                print('\nIban number: ', self.iban_formatted(iban).upper())
            else:
                print("Fake account!")
                print('\nIban number: ', self.iban_formatted(iban).upper())

    def registry_length(self, code):
        for p in data['values']:
            if p['code'] == code:
                self.length = p['length']
        return self.length

    def registry_country(self, code):
        for p in data['values']:
            if p['code'] == code:
                self.country = p['country']
        return self.country

    def iban_formatted(self, iban):
        return ' '.join(iban[i:i + 4] for i in range(0, len(iban), 4))


if __name__ == '__main__':

    mode = input('\nSelect spider run mode:'
                 '\n\tCLI .........(type "c" + enter)'
                 "\n\tINTERFACE ....(press enter)\n")

    if mode == "c":
        doit = True
        while doit != False:
            cli.iban_validator()
            print('Enter "exit" to exit or "hold" to enter again')
            hold = input()
            if hold == 'exit':
                doit = False
            elif hold == 'hold':
                continue

    if mode != "c":
        root = tkk.Tk()
        app = Application(master=root)
        app.mainloop()

''' examples:  
British: GB72 HBZU 7006 7212 1253 00
French: FR76 30003 03620 00020216907 50
German: DE02100100100152517108
If you are an EU resident, you can use you own account number for tests.
'''
