import random

def roll():
    return random.randint(1, 6)

def get_player_count():
    while True:
        players = input("Enter the number of players (2 - 4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                return players
            else:
                print("Please enter a number between 2 and 4.")
        else:
            print("Invalid input. Please enter a number.")

def player_turn(player_num, total_score):
    print(f"\n🎲 Player {player_num + 1}'s turn begins!")
    print(f"🔢 Current total score: {total_score}")
    current_score = 0

    while True:
        choice = input("Would you like to roll? (y/n): ").strip().lower()
        if choice != 'y':
            print("You chose to hold. Ending turn.")
            break

        value = roll()
        print(f"🎲 You rolled a {value}!")

        if value == 1:
            print("💥 Oops! Rolled a 1. Turn ends with 0 points.")
            current_score = 0
            break
        else:
            current_score += value
            print(f"✅ Current turn score: {current_score}")
            print(f"💾 If you hold now, your total will be: {total_score + current_score}")

    return current_score  # This will be added to total outside this function

def main():
    print("🎯 Welcome to the Dice Game!")
    players = get_player_count()
    max_score = 50
    player_scores = [0 for _ in range(players)]

    while max(player_scores) < max_score:
        for i in range(players):
            print("\n" + "=" * 40)
            print(f"🎮 Player {i + 1}'s turn")
            print("=" * 40)
            turn_score = player_turn(i, player_scores[i])
            player_scores[i] += turn_score
            print(f"🏁 End of turn. Player {i + 1}'s total score: {player_scores[i]}")
            if player_scores[i] >= max_score:
                break

    # Announce winner(s)
    max_final_score = max(player_scores)
    winners = [i + 1 for i, score in enumerate(player_scores) if score == max_final_score]

    print("\n🏆 Game Over!")
    if len(winners) == 1:
        print(f"🎉 Player {winners[0]} wins with {max_final_score} points!")
    else:
        print(f"🤝 It's a tie! Players {', '.join(map(str, winners))} all win with {max_final_score} points!")

if __name__ == "__main__":
    main()
