from fractions import Fraction
from typing import Tuple

FractionalOddsType = Tuple[float, float]


def american_odds_to_decimal_odds(american_odds: float) -> float:
    return probability_to_decimal_odds(american_odds_to_probability(american_odds))


def american_odds_to_fractional_odds(american_odds: float) -> FractionalOddsType:
    return decimal_odds_to_fractional_odds(american_odds_to_decimal_odds(american_odds))


def american_odds_to_probability(american_odds: float) -> float:
    return (
        100.0 / (american_odds + 100.0)
        if american_odds >= 0.0
        else -american_odds / (-american_odds + 100.0)
    )


def decimal_odds_to_american_odds(decimal_odds: float) -> float:
    return (
        (decimal_odds - 1.0) * 100.0
        if decimal_odds >= 2.0
        else -100.0 / (decimal_odds - 1.0)
    )


def decimal_odds_to_fractional_odds(decimal_odds: float) -> FractionalOddsType:
    fractional_odds = Fraction(decimal_odds - 1.0).limit_denominator()

    return fractional_odds.numerator, fractional_odds.denominator


def decimal_odds_to_probability(decimal_odds: float) -> float:
    return 1.0 / decimal_odds_to_american_odds


def fractional_odds_to_american_odds(numerator: float, denominator: float) -> float:
    return probability_to_american_odds(
        fractional_odds_to_probability(numerator, denominator)
    )


def fractional_odds_to_decimal_odds(numerator: float, denominator: float) -> float:
    return probability_to_decimal_odds(
        fractional_odds_to_probability(numerator, denominator)
    )


def fractional_odds_to_probability(numerator: float, denominator: float) -> float:
    return denominator / (numerator + denominator)


def probability_to_american_odds(p: float) -> float:
    return decimal_odds_to_american_odds(probability_to_decimal_odds(p))


def probability_to_decimal_odds(p: float) -> float:
    return 1.0 / p


def probability_to_fractional_odds(p: float) -> FractionalOddsType:
    return decimal_odds_to_fractional_odds(probability_to_decimal_odds(p))
