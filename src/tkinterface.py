import tkinter as tkk
import json
from src import cli

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
        self.ibanf = 0
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
        chunks = self.registry_format(code2)

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
                print('\nIBAN NUMBER: ', self.iban_formatted(iban).upper())
                print('BANK CODE...... ', self.bank_formatted(iban, chunks))
            else:
                print("Fake account!")
                print('\nIBAN NUMBER: ', self.iban_formatted(iban).upper())
                print('BANK CODE...... ', self.bank_formatted(iban, chunks))

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

    def registry_format(self, code):
        for p in data['values']:
            if p['code'] == code:
                format = p['format']
                return format

    def iban_formatted(self, iban):
        return ' '.join(iban[i:i + 4] for i in range(0, len(iban), 4))

    def bank_formatted(self, iban, chunks):
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


if __name__ == '__main__':

    mode = input('\nSelect run mode:'
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
