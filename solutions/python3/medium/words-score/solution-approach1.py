# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/words-score/problem?isFullScreen=true
# Problem     Words Score
# Difficulty  Medium
# Subdomain   Debugging
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-15, 08:56 p.m.
# ──────────────────────────────────────────────────

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score

