class GameState:
    def __init__(self, game_data):
        self.parse_game_data(game_data)

    def parse_game_data(self, game_data):
        self.hole_cards = game_data["hole_cards"]
        self.community_cards = game_data.get("community_cards", [])
        self.stack_sizes = game_data["stack_sizes"]
        self.pot = game_data["pot"]
        self.bets = game_data["bets"]
        self.phase = game_data["phase"]
        self.redraw_available = game_data["redraw_available"]
        self.discarded_card = None 

    def discard_card(self, card):
        """ Handles the redraw rule """
        if self.redraw_available:
            self.discarded_card = card
            self.redraw_available = False
        return card  # Must be revealed to the opponent