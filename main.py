from Game import Game

def ask_yes_no(prompt):
    """Fragt den Benutzer und akzeptiert nur y/yes/n/no."""
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in ["y", "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False
        print("Please enter 'y' or 'n'.")

def main():
    print("You are now playing the Dungeon Game \n")
    
    while True:
        game = Game()
        game.start()
        game.run_game()
        
        print("\n" + "="*30)
        if not ask_yes_no("Wanna play again?"):
            print("Thanks for playing the Dungeon Game. Goodbye!")
            break

if __name__ == "__main__":
    main()