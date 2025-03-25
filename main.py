import json
from game_state import GameState
from bot_strategy import PokerBot
from time_manager import TimeManager

if __name__ == "__main__":
    game_data = json.loads(input())  # Reads game data from tournament system
    game_state = GameState(game_data)
    
    bot = PokerBot()
    time_manager = TimeManager(time_limit=1500)  # Adjust per phase

    if time_manager.is_time_expired():
        print("fold")  # Avoid losing match due to time out
    else:
        action = bot.decide_action(game_state)
        print(action)