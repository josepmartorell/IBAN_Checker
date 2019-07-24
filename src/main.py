#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import module

doit = True
while doit != False:
    module.iban_validator()
    print('Enter "exit" to exit or "hold" to enter again')
    hold = input()
    if hold == 'exit':
        doit = False
    elif hold == 'hold':
        continue

'''
Test:     
  
British: GB72 HBZU 7006 7212 1253 00
French: FR76 30003 03620 00020216907 50
German: DE02100100100152517108


If you are an EU resident, you can use you own account number for tests.
'''







