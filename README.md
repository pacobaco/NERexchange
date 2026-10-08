# NER Exchange

Scaffold for a named-entity attention tape and an NER model leaderboard.

Spot is a 0-100 index:

    0.45 * log10(news mentions) + 0.35 * log10(social posts) + 0.20 * log10(report citations)

scaled and nudged by news sentiment (+/- 3). Change is spot minus prior_spot.

Leaderboard ranks listings by reported CoNLL-style F1. Scores are sample figures and are not cross-comparable.

Run: `python demo.py`
