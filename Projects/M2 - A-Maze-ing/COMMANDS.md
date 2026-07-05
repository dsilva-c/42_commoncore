# A-Maze-ing Commands and How They Are Implemented

This document explains every command the program exposes and where the
behavior is implemented in code. It covers the CLI entry point, the
interactive ASCII menu, and the MLX key bindings.

## 1) Program entry command

**Command**

- `python3 a_maze_ing.py config.txt`

**What it does**

- Loads the config file, generates the maze, solves the shortest path,
  writes the output file, and launches the chosen renderer(s).

**How it is implemented**

- The entry point validates `sys.argv`, then calls `main(config_path)`.
- `main()` runs the pipeline: config parse -> generate -> solve -> write ->
  optional SVG export -> render.
- Parsing is handled by `ConfigParser` in [config_parser.py](config_parser.py).
- Generation uses `MazeGenerator` in [mazegen/generator.py](mazegen/generator.py).
- Solving uses `MazeSolver` in [mazegen/solver.py](mazegen/solver.py).
- Output writing is done by `OutputWriter` in [output_writer.py](output_writer.py).
- SVG export uses `write_svg` in [export_svg.py](export_svg.py).
- Rendering is dispatched to [renderer_ascii.py](renderer_ascii.py) and/or
  [renderer_mlx.py](renderer_mlx.py).
- See [a_maze_ing.py](a_maze_ing.py) for the flow and error handling.

## 2) ASCII renderer menu commands

The ASCII menu is printed on every refresh and reads a numeric choice
from stdin.

**How the menu and commands are created**

- The menu text is printed by `_print_menu()`.
- Input is read by `_get_choice()` and handled by `_interactive_loop()`.
- Each option is an `if/elif` branch that toggles state or regenerates
  the maze, then redraws.
- See [renderer_ascii.py](renderer_ascii.py).

**Commands (menu options 1-19)**

| Menu # | Command | What it does | Implementation notes |
| --- | --- | --- | --- |
| 1 | Re-generate a new maze | Builds a new grid and solution path | `_interactive_loop()` picks a new seed, creates a `MazeGenerator`, calls `generate()`, then `_solve_path_cells()` for the new path. If `ANIMATE=True`, `_animate_solution()` replays the reveal. |
| 2 | Show/Hide path | Toggles showing the solution path | Toggles `show_solution` and the next render uses `_build_display_lines()` with or without solution cells. |
| 3 | Rotate maze wall colours | Cycles the wall/passage palette | Increments `palette_idx`, which changes the palette chosen in `_build_display_lines()`. |
| 4 | Toggle 42 pattern highlight | Shows/hides the "42" pattern overlay | Toggles `show_pattern`, which gates whether `pattern_cells` are painted. |
| 5 | Cycle path animation speed | Cycles speed preset for path animation | Increments `path_speed_idx`, selecting a new value from `ANIMATE_SPEEDS`. |
| 6 | Cycle effects speed | Cycles speed preset for effects | Increments `fx_speed_idx`, which controls animation timing in loops. |
| 7 | Toggle ducks | Turns the duck overlay on/off | Toggles `ducks_enabled`; when disabled, `duck_cells` is cleared. When enabled, `_pick_duck_cells()` chooses new locations. |
| 8 | Toggle duck animation | Ducks move over time | Toggles `ducks_animate`, allowing `_pick_duck_cells()` to run each frame. |
| 9 | Toggle auto palette | Automatically cycles palettes each redraw | Toggles `auto_palette`; when on, `palette_idx` increments each menu step. |
| 10 | Toggle entry/exit pulse | Pulses entry/exit cell colors | Toggles `pulse_entry_exit`, which affects the color computed in `_build_display_lines()`. |
| 11 | Toggle 42 pattern fade | Fades the 42 pattern color | Toggles `pattern_fade`, which drives the fade factor in `_build_display_lines()`. |
| 12 | Toggle dead-end shimmer | Highlights dead ends periodically | Toggles `dead_end_shimmer`; `_is_dead_end()` is used to decide shimmer cells. |
| 13 | Toggle stats ticker | Shows dead-end and path stats | Toggles `stats_ticker`; `_print_stats_line()` computes and prints stats. |
| 14 | Toggle seed slideshow | Auto-regenerates new mazes | Toggles `seed_slideshow`; when on, `_slideshow_loop()` continuously regenerates. |
| 15 | Faster path animation | Decreases path animation delay | Decrements `path_speed_idx` with bounds; animation uses `ANIMATE_SPEEDS`. |
| 16 | Slower path animation | Increases path animation delay | Increments `path_speed_idx` with bounds; animation uses `ANIMATE_SPEEDS`. |
| 17 | Faster effects | Decreases effects delay | Decrements `fx_speed_idx` with bounds; used by slideshow timing. |
| 18 | Slower effects | Increases effects delay | Increments `fx_speed_idx` with bounds; used by slideshow timing. |
| 19 | Quit | Exits the ASCII UI | Breaks the loop, ending `_interactive_loop()`. |

## 3) MLX renderer key commands

The MLX renderer listens for key codes and maps them to actions.

**How the key commands are created**

- Key sets (`KEY_*`) define which key codes trigger each action.
- `_handle_key()` applies the action for the matched key set.
- `render()` registers `_mlx_key_dispatch()` with `mlx_key_hook()` so MLX
  forwards key presses into `_handle_key()`.
- See [renderer_mlx.py](renderer_mlx.py).

**Commands (key bindings)**

| Key | Command | What it does | Implementation notes |
| --- | --- | --- | --- |
| R | Re-generate a new maze | Builds a new grid and solution path | `_handle_key()` calls `_regenerate()`, which re-runs `MazeGenerator.generate()`, recomputes `_path_cells`, and redraws. |
| P | Show/Hide path | Toggles solution path rendering | Toggles `_show_path`, resets animation counters, then `_redraw()` repaints cells. |
| C | Cycle wall colours | Rotates palette and re-randomizes bonus colors | Advances `_palette_idx` and calls `_randomize_bonus_colours()` before `_redraw()`. |
| H | Toggle 42 pattern highlight | Shows/hides the pattern overlay | Toggles `_show_pattern`, then `_redraw()` respects it. |
| S | Cycle path animation speed | Cycles path reveal speed | Changes `_path_speed_idx` and, if the path is visible, restarts animation. |
| E | Cycle effects speed | Cycles effect timing | Changes `_fx_speed_idx` and calls `_update_animation_intervals()`. |
| [ | Slower path animation | Increases path animation delay | Uses `_clamp_speed()` on `_path_speed_idx`. |
| ] | Faster path animation | Decreases path animation delay | Uses `_clamp_speed()` on `_path_speed_idx`. |
| - | Slower effects | Increases effect delays | Uses `_clamp_speed()` on `_fx_speed_idx`, then `_update_animation_intervals()`. |
| = | Faster effects | Decreases effect delays | Uses `_clamp_speed()` on `_fx_speed_idx`, then `_update_animation_intervals()`. |
| D | Toggle ducks | Turns duck overlay on/off | Toggles `_ducks_enabled`, calls `_reset_ducks()`, then `_redraw()`. |
| U | Toggle duck animation | Ducks move over time | Toggles `_ducks_animate`; `_loop_hook()` moves ducks on a timer. |
| A | Toggle auto palette | Auto-cycles palettes | Toggles `_auto_palette`; `_loop_hook()` advances palettes on a timer. |
| O | Toggle entry/exit pulse | Pulses entry/exit colors | Toggles `_pulse_entry_exit`, then `_redraw()` uses `_pulse_factor()`. |
| F | Toggle 42 pattern fade | Fades the 42 pattern color | Toggles `_pattern_fade`, then `_redraw()` uses `_scale_colour()`. |
| M | Toggle dead-end shimmer | Highlights dead ends periodically | Toggles `_dead_end_shimmer`, then `_redraw()` uses `_dead_end_cells`. |
| T | Toggle stats ticker | Prints stats periodically | Toggles `_stats_ticker`; `_loop_hook()` prints stats on interval. |
| L | Toggle seed slideshow | Auto-regenerates new mazes | Toggles `_seed_slideshow`; `_loop_hook()` triggers `_regenerate()` on interval. |
| Q or Esc | Quit | Exits the MLX loop | `_handle_key()` calls `mlx_loop_exit()`. |

## 4) Output validator (debug helper)

**Command**

- `python3 output_validator.py output_maze.txt`

**What it does**

- Verifies that adjacent cells have matching wall bits in the output grid.

**How it is implemented**

- Reads the hex grid until the blank line, then validates the wall-bit
  consistency against neighbors.
- See [output_validator.py](output_validator.py).
