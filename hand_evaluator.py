from collections import Counter

class HandEvaluator:
    def __init__(self, hole_cards, community_cards):
        self.cards = hole_cards + community_cards
        self.suits = [card[-1] for card in self.cards]  # Extract suits
        self.ranks = sorted([self.card_value(card) for card in self.cards])

    def card_value(self, card):
        # Converts card to numerical value for sorting and ranking 
        value_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
                     '7': 7, '8': 8, '9': 9, 'A': 10}  # Ace high
        return value_map[card[0]]

    def is_flush(self):
        # Checks if all suits match (flush)
        return len(set(self.suits)) == 1

    def is_straight(self):
        # Checks for a straight, including special Ace rules
        sorted_ranks = sorted(set(self.ranks))  # Remove duplicates
        for i in range(len(sorted_ranks) - 4):
            if sorted_ranks[i:i + 5] == list(range(sorted_ranks[i], sorted_ranks[i] + 5)):
                return True
        # Check special A-2-3-4-5 rule
        if set(sorted_ranks) >= {2, 3, 4, 5, 10}:
            return True
        return False

    def evaluate_hand(self):
        # Determines best hand ranking
        counts = Counter(self.ranks)
        sorted_counts = sorted(counts.values(), reverse=True)
        
        if self.is_flush() and self.is_straight():
            return "Straight Flush"
        if sorted_counts == [3, 2]:
            return "Full House"
        if self.is_flush():
            return "Flush"
        if self.is_straight():
            return "Straight"
        if 3 in sorted_counts:
            return "Three of a Kind"
        if sorted_counts == [2, 2, 1]:
            return "Two Pair"
        if 2 in sorted_counts:
            return "One Pair"
        return "High Card"