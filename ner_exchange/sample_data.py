from __future__ import annotations

from datetime import datetime, timedelta

from .models import EntityQuote, ModelListing, NewsItem, ReportCite, SocialSnap

NOW = datetime(2026, 10, 8, 16, 30)


def _n(source, headline, mentions, hours_ago, sentiment) -> NewsItem:
    return NewsItem(source, headline, mentions, NOW - timedelta(hours=hours_ago), sentiment)


def _s(platform, posts, authors, engagement, hours_ago) -> SocialSnap:
    return SocialSnap(platform, posts, authors, engagement, NOW - timedelta(hours=hours_ago))


def entities() -> list[EntityQuote]:
    return [
        EntityQuote(
            "PER.TRUMP", "Donald Trump", "PER", prior_spot=96.3,
            news=[
                _n("Reuters", "White House statement on trade", 8200, 2, -0.1),
                _n("AP", "Campaign rally coverage", 6400, 8, 0.2),
                _n("BBC", "Policy briefing", 5100, 14, 0.0),
            ],
            social=[
                _s("X", 620000, 180000, 2400000, 1),
                _s("Reddit", 48000, 22000, 310000, 3),
            ],
            reports=[ReportCite("Entity salience in US political news", "ACL demo", 120, 2025)],
        ),
        EntityQuote(
            "ORG.GOOG", "Google", "ORG", prior_spot=85.6,
            news=[
                _n("WSJ", "Search antitrust update", 5400, 5, -0.3),
                _n("The Verge", "AI overview citation study", 3100, 11, 0.4),
            ],
            social=[_s("X", 210000, 90000, 640000, 2), _s("LinkedIn", 18000, 9000, 40000, 6)],
            reports=[
                ReportCite("Brand mentions in AI overviews", "SE Ranking", 40, 2026),
                ReportCite("FinBERT NER on tech filings", "arXiv", 210, 2023),
            ],
        ),
        EntityQuote(
            "ORG.EU", "European Union", "ORG", prior_spot=75.5,
            news=[_n("FT", "EU policy update", 4900, 4, -0.2), _n("Politico", "Commission briefing", 3600, 9, 0.1)],
            social=[_s("X", 140000, 60000, 210000, 2)],
            reports=[ReportCite("Multilingual NER on EU texts", "ACL", 180, 2024)],
        ),
        EntityQuote(
            "PER.XI", "Xi Jinping", "PER", prior_spot=71.5,
            news=[_n("SCMP", "Bilateral talks", 4100, 6, 0.0), _n("Reuters", "Summit readout", 3900, 18, 0.1)],
            social=[_s("Weibo", 200000, 70000, 500000, 4), _s("X", 40000, 18000, 90000, 4)],
            reports=[ReportCite("Cross-lingual person NER", "EMNLP", 90, 2024)],
        ),
        EntityQuote(
            "ORG.AMZN", "Amazon", "ORG", prior_spot=63.3,
            news=[_n("CNBC", "Retail earnings preview", 2800, 7, 0.2)],
            social=[_s("X", 160000, 70000, 300000, 3), _s("Reddit", 22000, 11000, 80000, 5)],
            reports=[ReportCite("Product entity linking", "KDD", 70, 2022)],
        ),
        EntityQuote(
            "ORG.MSFT", "Microsoft", "ORG", prior_spot=57.7,
            news=[_n("Bloomberg", "Cloud contract", 2500, 3, 0.5)],
            social=[_s("LinkedIn", 30000, 14000, 70000, 2), _s("X", 120000, 50000, 200000, 2)],
            reports=[ReportCite("Enterprise NER pipelines", "VLDB", 150, 2025)],
        ),
        EntityQuote(
            "ORG.AAPL", "Apple", "ORG", prior_spot=55.8,
            news=[_n("9to5Mac", "Supply chain note", 1900, 10, 0.1)],
            social=[_s("X", 250000, 100000, 700000, 1)],
            reports=[ReportCite("Consumer brand NER", "WWW", 60, 2021)],
        ),
        EntityQuote(
            "ORG.OPENAI", "OpenAI", "ORG", prior_spot=48.1,
            news=[_n("TechCrunch", "Model release notes", 2200, 1, 0.6)],
            social=[_s("X", 300000, 120000, 900000, 1), _s("Reddit", 35000, 15000, 140000, 2)],
            reports=[ReportCite("LLM NER zero-shot", "arXiv", 340, 2026)],
        ),
        EntityQuote(
            "LOC.US", "United States", "LOC", prior_spot=49.0,
            news=[_n("NYT", "Markets wrap", 7000, 6, 0.0), _n("WSJ", "Fed minutes", 4200, 2, -0.1)],
            social=[_s("X", 90000, 40000, 120000, 3)],
            reports=[ReportCite("CoNLL-2003 revisited", "TACL", 500, 2023)],
        ),
        EntityQuote(
            "MISC.NFL", "National Football League", "MISC", prior_spot=39.2,
            news=[_n("ESPN", "Week 5 injury report", 1600, 4, 0.3)],
            social=[_s("X", 540000, 200000, 1800000, 1), _s("Reddit", 80000, 30000, 400000, 2)],
            reports=[ReportCite("Sports entity disambiguation", "workshop", 12, 2024)],
        ),
    ]


def listings() -> list[ModelListing]:
    return [
        ModelListing("ACE", "ACE-PT", "~355M", 93.2, 61.0, "Supervised encoder, CoNLL band", 240),
        ModelListing("LUKE", "LUKE-class", "large", 94.6, None, "Reported CoNLL-2003 peak (Wang et al.)", 410),
        ModelListing("STANZA", "Stanza-en", "Flair+RNN", 92.1, None, "Stanford English CoNLL03", 380),
        ModelListing("NT3", "NameTag 3", "355M", 94.1, None, "Span NER on full CoNLL test", 55),
        ModelListing("GLINER", "GLiNER-large", "460M", 73.9, 59.9, "Zero-shot; stronger on novel entities", 190),
        ModelListing("Q3-4B", "Qwen3-4B-Inst", "4B", 75.3, 50.6, "Generative; slips on WNUT-style noise", 80),
        ModelListing("RNER", "ReasoningNER", "7-8B", 85.2, None, "CrossNER/MIT average, not pure CoNLL", 30),
        ModelListing("OTTER", "OTTER", "small enc.", 48.9, None, "Zero-shot multilingual macro", 20),
        ModelListing("SPACY", "spaCy-sm", "13M", 59.5, 26.1, "Deployable baseline", 600),
        ModelListing("CRF", "CRF classic", "-", 88.0, None, "Pre-transformer reference", 900),
    ]
