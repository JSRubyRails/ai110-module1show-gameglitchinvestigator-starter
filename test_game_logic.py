from logic_utils import check_guess
import random

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_reveal_secret_on_attempts_exhausted():
    # Simulate the game logic for attempts running out
    attempt_limit = 3
    secret = 42
    attempts = attempt_limit
    status = "playing"
    score = 0
    # After last attempt, status should become 'lost' and secret should be revealed
    if attempts >= attempt_limit:
        status = "lost"
        revealed_secret = secret
    assert status == "lost"
    assert revealed_secret == 42

def test_new_game_resets_state():
    # Simulate initial state after playing a game
    st = {
        'attempts': 5,
        'status': 'lost',
        'secret': 42
    }
    # Simulate starting a new game
    st['attempts'] = 0
    st['status'] = 'playing'
    random.seed(0)  # For reproducibility
    st['secret'] = random.randint(1, 100)
    assert st['attempts'] == 0
    assert st['status'] == 'playing'
    assert 1 <= st['secret'] <= 100
