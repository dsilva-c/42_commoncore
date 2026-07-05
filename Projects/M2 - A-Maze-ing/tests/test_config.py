"""Unit tests for config_parser.py — authored by dsilva-c."""

from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

from config_parser import ConfigParser, MazeConfig


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def write_config(tmp_path: Path, content: str) -> str:
    """Write *content* to a temp config file and return its path."""
    p = tmp_path / "config.txt"
    p.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")
    return str(p)


VALID_CONTENT = """\
    WIDTH=10
    HEIGHT=8
    ENTRY=0,0
    EXIT=9,7
    OUTPUT_FILE=maze.txt
    PERFECT=True
"""


# ---------------------------------------------------------------------------
# Parsing a valid config
# ---------------------------------------------------------------------------

class TestValidConfig:

    def test_mandatory_fields_parsed(self, tmp_path: Path) -> None:
        cfg = ConfigParser(write_config(tmp_path, VALID_CONTENT)).parse()
        assert isinstance(cfg, MazeConfig)
        assert cfg.width == 10
        assert cfg.height == 8
        assert cfg.entry == (0, 0)
        assert cfg.exit_ == (9, 7)
        assert cfg.output_file == "maze.txt"
        assert cfg.perfect is True

    def test_optional_defaults(self, tmp_path: Path) -> None:
        cfg = ConfigParser(write_config(tmp_path, VALID_CONTENT)).parse()
        assert cfg.seed is None
        assert cfg.algorithm == "dfs"
        assert cfg.display_mode == "ascii"
        assert cfg.animate is False

    def test_optional_seed_present(self, tmp_path: Path) -> None:
        content = VALID_CONTENT + "SEED=42\n"
        cfg = ConfigParser(write_config(tmp_path, content)).parse()
        assert cfg.seed == 42

    def test_optional_algorithm_present(self, tmp_path: Path) -> None:
        content = VALID_CONTENT + "ALGORITHM=dfs\n"
        cfg = ConfigParser(write_config(tmp_path, content)).parse()
        assert cfg.algorithm == "dfs"

    def test_optional_display_mode_mlx(self, tmp_path: Path) -> None:
        content = VALID_CONTENT + "DISPLAY_MODE=mlx\n"
        cfg = ConfigParser(write_config(tmp_path, content)).parse()
        assert cfg.display_mode == "mlx"

    def test_optional_display_mode_both(self, tmp_path: Path) -> None:
        content = VALID_CONTENT + "DISPLAY_MODE=both\n"
        cfg = ConfigParser(write_config(tmp_path, content)).parse()
        assert cfg.display_mode == "both"

    def test_optional_animate_true(self, tmp_path: Path) -> None:
        content = VALID_CONTENT + "ANIMATE=True\n"
        cfg = ConfigParser(write_config(tmp_path, content)).parse()
        assert cfg.animate is True

    def test_perfect_false(self, tmp_path: Path) -> None:
        content = VALID_CONTENT.replace("PERFECT=True", "PERFECT=False")
        cfg = ConfigParser(write_config(tmp_path, content)).parse()
        assert cfg.perfect is False

    def test_comments_and_blank_lines_ignored(self, tmp_path: Path) -> None:
        content = """\
            # This is a comment
            WIDTH=5
            # another comment

            HEIGHT=5
            ENTRY=0,0
            EXIT=4,4
            OUTPUT_FILE=out.txt
            PERFECT=True
        """
        cfg = ConfigParser(write_config(tmp_path, content)).parse()
        assert cfg.width == 5
        assert cfg.height == 5

    def test_seed_none_string(self, tmp_path: Path) -> None:
        content = VALID_CONTENT + "SEED=None\n"
        cfg = ConfigParser(write_config(tmp_path, content)).parse()
        assert cfg.seed is None


# ---------------------------------------------------------------------------
# File not found
# ---------------------------------------------------------------------------

class TestFileNotFound:

    def test_missing_file_raises(self, tmp_path: Path) -> None:
        with pytest.raises(FileNotFoundError):
            ConfigParser(str(tmp_path / "nonexistent.txt")).parse()


# ---------------------------------------------------------------------------
# Missing mandatory keys
# ---------------------------------------------------------------------------

class TestMissingMandatoryKeys:

    @pytest.mark.parametrize("key_to_drop", [
        "WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT",
    ])
    def test_missing_key_raises_value_error(
        self, tmp_path: Path, key_to_drop: str
    ) -> None:
        lines = [
            ln for ln in textwrap.dedent(VALID_CONTENT).strip().splitlines()
            if not ln.startswith(key_to_drop)
        ]
        content = "\n".join(lines)
        with pytest.raises(ValueError, match=key_to_drop):
            ConfigParser(write_config(tmp_path, content)).parse()


# ---------------------------------------------------------------------------
# Invalid value formats
# ---------------------------------------------------------------------------

class TestInvalidValues:

    def test_width_not_integer(self, tmp_path: Path) -> None:
        content = VALID_CONTENT.replace("WIDTH=10", "WIDTH=abc")
        with pytest.raises(ValueError, match="WIDTH"):
            ConfigParser(write_config(tmp_path, content)).parse()

    def test_height_zero(self, tmp_path: Path) -> None:
        content = VALID_CONTENT.replace("HEIGHT=8", "HEIGHT=0")
        with pytest.raises(ValueError, match="HEIGHT"):
            ConfigParser(write_config(tmp_path, content)).parse()

    def test_width_negative(self, tmp_path: Path) -> None:
        content = VALID_CONTENT.replace("WIDTH=10", "WIDTH=-5")
        with pytest.raises(ValueError, match="WIDTH"):
            ConfigParser(write_config(tmp_path, content)).parse()

    def test_perfect_invalid_bool(self, tmp_path: Path) -> None:
        content = VALID_CONTENT.replace("PERFECT=True", "PERFECT=maybe")
        with pytest.raises(ValueError, match="PERFECT"):
            ConfigParser(write_config(tmp_path, content)).parse()

    def test_entry_bad_format(self, tmp_path: Path) -> None:
        content = VALID_CONTENT.replace("ENTRY=0,0", "ENTRY=0")
        with pytest.raises(ValueError, match="ENTRY"):
            ConfigParser(write_config(tmp_path, content)).parse()

    def test_entry_out_of_bounds(self, tmp_path: Path) -> None:
        # (99,0) is outside a 10×8 grid
        content = VALID_CONTENT.replace("ENTRY=0,0", "ENTRY=99,0")
        with pytest.raises(ValueError):
            ConfigParser(write_config(tmp_path, content)).parse()

    def test_exit_out_of_bounds(self, tmp_path: Path) -> None:
        content = VALID_CONTENT.replace("EXIT=9,7", "EXIT=9,99")
        with pytest.raises(ValueError):
            ConfigParser(write_config(tmp_path, content)).parse()

    def test_entry_equals_exit_raises(self, tmp_path: Path) -> None:
        content = VALID_CONTENT.replace("EXIT=9,7", "EXIT=0,0")
        with pytest.raises(ValueError, match="different"):
            ConfigParser(write_config(tmp_path, content)).parse()

    def test_entry_not_on_border(self, tmp_path: Path) -> None:
        # (3,3) is interior in a 10×8 grid
        content = VALID_CONTENT.replace("ENTRY=0,0", "ENTRY=3,3")
        with pytest.raises(ValueError, match="border"):
            ConfigParser(write_config(tmp_path, content)).parse()

    def test_exit_not_on_border(self, tmp_path: Path) -> None:
        # (5,5) is interior in a 10×8 grid
        content = VALID_CONTENT.replace("EXIT=9,7", "EXIT=5,5")
        with pytest.raises(ValueError, match="border"):
            ConfigParser(write_config(tmp_path, content)).parse()

    def test_display_mode_invalid(self, tmp_path: Path) -> None:
        content = VALID_CONTENT + "DISPLAY_MODE=vga\n"
        with pytest.raises(ValueError, match="DISPLAY_MODE"):
            ConfigParser(write_config(tmp_path, content)).parse()

    def test_invalid_key_value_line(self, tmp_path: Path) -> None:
        content = VALID_CONTENT + "BADLINE\n"
        with pytest.raises(ValueError):
            ConfigParser(write_config(tmp_path, content)).parse()
