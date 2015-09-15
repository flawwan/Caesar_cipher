#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.Crypto import Crypto

crypto = Crypto(language='en_US')

crypto.decrypt_caesar(message="QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD",
					  smart_search=True)  # THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG

crypto.decrypt_vigenere(message="LXFOPVEFRNHR", secret="LEMONLEMONLE", smart_search=True)  # attackatdawn


crypto.decrypt_transposition(message="HEEUJGXDDEDOMATTGEMDMRGDELRLESIHENOSILTKANSBXGAOERIJXXTNRNLSOAXMDMXAIRNX ",
							 depth_from=1,
							 depth_to=10)  # HEMLIGTMEDDELANDEOMSTORMUMRIKENXJAGHARLAGTDENISIXTENSJORDGLOBXANDERSXXXX

crypto.encrypt_vigenere(message="blekinge", secret="BITBITBI")