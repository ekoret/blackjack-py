"""Test functions for Deck"""

import pytest


from blackjack.deck import Deck


@pytest.fixture
def deck():
    deck = Deck()
    return deck


def test_deck_is_full(deck):
    """Is deck full"""
    count = 0
    for card in deck.cards:
        count += 1
    assert count == 52


def test_deal_card(deck):
    """Is the card removed the top card"""
    top_card = deck.cards[-1]
    removed_card = deck.deal_card()
    assert top_card == removed_card
