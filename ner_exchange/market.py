from __future__ import annotations

from .models import EntityQuote, ModelListing
from .pricing import change, spot


class NERExchange:
    def __init__(self, entities: list[EntityQuote], listings: list[ModelListing]):
        self.entities = entities
        self.listings = listings

    def tape(self) -> list[dict]:
        rows = []
        for q in self.entities:
            rows.append({
                "symbol": q.symbol,
                "name": q.name,
                "type": q.entity_type,
                "spot": spot(q),
                "chg": change(q),
                "news": q.news_mentions,
                "social": q.social_volume,
                "reports": q.report_weight,
                "sentiment": round(q.sentiment, 2),
            })
        rows.sort(key=lambda r: r["spot"], reverse=True)
        return rows

    def leaderboard(self) -> list[dict]:
        ranked = sorted(
            self.listings,
            key=lambda m: (m.conll_f1 is not None, m.conll_f1 or -1),
            reverse=True,
        )
        out = []
        for i, m in enumerate(ranked, 1):
            out.append({
                "rank": i,
                "ticker": m.ticker,
                "name": m.name,
                "params": m.params,
                "conll_f1": m.conll_f1,
                "noisy_f1": m.noisy_f1,
                "spread": m.spread,
                "cites": m.report_cites,
                "notes": m.notes,
            })
        return out

    def render(self) -> str:
        lines = ["NER TAPE — NAMED ENTITY MARKET", "-" * 88]
        header = f"{'SYMBOL':<12} {'SPOT':>6} {'CHG':>7} {'NEWS':>8} {'SOCIAL':>10} {'REPORTS':>8} {'SENT':>6}"
        lines.append(header)
        for r in self.tape():
            lines.append(
                f"{r['symbol']:<12} {r['spot']:6.1f} {r['chg']:+7.1f} {r['news']:8d} {r['social']:10d} {r['reports']:8d} {r['sentiment']:6.2f}"
            )
        lines.append("")
        lines.append("NER EXCHANGE — MODEL LEADERBOARD")
        lines.append("-" * 88)
        lines.append(f"{'#':<4} {'TICKER':<8} {'NAME':<16} {'CONLL':>6} {'NOISY':>6} {'SPREAD':>7} {'CITES':>6}")
        for r in self.leaderboard():
            conll = f"{r['conll_f1']:.1f}" if r["conll_f1"] is not None else "  -"
            noisy = f"{r['noisy_f1']:.1f}" if r["noisy_f1"] is not None else "  -"
            spread = f"{r['spread']:+.1f}" if r["spread"] is not None else "  -"
            lines.append(
                f"{r['rank']:<4} {r['ticker']:<8} {r['name']:<16} {conll:>6} {noisy:>6} {spread:>7} {r['cites']:6d}"
            )
        lines.append("")
        lines.append("Notes: F1 columns are not cross-comparable across benchmarks.")
        return "\n".join(lines)
