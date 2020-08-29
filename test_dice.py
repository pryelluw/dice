from dice import Dice


def test_roll_20_sided_dice_returns_equal_or_less_that_20():
    dice = Dice(20)
    n = dice.roll()
    assert n > 0 and n <= 20
