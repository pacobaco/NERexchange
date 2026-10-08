from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class NewsItem:
    source: str
    headline: str
    mentions: int
    published_at: datetime
    sentiment: float  # -1..1


@dataclass
class SocialSnap:
    platform: str
    posts: int
    unique_authors: int
    engagement: int
    captured_at: datetime


@dataclass
class ReportCite:
    title: str
    venue: str
    citations: int
    year: int


@dataclass
class EntityQuote:
    symbol: str
    name: str
    entity_type: str  # PER, ORG, LOC, MISC
    news: list[NewsItem] = field(default_factory=list)
    social: list[SocialSnap] = field(default_factory=list)
    reports: list[ReportCite] = field(default_factory=list)
    prior_spot: float = 50.0

    @property
    def news_mentions(self) -> int:
        return sum(n.mentions for n in self.news)

    @property
    def social_volume(self) -> int:
        return sum(s.posts for s in self.social)

    @property
    def report_weight(self) -> int:
        return sum(r.citations for r in self.reports)

    @property
    def sentiment(self) -> float:
        if not self.news:
            return 0.0
        w = sum(n.mentions for n in self.news) or 1
        return sum(n.sentiment * n.mentions for n in self.news) / w


@dataclass
class ModelListing:
    ticker: str
    name: str
    params: str
    conll_f1: float | None
    noisy_f1: float | None
    notes: str
    report_cites: int = 0

    @property
    def spread(self) -> float | None:
        if self.conll_f1 is None or self.noisy_f1 is None:
            return None
        return round(self.conll_f1 - self.noisy_f1, 1)
