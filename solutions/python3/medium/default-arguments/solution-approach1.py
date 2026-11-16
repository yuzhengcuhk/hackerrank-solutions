# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/default-arguments/problem?isFullScreen=true
# Problem     Default Arguments
# Difficulty  Medium
# Subdomain   Debugging
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-15, 08:03 p.m.
# ──────────────────────────────────────────────────



def print_from_stream(n, stream=None):
    if not stream:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())

