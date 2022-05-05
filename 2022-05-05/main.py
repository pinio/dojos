#!/usr/bin/env python

import unittest
import re

"""
Um número primo é definido se ele possuir exatamente dois divisores: o número um e ele
próprio. São exemplos de números primos: 2, 3, 5, 101, 367 e 523.

Neste problema, você deve ler uma palavra composta somente por letras [a-zA-Z]. Cada
letra possui um valor específico, a vale 1, b vale 2 e assim por diante, até a letra
z que vale 26. Do mesmo modo A vale 27, B vale 28, até a letra Z que vale 52.

Você precisa definir se cada palavra em um conjunto de palavras é prima ou não. Para
ela ser prima, a soma dos valores de suas letras deve ser um número primo.
"""
# Thales
# Vitor
# Rafael Bordin
# Murilo Viana
# André
# Mawkee
# Camila


class InvalidWordError(Exception):
    ...


def convert_to_int(word):
    acc = 0

    for letter in word:
        if letter.isupper():
            acc += ord(letter) - 38
        else:
            acc += ord(letter) - 96

    return acc


def is_prime(word):

    if not re.match(r"^[a-zA-Z]+$", word):
        raise InvalidWordError

    word_number = convert_to_int(word)

    for n in range(2, word_number):
        if word_number % n == 0:
            return False
    return True


def are_primes(words):
    return tuple(is_prime(word) for word in words.split(" "))


class PalavraPrimaTestCase(unittest.TestCase):
    def test_a_is_prime(self):
        self.assertTrue(is_prime("a"))

    def test_convert_a_to_1(self):
        self.assertEqual(convert_to_int("a"), 1)

    def test_convert_A_to_27(self):
        self.assertEqual(convert_to_int("A"), 27)

    def test_aBaCaTe_is_prime(self):
        self.assertFalse(is_prime("aBaCaTe"))

    def test_b_is_prime(self):
        self.assertTrue(is_prime("b"))

    def test_d_is_prime(self):
        self.assertFalse(is_prime("d"))

    def test_zeca_is_cousin(self):
        self.assertTrue(is_prime("Zeca"))

    def test_andre_accent_is_cousin(self):
        with self.assertRaises(InvalidWordError):
            is_prime("André")

    def test_long_andre_accent_is_cousin(self):
        with self.assertRaises(InvalidWordError):
            is_prime("André Garcia")

    def test_andre_punctuation_is_cousin(self):
        with self.assertRaises(InvalidWordError):
            is_prime("Andre!")

    def test_is_cousin_with_numbers(self):
        with self.assertRaises(InvalidWordError):
            is_prime("1")

    def test_is_cousin_a_a(self):
        self.assertEqual(are_primes("a a"), (True, True))

    def test_is_cousin_a_d(self):
        self.assertEqual(are_primes("a d"), (True, False))

    def test_is_cousin_aBaCaTe__Maca(self):
        self.assertEqual(are_primes("aBaCaTe Maca"), (False, False))

    def test_raise_Andre_Maca(self):
        with self.assertRaises(InvalidWordError):
            are_primes("André Maca")

    def test_lorem(self):
        self.assertTrue(is_prime("Lorem"))

    def test_ipsum(self):
        self.assertFalse(is_prime("ipsum"))

    def test_dolor(self):
        self.assertFalse(is_prime("dolor"))

    def test_sit(self):
        self.assertFalse(is_prime("sit"))

    def test_amet(self):
        self.assertFalse(is_prime("amet"))

    def test_is_lorem(self):
        self.assertEqual(
            are_primes("Lorem ipsum dolor sit amet"), (True, False, False, False, False)
        )

    def test_pinion(self):
        self.assertFalse(is_prime("PiniOn"))


if __name__ == "__main__":
    unittest.main()
