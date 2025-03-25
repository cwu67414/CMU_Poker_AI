import random
from hand_evaluator import HandEvaluator

class PokerBot:
    def __init__(self):
        self.aggressiveness = 0.5  # Adjustable for bluffing

    def decide_action(self, game_state):
        # Chooses the best action based on hand strength and game situation
        hand_strength = HandEvaluator(game_state.hole_cards, game_state.community_cards).evaluate_hand()

        if game_state.phase == "Preflop":
            return self.preflop_strategy(game_state)

        if hand_strength in ["Straight Flush", "Full House"]:
            return "raise 2x pot"
        elif hand_strength in ["Flush", "Straight"]:
            return "bet half pot"
        elif hand_strength == "Three of a Kind":
            return "call" if random.random() > self.aggressiveness else "raise"
        elif hand_strength == "One Pair":
            return "check" if game_state.phase == "Flop" else "fold"
        return "fold"

    def preflop_strategy(self, game_state):
        # Simple preflop hand strength-based strategy
        strong_hands = ["A", "9", "8", "7"]
        if any(card[0] in strong_hands for card in game_state.hole_cards):
            return "raise"
        return "call"

    def discard_decision(self, game_state):
        # Decides if and which card to discard
        if game_state.redraw_available:
            return game_state.hole_cards[0]  # Discard weakest hole card
        return None