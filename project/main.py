from drawing import *
from game_state import GameState


global main_screen
global main_canvas
global game_state

def main():
    main_screen = create_screen("battleship","500x500")
    main_canvas = create_canvas(main_screen, 420,420, "white")

    game_state = GameState(4,4)
    print(game_state.get_debug("basic"))
    draw_game_state(main_canvas, game_state)

    main_screen.mainloop()
    return 0




main()