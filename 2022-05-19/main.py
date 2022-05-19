#!/usr/bin/env python

import unittest

OPERANDS = ["true", "false"]
OPERATORS = ["xor", "and", "or"]


def evalutate_expr(expr: str) -> bool:
    expr = expr.replace("true", "True").replace("false", "False").replace("xor", "!=")
    return eval(expr)


def get_variants(expression):
    tokens = expression.split(" ")

    if len(tokens) <= 3:
        return [expression]

    return [
        expression,
        f"({' '.join(tokens[0:3])}) {' '.join(tokens[3:])}",
        f"{' '.join(tokens[:2])} ({' '.join(tokens[2:5])})",
    ]


def count_parents(expression):
    all_expressions = get_variants(expression)
    return sum(evalutate_expr(e) for e in all_expressions)


class CountingParentsTestCase(unittest.TestCase):
    def test_true(self):
        self.assertEqual(count_parents("true"), 1)

    def test_false(self):
        self.assertEqual(count_parents("false"), 0)

    def test_true_and_true(self):
        self.assertEqual(count_parents("true and true"), 1)

    def test_true_and_false(self):
        self.assertEqual(count_parents("true and false"), 0)

    def test_true_or_false(self):
        self.assertEqual(count_parents("true or false"), 1)

    def test_false_or_false(self):
        self.assertEqual(count_parents("false or false"), 0)

    def test_true_xor_true(self):
        self.assertEqual(count_parents("true xor true"), 0)

    def test_false_xor_true(self):
        self.assertEqual(count_parents("false xor true"), 1)

    def test_false_and_true_and_true(self):
        self.assertEqual(count_parents("false and true and true"), 0)

    def test_true_and_true_and_true(self):
        self.assertEqual(count_parents("true and true and true"), 3)

    def test_false_and_false_and_false(self):
        self.assertEqual(count_parents("false and false and false"), 0)

    def test_false_and_false_or_true(self):
        self.assertEqual(count_parents("false and false or true"), 2)

    def test_true_and_false_or_true(self):
        self.assertEqual(count_parents("true and false or true"), 3)

    def test_true_or_false_or_true(self):
        self.assertEqual(count_parents("true or false or true"), 3)

    def test_true_xor_false_and_true(self):
        self.assertEqual(count_parents("true xor false and true"), 3)

    def test_true_and_false_xor_true(self):
        self.assertEqual(count_parents("true and false xor true"), 3)


if __name__ == "__main__":
    unittest.main()
