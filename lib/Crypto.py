# -*- coding: utf-8 -*-
from enchant.checker import SpellChecker


class Crypto:
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
	long_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
	cipher_text = ""
	spell_check = None
	language = "en_US"
	decrypted_list = {}

	def __init__(self, language):
		self.language = language

	def decrypt_caesar(self, message, smart_search):
		message = message.lower()
		self.decrypted_list = {}

		for i in xrange(0, len(self.alphabet)):
			possibly_decrypted_string = ""
			for char in message:
				# If space, skip
				if char == " ":
					possibly_decrypted_string += " "
					continue
				# Find the location in the alphabet
				char_index = self.alphabet.index(char)
				# Rotate all letters -1 to the left
				if char_index - i >= len(self.alphabet):
					char_index = 0
				# Get the new character
				possibly_decrypted_string += self.alphabet[char_index - i]
			if not smart_search:
				print possibly_decrypted_string + " (" + str(i) + ")"
			else:
				self.smart_search(possibly_decrypted_string)
		if smart_search:
			print "Best matches: " + str.join(",\n", self.decrypted_list[
				sorted(self.decrypted_list.iterkeys(), key=lambda k: self.decrypted_list[k], reverse=True)[0]])

	def smart_search(self, spell_check_string):
		self.spell_check = SpellChecker(self.language)
		errors = self.search_words(spell_check_string)
		if not self.decrypted_list.get(errors):
			self.decrypted_list[errors] = [spell_check_string]
		else:
			self.decrypted_list[errors].append(spell_check_string)


	def generate_vigenere_tables(self):
		i = 0
		alphabets = []
		for k in xrange(0, len(self.alphabet)):
			new_alpha = ""
			for a in self.long_alphabet:
				ind = self.long_alphabet.index(a)
				if ind + i >= len(self.long_alphabet):
					ind = 0
				new_alpha += self.long_alphabet[ind + i]
			alphabets.append(new_alpha[:26])
			i += 1
		return alphabets


	def decrypt_vigenere(self, message, secret, smart_search):
		self.vigenere(message, secret, smart_search, True)

	def encrypt_vigenere(self, message, secret):
		self.vigenere(message, secret, False, False)

	def vigenere(self, message, secret, smart_search, do_decrypt):
		message = message.lower()
		secret = secret.lower()
		self.decrypted_list = {}
		new_ciphered_text = message
		tables = self.generate_vigenere_tables()
		for i in xrange(0, len(self.alphabet)):
			cipher_text = new_ciphered_text
			new_ciphered_text = ""
			cipher_index = 0
			for key in secret:
				if key == " ":
					new_ciphered_text += " "
					cipher_index += 1
					continue
				secret_key_index = self.long_alphabet.index(key)
				cipher_char = cipher_text[cipher_index]

				if do_decrypt:
					deciphered_index = tables[secret_key_index].index(cipher_char)
					new_ciphered_text += self.alphabet[deciphered_index]
				else:
					deciphered_index = self.alphabet.index(cipher_char)
					new_ciphered_text += tables[secret_key_index][deciphered_index]
				cipher_index += 1
			if not smart_search:
				print new_ciphered_text + " (" + str(i) + ")"
			else:
				self.smart_search(new_ciphered_text)
		if smart_search:
			print "Best matches: " + str.join(",\n", self.decrypted_list[
				sorted(self.decrypted_list.iterkeys(), key=lambda k: self.decrypted_list[k], reverse=True)[0]])


	def search_words(self, string):
		self.spell_check.set_text(string)
		total_errors = 0
		for err in self.spell_check:
			total_errors += 1
		return total_errors

	def decrypt_transposition(self, message, depth_from, depth_to):

		for depth in xrange(depth_from, depth_to + 1):
			print "This is depth " + str(depth)
			encrypted_string = message.decode("utf-8")
			dictionary = {}
			interation = 0
			while True:
				if len(encrypted_string) < depth:
					break
				# first letter does not exist
				depth_line = encrypted_string[:depth]
				# print depth_line
				cur_index = 0
				for char in depth_line:
					if not dictionary.get(cur_index):
						dictionary[cur_index] = [char]
					else:
						dictionary[cur_index].append(char)
					cur_index += 1

				encrypted_string = encrypted_string[depth:]
				interation += 1

			for word in dictionary:
				line = ""
				for char in dictionary[word]:
					line += char
				print line