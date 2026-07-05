#!/usr/bin/env python3
"""
Exercise 0: Data Processor Foundation

Polymorphic data processors using ABC and method overriding.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataProcessor(ABC):
    """Abstract base class defining the common data processing interface."""

    def __init__(self) -> None:
        self.metadata: Dict[str, Optional[str]] = {}

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return a result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string. Can be overridden by subclasses."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor specialised for numeric data (lists of numbers)."""

    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        """Process a list of numeric values and return summary statistics."""
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")
        numbers: List[Union[int, float]] = list(data)
        total = sum(numbers)
        avg = total / len(numbers)
        return (
            f"Processed {len(numbers)} numeric values, "
            f"sum={total}, avg={avg}"
        )

    def validate(self, data: Any) -> bool:
        """Return True if data is a non-empty iterable of numbers."""
        try:
            items = list(data)
            return len(items) > 0 and all(
                isinstance(item, (int, float)) for item in items
            )
        except TypeError:
            return False

    def format_output(self, result: str) -> str:
        """Format numeric processor output."""
        return result


class TextProcessor(DataProcessor):
    """Processor specialised for text (string) data."""

    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        """Process a text string and return character/word summary."""
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")
        text: str = str(data)
        char_count = len(text)
        word_count = len(text.split())
        return f"Processed text: {char_count} characters, {word_count} words"

    def validate(self, data: Any) -> bool:
        """Return True if data is a non-empty string."""
        return isinstance(data, str) and len(data) > 0

    def format_output(self, result: str) -> str:
        """Format text processor output."""
        return result


class LogProcessor(DataProcessor):
    """Processor specialised for log-entry strings."""

    _LEVELS: List[str] = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        """Parse a log entry and return an alert-style summary."""
        if not self.validate(data):
            raise ValueError("Invalid data for LogProcessor")
        text: str = str(data)
        level = "INFO"
        message = text
        for lvl in self._LEVELS:
            if text.upper().startswith(f"{lvl}:"):
                level = lvl
                message = text[len(lvl) + 1:].strip()
                break
        label = "ALERT" if level in ("ERROR", "CRITICAL") else level
        return f"[{label}] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        """Return True if data is a non-empty string."""
        return isinstance(data, str) and len(data) > 0

    def format_output(self, result: str) -> str:
        """Format log processor output."""
        return result


def main() -> None:
    """Demonstrate polymorphic data processing."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    numeric_proc = NumericProcessor()
    print("Initializing Numeric Processor...")
    data_n = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_n}")
    ok_n = numeric_proc.validate(data_n)
    valid_n = "Numeric data verified" if ok_n else "Invalid"
    print(f"Validation: {valid_n}")
    result_n = numeric_proc.process(data_n)
    print(f"{numeric_proc.format_output(result_n)}\n")

    text_proc = TextProcessor()
    print("Initializing Text Processor...")
    data_t = "Hello Nexus World"
    print(f'Processing data: "{data_t}"')
    ok_t = text_proc.validate(data_t)
    valid_t = "Text data verified" if ok_t else "Invalid"
    print(f"Validation: {valid_t}")
    result_t = text_proc.process(data_t)
    print(f"{text_proc.format_output(result_t)}\n")

    log_proc = LogProcessor()
    print("Initializing Log Processor...")
    data_l = "ERROR: Connection timeout"
    print(f'Processing data: "{data_l}"')
    ok_l = log_proc.validate(data_l)
    valid_l = "Log entry verified" if ok_l else "Invalid"
    print(f"Validation: {valid_l}")
    result_l = log_proc.process(data_l)
    print(f"{log_proc.format_output(result_l)}\n")

    print("=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    datasets: List[Any] = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready",
    ]

    for idx, (proc, data) in enumerate(zip(processors, datasets), start=1):
        result = proc.process(data)
        print(f"Result {idx}: {proc.format_output(result)}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
