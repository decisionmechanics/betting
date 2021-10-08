# Betting

Utility library to convert between betting odds.

Converts to/from:

- American/Moneyline odds
- Decimal odds
- Fractional odds
- Implied probability

## Functions

- `american_odds_to_decimal_odds(american_odds: float) -> float`
- `american_odds_to_fractional_odds(american_odds: float) -> Tuple[float, float]`
- `american_odds_to_probability(american_odds: float) -> float`
- `decimal_odds_to_american_odds(decimal_odds: float) -> float`
- `decimal_odds_to_fractional_odds(decimal_odds: float) -> Tuple[float, float]`
- `decimal_odds_to_probability(decimal_odds: float) -> float`
- `fractional_odds_to_american_odds(numerator: float, denominator: float) -> float`
- `fractional_odds_to_decimal_odds(numerator: float, denominator: float) -> float`
- `fractional_odds_to_probability(numerator: float, denominator: float) -> float`
- `probability_to_american_odds(p: float) -> float`
- `probability_to_decimal_odds(p: float) -> float`
- `probability_to_fractional_odds(p: float) -> Tuple[float, float]`