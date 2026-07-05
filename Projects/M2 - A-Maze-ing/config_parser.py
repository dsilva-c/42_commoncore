"""Configuration file parser for the A-Maze-ing project.

Reads a plain-text ``KEY=VALUE`` configuration file and exposes the values
as a typed :class:`MazeConfig` dataclass.

File format rules
-----------------
- One ``KEY=VALUE`` pair per line.
- Lines starting with ``#`` (ignoring leading whitespace) are comments.
- Blank lines are ignored.
- Leading and trailing whitespace is stripped from both key and value.

Mandatory keys
--------------
================  ===================  =============================
Key               Type                 Example
================  ===================  =============================
``WIDTH``         int                  ``WIDTH=20``
``HEIGHT``        int                  ``HEIGHT=15``
``ENTRY``         ``x,y``              ``ENTRY=0,0``
``EXIT``          ``x,y``              ``EXIT=19,14``
``OUTPUT_FILE``   str                  ``OUTPUT_FILE=maze.txt``
``PERFECT``       bool (True/False)    ``PERFECT=True``
================  ===================  =============================

Optional keys
-------------
================  ===================  =============================
Key               Type                 Example
================  ===================  =============================
``SEED``          int or ``None``      ``SEED=42``
``ALGORITHM``     str                  ``ALGORITHM=dfs``
``DISPLAY_MODE``  str                  ``DISPLAY_MODE=ascii``
``ANIMATE``       bool                 ``ANIMATE=False``
``PALETTE``       str                  ``PALETTE=default``
``EXPORT_SVG``    str                  ``EXPORT_SVG=maze.svg``
``EXPORT_CELL_SIZE`` int               ``EXPORT_CELL_SIZE=24``
``EXPORT_WALL``   int                  ``EXPORT_WALL=2``
``DUCKS``         bool                 ``DUCKS=True``
``DUCKS_COUNT``   int                  ``DUCKS_COUNT=5``
``DUCKS_ANIMATE`` bool                 ``DUCKS_ANIMATE=False``
``AUTO_PALETTE``  bool                 ``AUTO_PALETTE=True``
``PULSE_ENTRY_EXIT`` bool              ``PULSE_ENTRY_EXIT=True``
``PATTERN_FADE``  bool                 ``PATTERN_FADE=True``
``DEAD_END_SHIMMER`` bool              ``DEAD_END_SHIMMER=True``
``SEED_SLIDESHOW`` bool                ``SEED_SLIDESHOW=True``
``STATS_TICKER``  bool                 ``STATS_TICKER=True``
================  ===================  =============================
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Typed configuration container
# ---------------------------------------------------------------------------

@dataclass
class MazeConfig:
    """Parsed configuration for a maze generation run.

    Attributes:
        width: Number of maze columns.
        height: Number of maze rows.
        entry: Entry cell coordinates as (x, y).
        exit_: Exit cell coordinates as (x, y).
        output_file: Path to write the output hex file.
        perfect: Whether to generate a perfect maze.
        seed: Optional random seed for reproducibility.
        algorithm: Generation algorithm name (default ``"dfs"``).
        display_mode: Visual output mode: ``"ascii"``, ``"mlx"``, or
            ``"both"`` (default ``"ascii"``).
        animate: Whether to animate the generation process.
    """

    width: int
    height: int
    entry: tuple[int, int]
    exit_: tuple[int, int]
    output_file: str
    perfect: bool
    seed: Optional[int] = field(default=None)
    algorithm: str = field(default="dfs")
    display_mode: str = field(default="ascii")
    animate: bool = field(default=False)
    palette: str = field(default="default")
    export_svg: Optional[str] = field(default=None)
    export_cell_size: int = field(default=24)
    export_wall_thickness: int = field(default=2)
    ducks: bool = field(default=False)
    ducks_count: int = field(default=0)
    ducks_animate: bool = field(default=False)
    auto_palette: bool = field(default=False)
    pulse_entry_exit: bool = field(default=False)
    pattern_fade: bool = field(default=False)
    dead_end_shimmer: bool = field(default=False)
    seed_slideshow: bool = field(default=False)
    stats_ticker: bool = field(default=False)


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

class ConfigParser:
    """Parse a ``KEY=VALUE`` configuration file into a :class:`MazeConfig`.

    Example:
        >>> parser = ConfigParser("config.txt")
        >>> cfg = parser.parse()
        >>> print(cfg.width, cfg.height)
        20 15

    Args:
        filepath: Path to the configuration file.
    """

    _MANDATORY_KEYS: frozenset[str] = frozenset(
        {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}
    )

    def __init__(self, filepath: str) -> None:
        self.filepath: str = filepath

    def parse(self) -> MazeConfig:
        """Read and validate the configuration file.

        Returns:
            A fully populated :class:`MazeConfig` instance.

        Raises:
            FileNotFoundError: If the configuration file does not exist.
            ValueError: If any mandatory key is missing, a value is not in the
                expected format, or the coordinates are logically invalid.
        """
        if not os.path.isfile(self.filepath):
            raise FileNotFoundError(
                f"Configuration file not found: '{self.filepath}'"
            )

        raw = self._read_raw(self.filepath)
        self._check_mandatory(raw)
        return self._build_config(raw)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _read_raw(filepath: str) -> dict[str, str]:
        """Read file and return a {KEY: raw_value} dict (no type casting yet).

        Args:
            filepath: Path to the configuration file.

        Returns:
            Dictionary mapping upper-cased keys to their raw string values.

        Raises:
            ValueError: If a non-comment, non-blank line is not a valid
                ``KEY=VALUE`` pair.
        """
        raw: dict[str, str] = {}
        with open(filepath, "r", encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, start=1):
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                if "=" not in stripped:
                    raise ValueError(
                        f"Line {lineno}: invalid format (expected KEY=VALUE):"
                        f" '{stripped}'"
                    )
                key, _, value = stripped.partition("=")
                raw[key.strip().upper()] = value.strip()
        return raw

    def _check_mandatory(self, raw: dict[str, str]) -> None:
        """Raise ValueError if any mandatory key is absent.

        Args:
            raw: Parsed raw key-value pairs.

        Raises:
            ValueError: Listing all missing mandatory keys.
        """
        missing = self._MANDATORY_KEYS - raw.keys()
        if missing:
            raise ValueError(
                f"Missing mandatory configuration keys: "
                f"{', '.join(sorted(missing))}"
            )

    def _build_config(self, raw: dict[str, str]) -> MazeConfig:
        """Cast raw string values to their proper types and construct config.

        Args:
            raw: Parsed raw key-value pairs (all mandatory keys present).

        Returns:
            A :class:`MazeConfig` instance.

        Raises:
            ValueError: If any value cannot be cast to its expected type or
                fails a domain constraint.
        """
        width = self._parse_positive_int("WIDTH", raw["WIDTH"])
        height = self._parse_positive_int("HEIGHT", raw["HEIGHT"])
        entry = self._parse_coord("ENTRY", raw["ENTRY"], width, height)
        exit_ = self._parse_coord("EXIT", raw["EXIT"], width, height)

        if entry == exit_:
            raise ValueError("ENTRY and EXIT coordinates must be different.")

        if not self._is_border_cell(entry, width, height):
            raise ValueError(
                f"ENTRY {entry} must be on the maze border."
            )
        if not self._is_border_cell(exit_, width, height):
            raise ValueError(
                f"EXIT {exit_} must be on the maze border."
            )

        perfect = self._parse_bool("PERFECT", raw["PERFECT"])

        # Optional keys
        seed: Optional[int] = None
        if "SEED" in raw and raw["SEED"].upper() not in ("", "NONE", "NULL"):
            seed = self._parse_int("SEED", raw["SEED"])

        algorithm = raw.get("ALGORITHM", "dfs").lower()
        display_mode = raw.get("DISPLAY_MODE", "ascii").lower()
        if display_mode not in ("ascii", "mlx", "both"):
            raise ValueError(
                f"DISPLAY_MODE must be 'ascii', 'mlx', or 'both', "
                f"got '{display_mode}'."
            )

        animate = False
        if "ANIMATE" in raw:
            animate = self._parse_bool("ANIMATE", raw["ANIMATE"])

        palette = raw.get("PALETTE", "default").lower()
        if palette not in ("default", "colorblind"):
            raise ValueError(
                "PALETTE must be 'default' or 'colorblind', "
                f"got '{palette}'."
            )

        export_svg = None
        if "EXPORT_SVG" in raw and raw["EXPORT_SVG"].strip():
            export_svg = raw["EXPORT_SVG"].strip()

        export_cell_size = 24
        if "EXPORT_CELL_SIZE" in raw:
            export_cell_size = self._parse_positive_int(
                "EXPORT_CELL_SIZE",
                raw["EXPORT_CELL_SIZE"],
            )

        export_wall_thickness = 2
        if "EXPORT_WALL" in raw:
            export_wall_thickness = self._parse_positive_int(
                "EXPORT_WALL",
                raw["EXPORT_WALL"],
            )

        ducks = False
        if "DUCKS" in raw:
            ducks = self._parse_bool("DUCKS", raw["DUCKS"])

        ducks_count = 0
        if "DUCKS_COUNT" in raw:
            ducks_count = self._parse_positive_int(
                "DUCKS_COUNT",
                raw["DUCKS_COUNT"],
            )
        elif ducks:
            ducks_count = 5

        ducks_animate = False
        if "DUCKS_ANIMATE" in raw:
            ducks_animate = self._parse_bool(
                "DUCKS_ANIMATE",
                raw["DUCKS_ANIMATE"],
            )

        auto_palette = False
        if "AUTO_PALETTE" in raw:
            auto_palette = self._parse_bool(
                "AUTO_PALETTE",
                raw["AUTO_PALETTE"],
            )

        pulse_entry_exit = False
        if "PULSE_ENTRY_EXIT" in raw:
            pulse_entry_exit = self._parse_bool(
                "PULSE_ENTRY_EXIT",
                raw["PULSE_ENTRY_EXIT"],
            )

        pattern_fade = False
        if "PATTERN_FADE" in raw:
            pattern_fade = self._parse_bool(
                "PATTERN_FADE",
                raw["PATTERN_FADE"],
            )

        dead_end_shimmer = False
        if "DEAD_END_SHIMMER" in raw:
            dead_end_shimmer = self._parse_bool(
                "DEAD_END_SHIMMER",
                raw["DEAD_END_SHIMMER"],
            )

        seed_slideshow = False
        if "SEED_SLIDESHOW" in raw:
            seed_slideshow = self._parse_bool(
                "SEED_SLIDESHOW",
                raw["SEED_SLIDESHOW"],
            )

        stats_ticker = False
        if "STATS_TICKER" in raw:
            stats_ticker = self._parse_bool(
                "STATS_TICKER",
                raw["STATS_TICKER"],
            )

        return MazeConfig(
            width=width,
            height=height,
            entry=entry,
            exit_=exit_,
            output_file=raw["OUTPUT_FILE"],
            perfect=perfect,
            seed=seed,
            algorithm=algorithm,
            display_mode=display_mode,
            animate=animate,
            palette=palette,
            export_svg=export_svg,
            export_cell_size=export_cell_size,
            export_wall_thickness=export_wall_thickness,
            ducks=ducks,
            ducks_count=ducks_count,
            ducks_animate=ducks_animate,
            auto_palette=auto_palette,
            pulse_entry_exit=pulse_entry_exit,
            pattern_fade=pattern_fade,
            dead_end_shimmer=dead_end_shimmer,
            seed_slideshow=seed_slideshow,
            stats_ticker=stats_ticker,
        )

    # ------------------------------------------------------------------
    # Type-casting helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_int(key: str, value: str) -> int:
        """Parse *value* as an integer.

        Args:
            key: Key name (for error messages).
            value: The raw string value.

        Returns:
            Parsed integer.

        Raises:
            ValueError: If *value* is not a valid integer.
        """
        try:
            return int(value)
        except ValueError:
            raise ValueError(
                f"Key {key}: expected an integer, got '{value}'."
            )

    @staticmethod
    def _parse_positive_int(key: str, value: str) -> int:
        """Parse *value* as a positive integer (>= 1).

        Args:
            key: Key name.
            value: Raw string value.

        Returns:
            Parsed positive integer.

        Raises:
            ValueError: If the value is not a valid positive integer.
        """
        try:
            n = int(value)
        except ValueError:
            raise ValueError(
                f"Key {key}: expected a positive integer, got '{value}'."
            )
        if n < 1:
            raise ValueError(
                f"Key {key}: value must be >= 1, got {n}."
            )
        return n

    @staticmethod
    def _parse_bool(key: str, value: str) -> bool:
        """Parse *value* as a boolean (True/False, case-insensitive).

        Args:
            key: Key name.
            value: Raw string value.

        Returns:
            True or False.

        Raises:
            ValueError: If the value is not a recognised boolean string.
        """
        normalised = value.strip().lower()
        if normalised == "true":
            return True
        if normalised == "false":
            return False
        raise ValueError(
            f"Key {key}: expected True/False, got '{value}'."
        )

    @staticmethod
    def _parse_coord(
        key: str,
        value: str,
        width: int,
        height: int,
    ) -> tuple[int, int]:
        """Parse *value* as an ``x,y`` coordinate pair within grid bounds.

        Args:
            key: Key name.
            value: Raw string value (e.g. ``"0,0"``).
            width: Maze width for bounds-checking.
            height: Maze height for bounds-checking.

        Returns:
            ``(x, y)`` tuple.

        Raises:
            ValueError: If the format is wrong or coordinates are out of
                bounds.
        """
        parts = value.split(",")
        if len(parts) != 2:
            raise ValueError(
                f"Key {key}: expected format 'x,y', got '{value}'."
            )
        try:
            x, y = int(parts[0].strip()), int(parts[1].strip())
        except ValueError:
            raise ValueError(
                f"Key {key}: coordinates must be integers, got '{value}'."
            )
        if not (0 <= x < width and 0 <= y < height):
            raise ValueError(
                f"Key {key}: coordinate ({x},{y}) is outside the "
                f"{width}×{height} grid."
            )
        return (x, y)

    @staticmethod
    def _is_border_cell(
        coord: tuple[int, int],
        width: int,
        height: int,
    ) -> bool:
        """Return True if *coord* lies on the grid border.

        Args:
            coord: (x, y) to check.
            width: Maze width.
            height: Maze height.

        Returns:
            True when the cell is on the outermost row or column.
        """
        x, y = coord
        return x == 0 or x == width - 1 or y == 0 or y == height - 1
