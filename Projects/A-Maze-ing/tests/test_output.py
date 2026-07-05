"""Unit tests for output_writer.py — authored by dsilva-c."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from mazegen.generator import MazeGenerator
from mazegen.solver import MazeSolver
from output_writer import OutputWriter


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

WORKSPACE = Path(__file__).parent.parent


def generate_and_write(tmp_path: Path, seed: int = 1) -> Path:
    """Generate a small maze, solve it, and write output.

    Returns:
        The output file path.
    """
    gen = MazeGenerator(10, 8, seed=seed)
    grid = gen.generate(entry=(0, 0), exit_=(9, 7))

    solver = MazeSolver(grid)
    directions = solver.solve()

    out_path = tmp_path / "maze_output.txt"
    OutputWriter().write(grid, directions, str(out_path))
    return out_path


# ---------------------------------------------------------------------------
# output_validator.py integration
# ---------------------------------------------------------------------------

class TestOutputValidator:

    def test_validator_no_errors(self, tmp_path: Path) -> None:
        """output_validator.py must produce no 'Wrong encoding' output."""
        out_path = generate_and_write(tmp_path)
        validator = WORKSPACE / "output_validator.py"
        result = subprocess.run(
            [sys.executable, str(validator), str(out_path)],
            capture_output=True,
            text=True,
        )
        message = (
            "Validator reported encoding errors:\n"
            f"{result.stdout}"
        )
        assert "Wrong encoding" not in result.stdout, message

    @pytest.mark.parametrize("seed", [0, 7, 42, 100])
    def test_validator_various_seeds(self, tmp_path: Path, seed: int) -> None:
        out_path = generate_and_write(tmp_path, seed=seed)
        validator = WORKSPACE / "output_validator.py"
        result = subprocess.run(
            [sys.executable, str(validator), str(out_path)],
            capture_output=True,
            text=True,
        )
        message = f"Seed {seed}: validator errors:\n{result.stdout}"
        assert "Wrong encoding" not in result.stdout, message


# ---------------------------------------------------------------------------
# File format checks
# ---------------------------------------------------------------------------

class TestFileFormat:

    def test_file_created(self, tmp_path: Path) -> None:
        out_path = generate_and_write(tmp_path)
        assert out_path.exists()

    def test_hex_rows_correct_count(self, tmp_path: Path) -> None:
        out_path = generate_and_write(tmp_path)
        lines = out_path.read_text(encoding="utf-8").splitlines()
        # Hex rows come before the first blank line
        hex_lines: list[str] = []
        for line in lines:
            if line == "":
                break
            hex_lines.append(line)
        assert len(hex_lines) == 8, (
            f"Expected 8 hex rows, got {len(hex_lines)}"
        )

    def test_hex_row_width(self, tmp_path: Path) -> None:
        out_path = generate_and_write(tmp_path)
        lines = out_path.read_text(encoding="utf-8").splitlines()
        for line in lines:
            if line == "":
                break
            assert len(line) == 10, (
                f"Hex row '{line}' is not 10 chars wide"
            )

    def test_blank_separator_line_present(self, tmp_path: Path) -> None:
        out_path = generate_and_write(tmp_path)
        text = out_path.read_text(encoding="utf-8")
        assert "\n\n" in text, "Expected blank separator line in output"

    def test_entry_line_format(self, tmp_path: Path) -> None:
        out_path = generate_and_write(tmp_path)
        lines = out_path.read_text(encoding="utf-8").splitlines()
        # Entry line is the first line after the blank separator
        after_blank = False
        entry_line = None
        for line in lines:
            if after_blank:
                entry_line = line
                break
            if line == "":
                after_blank = True
        assert entry_line is not None
        parts = entry_line.split(",")
        assert len(parts) == 2, (
            f"Entry line '{entry_line}' not in x,y format"
        )
        assert all(p.strip().lstrip("-").isdigit() for p in parts)

    def test_exit_line_format(self, tmp_path: Path) -> None:
        out_path = generate_and_write(tmp_path)
        lines = out_path.read_text(encoding="utf-8").splitlines()
        # Exit line is the second line after the blank separator
        after_blank = False
        post_blank: list[str] = []
        for line in lines:
            if after_blank:
                post_blank.append(line)
            if line == "" and not after_blank:
                after_blank = True
        exit_line = post_blank[1]
        parts = exit_line.split(",")
        assert len(parts) == 2
        assert all(p.strip().lstrip("-").isdigit() for p in parts)

    def test_entry_coordinates_correct(self, tmp_path: Path) -> None:
        out_path = generate_and_write(tmp_path)
        lines = out_path.read_text(encoding="utf-8").splitlines()
        after_blank = False
        post_blank: list[str] = []
        for line in lines:
            if after_blank:
                post_blank.append(line)
            if line == "" and not after_blank:
                after_blank = True
        entry_x, entry_y = (int(v) for v in post_blank[0].split(","))
        assert (entry_x, entry_y) == (0, 0)

    def test_exit_coordinates_correct(self, tmp_path: Path) -> None:
        out_path = generate_and_write(tmp_path)
        lines = out_path.read_text(encoding="utf-8").splitlines()
        after_blank = False
        post_blank: list[str] = []
        for line in lines:
            if after_blank:
                post_blank.append(line)
            if line == "" and not after_blank:
                after_blank = True
        exit_x, exit_y = (int(v) for v in post_blank[1].split(","))
        assert (exit_x, exit_y) == (9, 7)

    def test_path_line_only_nesw(self, tmp_path: Path) -> None:
        out_path = generate_and_write(tmp_path)
        lines = out_path.read_text(encoding="utf-8").splitlines()
        after_blank = False
        post_blank: list[str] = []
        for line in lines:
            if after_blank:
                post_blank.append(line)
            if line == "" and not after_blank:
                after_blank = True
        path_line = post_blank[2]
        assert all(c in "NESW" for c in path_line), (
            f"Path line contains invalid chars: '{path_line}'"
        )

    def test_path_line_non_empty(self, tmp_path: Path) -> None:
        out_path = generate_and_write(tmp_path)
        lines = out_path.read_text(encoding="utf-8").splitlines()
        after_blank = False
        post_blank: list[str] = []
        for line in lines:
            if after_blank:
                post_blank.append(line)
            if line == "" and not after_blank:
                after_blank = True
        path_line = post_blank[2]
        assert len(path_line) > 0

    def test_all_lines_end_with_newline(self, tmp_path: Path) -> None:
        out_path = generate_and_write(tmp_path)
        raw = out_path.read_bytes()
        # Every line should end with \n (not \r\n)
        assert b"\r" not in raw, "Output must use Unix line endings"
        assert raw.endswith(b"\n"), "File must end with a newline"


# ---------------------------------------------------------------------------
# OutputWriter.write() error handling
# ---------------------------------------------------------------------------

class TestOutputWriterErrors:

    def test_invalid_direction_raises(self, tmp_path: Path) -> None:
        gen = MazeGenerator(6, 6, seed=0)
        grid = gen.generate()
        writer = OutputWriter()
        with pytest.raises(ValueError, match="direction"):
            writer.write(grid, ["N", "X", "E"], str(tmp_path / "bad.txt"))

    def test_empty_directions_writes_empty_path(self, tmp_path: Path) -> None:
        gen = MazeGenerator(6, 6, seed=0)
        grid = gen.generate()
        out_path = tmp_path / "empty_path.txt"
        writer = OutputWriter()
        writer.write(grid, [], str(out_path))
        text = out_path.read_text(encoding="utf-8")
        lines = text.splitlines()
        after_blank = False
        post_blank: list[str] = []
        for line in lines:
            if after_blank:
                post_blank.append(line)
            if line == "" and not after_blank:
                after_blank = True
        # Path line exists but is empty
        assert post_blank[2] == ""
