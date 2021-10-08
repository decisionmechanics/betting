import pytest
from betting import convert


@pytest.mark.parametrize(
    "american_odds, expected_decimal_odds",
    [(100, 2.0), (235, 3.35), (-110, 1.9091), (-152, 1.6579)],
)
def test_american_odds_to_decimal_odds(american_odds, expected_decimal_odds):
    # Act
    actual_decimal_odds = convert.american_odds_to_decimal_odds(american_odds)

    # Assert
    assert round(actual_decimal_odds, 4) == expected_decimal_odds


@pytest.mark.parametrize(
    "american_odds, expected_fractional_odds",
    [(120, (6, 5)), (250, (5, 2)), (-120, (5, 6)), (-300, (1, 3))],
)
def test_american_odds_to_fractional_odds(american_odds, expected_fractional_odds):
    # Act
    actual_fractional_odds = convert.american_odds_to_fractional_odds(american_odds)

    # Assert
    assert actual_fractional_odds == expected_fractional_odds


@pytest.mark.parametrize(
    "decimal_odds, expected_american_odds",
    [(2.0, 100.0), (3.35, 235), (1.9091, -110), (1.6579, -152)],
)
def test_decimal_odds_to_american_odds(decimal_odds, expected_american_odds):
    # Act
    actual_american_odds = convert.decimal_odds_to_american_odds(decimal_odds)

    # Assert
    assert round(actual_american_odds) == expected_american_odds


@pytest.mark.parametrize(
    "decimal_odds, expected_fractional_odds", [(1.75, (3, 4)), (2.2, (6, 5))]
)
def test_decimal_odds_to_fractional_odds(decimal_odds, expected_fractional_odds):
    # Act
    actual_fractional_odds = convert.decimal_odds_to_fractional_odds(decimal_odds)

    # Assert
    assert actual_fractional_odds == expected_fractional_odds


@pytest.mark.parametrize(
    "fractional_odds, expected_american_odds",
    [((7, 4), 175), ((6, 5), 120), ((1, 4), -400), ((1, 10), -1000)],
)
def test_fractional_odds_to_american_odds(fractional_odds, expected_american_odds):
    # Act
    actual_american_odds = convert.fractional_odds_to_american_odds(
        fractional_odds[0], fractional_odds[1]
    )

    # Assert
    assert round(actual_american_odds) == expected_american_odds


@pytest.mark.parametrize(
    "fractional_odds, expected_decimal_odds",
    [((3, 4), 1.75), ((6, 5), 2.2)],
)
def test_fractional_odds_to_decimal_odds(fractional_odds, expected_decimal_odds):
    # Act
    actual_decimal_odds = convert.fractional_odds_to_decimal_odds(
        fractional_odds[0], fractional_odds[1]
    )

    # Assert
    assert actual_decimal_odds == expected_decimal_odds
