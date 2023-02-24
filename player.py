
from game_text import GameText
from sprite import DealerSprite


class Player:
    def __init__(self, game, name=""):
        """Pygame init"""
        self.game = game

        """Self init"""
        self.name = name
        self.hand = []
        self.cards_played = []
        self.x = -1
        self.y = game.settings.screen_height - 200

    def __str__(self):
        return f"Player({self.name})"

    def draw(self):
        """
        Draws the player's hand and name on the game screen.

        Returns:
            None
        """
        player_label = GameText(self.name)
        cards_label = GameText(self.get_hand())

        cards_label.draw(self.game.screen, self.x, self.y + 20)
        player_label.draw(self.game.screen, self.x, self.y)

    def add_card(self, card):
        """
        Adds a single card to the player's hand.

        Args:
            card (Card): The card to add to the player's hand.

        Returns:
            None
        """
        self.hand.append(card)

    def play_card(self, card):
        """
        Plays a card from the player's hand and adds it to the cards played pile.
        TODO: needs to be refactored to take in an index

        Args:
            card (Card): The card to play.

        Returns:
            Card: The played card.

        Raises:
            ValueError: If the card is not in the player's hand.
        """
        if card in self.hand:
            self.hand.remove(card)
            self.cards_played.append(card)
            return card
        else:
            raise ValueError(f"Card not found in {self.name}'s hand")

    def get_hand(self, list=False):
        """
        Returns a string representation of the player's hand.

        Args:
            list (bool, optional): Whether to return the hand as a list. Defaults to False.

        Returns:
            str or list: The string or list representation of the player's hand.
        """
        if list:
            return [str(card) for card in self.hand]

        return " - ".join(str(card) for card in self.hand)


class Dealer(Player):
    """
    The dealer of the game.
    """

    def __init__(self, game):
        super().__init__(game)
        self.name = "Dealer"
        self.sprite = DealerSprite()
        self.x = self.game.settings.screen_width // 2
        self.y = 125

    def __str__(self):
        return f"Dealer({self.name})"

    def draw(self):
        """
        Draws the dealer's name and hand on the game screen.

        Returns:
            None
        """
        dealer_label = GameText("Dealer")
        player_cards_label = GameText(self.get_hand())

        player_cards_label.draw(self.game.screen, self.x, self.y + 20)
        dealer_label.draw(self.game.screen, self.x, self.y)


class Table(Player):
    """
    The table for the game. Holds all cards that have been played
    """

    def __init__(self, game):
        super().__init__(game)
        self.name = "Table"
        self.graveyard = []
        self.x = self.game.settings.screen_width // 2
        self.y = self.game.settings.screen_height // 2

    def __str__(self):
        return f"Table({self.name})"

    def draw(self):
        """
        Draws the table's name and hand on the game screen.

        Returns:
            None
        """
        table_label = GameText("Table")
        table_cards_label = GameText(self.get_hand())
        table_label.draw(self.game.screen, self.x, self.y)
        table_cards_label.draw(self.game.screen, self.x, self.y + 20)

    def draw_remaining_cards(self, x, y):
        """
        Draw the remaining cards in the deck on the game screen. Because
        cards are pulled from the bottom of the deck using List.pop(), we
        copy and reverse the list to show the "correct" top of the deck.

        Args:
            x (int): The x-coordinate where the remaining cards will be drawn.
            y (int): The y-coordinate where the remaining cards will be drawn.

        Returns:
            None
        """
        remaining_cards = self.game.deck.get_remaining_cards()

        remaining_cards = list(reversed(remaining_cards))

        remaining_deck_total = len(remaining_cards)

        """Splitting the deck for easier viewing"""
        half = remaining_deck_total // 2
        first_half = remaining_cards[:half]
        first_half.insert(0, "Top Of Deck: ")  # helper text
        second_half = remaining_cards[half:]

        remaining_list = []
        for i, cards in enumerate([first_half, second_half]):
            cards_label = GameText(' '.join(cards))
            remaining_list.append(cards_label)

        for i, row in enumerate(remaining_list):
            row.draw(self.game.screen, x, y + (20 * i))
