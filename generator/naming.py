import random
import os.path

class NameGenerator:

	PREFIX_FIRSTWORDS = 'generator/firstwords'
	PREFIX_LASTWORDS = 'generator/lastwords'
	SUFFIX_MEMBER = 'member'

	def __init__ (self, type=''):
		self.__type = type
		self.__firstwords = self.readWords(self.PREFIX_FIRSTWORDS)
		self.__lastwords = self.readWords(self.PREFIX_LASTWORDS)

	def readWords(self, preffix):
		words = []
		filename = preffix
		if self.__type == '' or not os.path.isfile(preffix + self.__type):
			filename += self.SUFFIX_MEMBER
		else:
			filename += self.__type

		with open(filename) as wordsFile:
			for word in wordsFile:
				words.append(word.rstrip())
		return words

	def generate(self):
		return self.generateFirstName() + " " + self.generateLastName()

	def generateFirstName(self):
		return self.randomWord(self.__firstwords)

	def generateLastName(self):
		return self.randomWord(self.__lastwords)
	
	def randomWord(self, words=[]):
		return words[random.randint(0, len(words) - 1)]
