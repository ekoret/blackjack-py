"""Test functions for Card"""

import pytest

from blackjack.card import Card


@pytest.fixture
def card():
    """A single card that will be availible for all test functions"""
    card = Card(2, "C")
    return card


def test_card_creation_value(card):
    """Does card have correct value"""
    assert card.value == 2


def test_card_creation_suit(card):
    """Does card have correct suit"""
    assert card.suit == "C"
