from __future__ import annotations

import math

from .models import EntityQuote


def _log_scale(value: int, cap: float = 100.0) -> float:
    if value <= 0:
        return 0.0
    return min(cap, 18.0 * math.log10(value + 1))


def spot(quote: EntityQuote, weights: tuple[float, float, float] = (0.45, 0.35, 0.20)) -> float:
    """Composite 0-100 index from news mentions, social posts, report citations."""
    wn, ws, wr = weights
    raw = (
        wn * _log_scale(quote.news_mentions)
        + ws * _log_scale(quote.social_volume)
        + wr * _log_scale(quote.report_weight, cap=80.0)
    )
    raw += 3.0 * quote.sentiment
    return round(max(0.0, min(100.0, raw)), 1)


def change(quote: EntityQuote) -> float:
    return round(spot(quote) - quote.prior_spot, 1)
