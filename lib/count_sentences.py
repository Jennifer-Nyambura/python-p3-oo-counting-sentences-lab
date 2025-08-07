#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # Triggers the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        import re
        # Use regex to split by punctuation that could end a sentence
        parts = re.split(r'[.!?]', self.value)
        # Filter out empty strings and whitespace
        sentences = [part for part in parts if part.strip()]
        return len(sentences)

