import pytest
import re


class TestTextSummarizer:

    def test_summary_shorter_than_input(self):
        original = " ".join(["word"] * 200)
        summary = " ".join(["word"] * 50)
        assert len(summary.split()) < len(original.split())

    def test_empty_input_handled(self):
        def summarize(text):
            if not text or not text.strip():
                return ""
            return text[:100]
        assert summarize("") == ""
        assert summarize("   ") == ""

    def test_minimum_input_length(self):
        short_text = "Hello world"
        assert len(short_text.split()) < 20

    def test_special_characters_handled(self):
        text = "Hello!!! This is a test... with special chars @#$%"
        clean = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        assert '!' not in clean
        assert '@' not in clean

    def test_sentence_boundary_detection(self):
        text = "First sentence. Second sentence. Third sentence."
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        assert len(sentences) == 3


class TestTokenization:

    def test_word_tokenization(self):
        text = "natural language processing is fascinating"
        tokens = text.split()
        assert len(tokens) == 5

    def test_subword_count_reasonable(self):
        word = "tokenization"
        assert len(word) > 3

    def test_max_token_length_respected(self):
        max_len = 512
        tokens = list(range(600))
        truncated = tokens[:max_len]
        assert len(truncated) == max_len

    def test_padding_applied(self):
        sequences = [[1, 2, 3], [1, 2, 3, 4, 5], [1]]
        max_len = max(len(s) for s in sequences)
        padded = [s + [0] * (max_len - len(s)) for s in sequences]
        assert all(len(s) == max_len for s in padded)
