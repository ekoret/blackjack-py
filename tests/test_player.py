"""Test functions for Player"""

import pytest

from blackjack.player import Player
from blackjack.card import Card
from blackjack.game import BlackJack


@pytest.fixture
def blackjack_game():
    game = BlackJack()
    return game


@pytest.fixture
def player():
    player1 = Player("1")
    return player1


@pytest.fixture
def card():
    card = Card(10, "H")
    return card


def test_player_add_card(player, card, game):
    player.game = game
    player.add_card(card)
    assert player.hand[0].value == 10
    assert player.hand[0].suit == "H"
