# Module 05 - Code Nexus
## Polymorphic Data Streams in the Digital Matrix

### Python Inheritance, Method Overriding & Subtype Polymorphism

---

## Project Overview

This module focuses on Python's object-oriented programming features:
inheritance, abstract base classes, method overriding, and subtype
polymorphism. Through the sci-fi theme of the **Code Nexus** (Neo-Tokyo, 2087),
you will build a series of progressively more complex data-processing pipelines
whose components are interchangeable through shared interfaces.

**Python Version**: 3.10+  
**Focus**: ABC, abstractmethod, Protocol, method overriding, type annotations

---

## Project Structure

```
Python Module 05/
├── ex0/
│   └── stream_processor.py       # Abstract DataProcessor + 3 specialised processors
├── ex1/
│   └── data_stream.py            # Abstract DataStream + 3 stream types + StreamProcessor
├── ex2/
│   └── nexus_pipeline.py         # Full enterprise pipeline with Protocol, ABC, adapters
├── main.py                       # Automated test suite (provided)
├── pyrightconfig.json            # Pyright / Pylance path configuration
├── DEFENSE_GUIDE.md              # Comprehensive defense preparation
├── IMPLEMENTATION_SUMMARY.md     # Implementation notes
├── SUBMISSION_CHECKLIST.md       # Submission checklist
└── en.subject.pdf                # Original project subject
```

---

## Quick Start

```bash
# Run the automated test suite
python3 main.py

# Run individual exercises
python3 ex0/stream_processor.py
python3 ex1/data_stream.py
python3 ex2/nexus_pipeline.py

# Lint check
flake8 ex0/ ex1/ ex2/

# Verbose test output
python3 main.py --verbose
```

---

## Exercise Summary

| Exercise | File | Key Classes | Concepts |
|----------|------|-------------|----------|
| 0 | `ex0/stream_processor.py` | `DataProcessor`, `NumericProcessor`, `TextProcessor`, `LogProcessor` | ABC, abstractmethod, method overriding |
| 1 | `ex1/data_stream.py` | `DataStream`, `SensorStream`, `TransactionStream`, `EventStream`, `StreamProcessor` | Subtype polymorphism, batch processing, filtering |
| 2 | `ex2/nexus_pipeline.py` | `ProcessingPipeline`, `InputStage`, `TransformStage`, `OutputStage`, `JSONAdapter`, `CSVAdapter`, `StreamAdapter`, `NexusManager` | Protocol (duck typing), pipeline chaining, error recovery |

---

## Key Concepts

### Abstract Base Classes (ABC)
Used to define interfaces that subclasses *must* implement:
```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
```

### Method Overriding
Each subclass overrides abstract (and optionally concrete) methods to provide
specialised behaviour while keeping the same signature:
```python
class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        # numeric-specific implementation
        ...
```

### Protocol (Duck Typing)
`ProcessingStage` in ex2 uses `typing.Protocol` — no inheritance needed; any
class with a compatible `process()` method qualifies:
```python
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...
```

### Subtype Polymorphism
Objects of different classes are used interchangeably through a common base
type, e.g. iterating over `List[DataStream]` and calling `process_batch()`.
