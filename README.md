Poker AI Bot-7

├── bot_strategy.py     # AI decision-making logic (betting, raising, folding)

├── game_state.py      # Handles parsing game data and tracking game state

├── hand_evaluator.py  # Evaluates hand strength based on modified rules

├── time_manager.py    # Manages time constraints to prevent forfeiting

├── main.py            # Runs the bot, integrates all modules, and outputs moves

├── README.md          # Project documentation

Installation
1. git clone https://github.com/your-repo/poker-ai-bot.git
   
   cd poker-ai-bot
   
2. pip install -r requirements.txt

5. python main.py

How It Works

1. Game State Handling (game_state.py)
Parses input data from the tournament engine.
Tracks hole cards, community cards, pot, stack sizes, and betting actions.
Implements redraw logic for discarding and drawing a card.

2. Hand Evaluation (hand_evaluator.py)
Converts cards into numerical values.
Checks for flush, straight, full house, etc. with the modified deck.
Implements special Ace rule (high or low in straights).

3. AI Decision Making (bot_strategy.py)
Uses Game Theory Optimal (GTO) strategies.
Adapts to game state and chooses the best action (fold, call, raise, redraw).
Implements preflop and postflop betting strategies.

4. Time Management (time_manager.py)
Ensures the bot does not exceed time constraints.
Optimizes decision-making speed per hand to prevent forfeiting.

5. Running the Bot (main.py)
Reads game input and initializes game state.
Calls the decision-making engine.
Outputs a valid poker action.

Strategy & Future Improvements

1. Opponent Modeling: Adjust play based on opponent tendencies.
2. Monte Carlo Simulations: Estimate winning probabilities.
3. Reinforcement Learning: Train the bot to improve decision-making over time.
4. Improved Bluffing Strategies: Introduce randomness to avoid predictability.
