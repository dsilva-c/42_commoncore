# Module 05 - Code Nexus
## Polymorphic Data Streams in the Digital Matrix

### Python Inheritance, Method Overriding & Subtype Polymorphism

---

## 📋 Overview

This module focuses on Python's object-oriented programming features:
inheritance, abstract base classes, method overriding, and subtype
polymorphism. Through the sci-fi theme of the **Code Nexus** (Neo-Tokyo, 2087),
the module builds a series of progressively more complex data-processing
pipelines whose components are interchangeable through shared interfaces.

**Python Version**: 3.10+
**Focus**: ABC, abstractmethod, Protocol, method overriding, type annotations

---

## 🎯 Learning Objectives

After completing this module you should understand:

- How `abc.ABC` and `@abstractmethod` enforce an interface contract that
  subclasses *must* implement, and how attempting to instantiate an abstract
  class directly raises `TypeError`.
- How method overriding lets a subclass replace or extend a parent's
  behaviour while keeping the same call signature, and how Python resolves
  the call to the most-derived implementation at runtime (dynamic dispatch).
- How `super()` supports cooperative inheritance — delegating to a parent's
  `__init__`/method instead of duplicating its logic.
- How subtype polymorphism lets code written against a base type
  (`DataProcessor`, `DataStream`, `ProcessingPipeline`) work unmodified with
  any concrete subtype.
- How `typing.Protocol` provides structural subtyping ("duck typing"): a
  class satisfies a Protocol simply by exposing the right method signature,
  with no inheritance relationship required.
- The difference between explicit (ABC) and structural (Protocol) interfaces,
  and when each is the more appropriate tool.

---

## 📁 Project Structure

```
Python Module 05/
├── ex0/
│   └── stream_processor.py       # Abstract DataProcessor + 3 specialised processors
├── ex1/
│   └── data_stream.py            # Abstract DataStream + 3 stream types + StreamProcessor
├── ex2/
│   └── nexus_pipeline.py         # Full enterprise pipeline with Protocol, ABC, adapters
├── main.py                       # Automated test suite (provided)
├── main.tar.gz                   # Archived reference/delivery bundle
├── pyrightconfig.json            # Pyright / Pylance path configuration
└── en.subject.pdf                # Original project subject
```

---

## 🚀 Usage

```bash
# Run the automated test suite
python3 main.py

# Verbose test output
python3 main.py --verbose

# Run individual exercises
python3 ex0/stream_processor.py
python3 ex1/data_stream.py
python3 ex2/nexus_pipeline.py

# Lint check
flake8 ex0/ ex1/ ex2/
```

---

## 📚 Exercises

### Exercise 0 — Data Processor Foundation
`ex0/stream_processor.py`

Build an abstract `DataProcessor` interface and three concrete processors that
each interpret raw input differently.

- `DataProcessor(ABC)` declares `process()` and `validate()` as
  `@abstractmethod`, and provides a concrete default `format_output()`
  (`"Output: ..."`) that subclasses may override.
- The base `__init__()` sets up shared `metadata`; every subclass calls
  `super().__init__()`.
- `NumericProcessor` validates a non-empty iterable of numbers
  (`isinstance(item, (int, float))`) and reports sum/average.
- `TextProcessor` validates a non-empty string and reports character/word
  counts.
- `LogProcessor` parses `"LEVEL: message"` entries and labels the result
  `[ALERT]` for `ERROR`/`CRITICAL`, otherwise `[<LEVEL>]`.
- `main()` demonstrates each processor individually, then loops over a
  `List[DataProcessor]` calling `process()` polymorphically regardless of
  concrete type.

### Exercise 1 — Polymorphic Streams
`ex1/data_stream.py`

Extend the pattern to stateful streams that track their own batch/item
counters and support pluggable filtering.

- `DataStream(ABC)` stores `stream_id`, `_batch_count`, `_total_items`;
  declares `process_batch()` abstract; provides concrete `filter_data()`
  (default substring search) and `get_stats()`.
- `SensorStream` averages numeric temperature readings; its `filter_data()`
  overrides the `"critical"` criteria to keep only readings `> 30`, falling
  back to `super().filter_data()` for any other criteria string.
- `TransactionStream` parses `"buy:N"` / `"sell:N"` tokens into a net-flow
  figure; its `"large"` filter keeps amounts `> 100`.
- `EventStream` counts entries containing `"error"` and can filter down to
  just those entries.
- `StreamProcessor` holds a list of `DataStream` objects and drives them
  polymorphically through `process_all()` / `get_all_stats()`, without ever
  checking which concrete stream type it's holding.

### Exercise 2 — Nexus Integration
`ex2/nexus_pipeline.py`

Combine ABC-based pipelines with a `Protocol`-based stage interface into a
multi-format processing system with chaining and error recovery.

- `ProcessingStage(Protocol)` defines a structural interface — any object
  with a matching `process(data) -> Any` method qualifies, with no
  inheritance declared.
- `InputStage`, `TransformStage`, `OutputStage` implement that Protocol
  purely through duck typing (plain classes, no base class, no constructor
  arguments).
- `ProcessingPipeline(ABC)` stores `pipeline_id` and an ordered
  `List[ProcessingStage]`; declares `process()` abstract; provides concrete
  `add_stage()` and `get_stats()` (including elapsed time).
- `JSONAdapter`, `CSVAdapter`, `StreamAdapter` each inherit from
  `ProcessingPipeline`, take `pipeline_id` as their sole constructor
  argument, and wire the same three stages, but process input differently
  (JSON parsing, CSV row counting, running numeric average respectively).
- `NexusManager` registers pipelines by ID and offers `process()` (route to
  one pipeline), `chain_pipelines()` (feed one pipeline's output into the
  next), `get_all_stats()`, and `simulate_recovery()` (deliberately raises
  and catches a `ValueError` to demonstrate error handling).
- `NexusManager._performance` uses `collections.defaultdict(dict)` so a new
  pipeline's metrics dict is created on first access instead of raising
  `KeyError`.

---

## 🧠 Key Concepts

### Abstract Base Classes (ABC)
Used to define interfaces that subclasses *must* implement:
```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
```
Instantiating `DataProcessor()` directly raises `TypeError` — the contract is
enforced at class-definition time, not by convention.

### Method Overriding
Each subclass overrides abstract (and optionally concrete) methods to provide
specialised behaviour while keeping the same signature:
```python
class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        # numeric-specific implementation
        ...
```
Python resolves the call to the most-derived version at runtime (dynamic
dispatch); the same pattern shows up in `SensorStream.filter_data()`, which
calls `super().filter_data()` to reuse the base implementation for criteria
it doesn't specifically handle.

### Protocol (Duck Typing)
`ProcessingStage` in ex2 uses `typing.Protocol` — no inheritance needed; any
class with a compatible `process()` method qualifies:
```python
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...
```

### Subtype Polymorphism
Objects of different classes are used interchangeably through a common base
type, e.g. iterating over `List[DataStream]` and calling `process_batch()`,
or `List[DataProcessor]` and calling `process()` — the caller never needs to
know the concrete class.

---

## 🧪 Testing

Correctness is verified with the provided automated suite rather than manual
inspection:

```bash
python3 main.py            # run all tests; a non-zero summary of failures
                            # signals a problem, all-pass means the module is done
python3 main.py --verbose   # per-test detail when a failure needs investigating
```

Each exercise file is also runnable standalone (`python3 ex0/stream_processor.py`,
etc.) and prints a themed demo of its classes being exercised polymorphically,
which is a quick manual sanity check beyond the automated suite.

---

## ✅ Code Style & Requirements

- **Python 3.10+** syntax throughout.
- Full type annotations on every function/method parameter and return value
  (`from typing import Any, Dict, List, Optional, Protocol, Union`).
- `flake8 ex0/ ex1/ ex2/` must pass with zero warnings (79-character line
  limit, so long expressions are wrapped or split).
- Standard library only — `abc`, `typing`, `json`, `time`, `collections`; no
  third-party dependencies.

---

## 🛡️ Defense Notes

- **Why ABC instead of just raising `NotImplementedError` in a plain
  class?** `ABC` + `@abstractmethod` prevents instantiation of the abstract
  class itself and fails at class-definition time, not at first call — the
  contract is explicit and unbypassable, whereas `NotImplementedError` only
  fails if and when the missing method actually gets invoked.
- **Why is `format_output()` concrete but `process()`/`validate()` abstract
  (ex0)?** Only the methods where every subclass genuinely needs its own
  logic are marked abstract; `format_output()` has a sensible default that
  most subclasses are happy to inherit, and being non-abstract still allows
  selective overriding (as `NumericProcessor` etc. do).
- **`isinstance(item, (int, float))` vs. `type(item) == int`:** `isinstance`
  respects the class hierarchy (e.g. `bool` is technically a subclass of
  `int`), so it's the correct tool for validating "numeric-ish" input; `type()`
  equality checks the exact type only and silently rejects legitimate
  subclasses.
- **ABC vs. Protocol — when to use which:** `ABC` is for a family of related
  classes that share state/behaviour and should be forced into an explicit
  `is-a` relationship (`DataProcessor`, `DataStream`, `ProcessingPipeline`).
  `Protocol` is for a capability check that shouldn't require inheritance —
  ex2's `InputStage`/`TransformStage`/`OutputStage` only need a `process()`
  method, so tying them to a common base class would add coupling for no
  benefit. Protocol membership is structural: any object with the right
  method signature qualifies, checked (optionally) via
  `isinstance(obj, MyProtocol)` at runtime if `@runtime_checkable` is used,
  or simply by static type checkers otherwise.
- **Common mistake — forgetting `super().__init__()`:** subclasses that skip
  the base-class constructor silently lose shared state (e.g. `metadata` in
  ex0, `stream_id`/counters in ex1, `pipeline_id`/`_stages` in ex2), which
  then surfaces as confusing `AttributeError`s deep inside inherited methods
  rather than at the point of the mistake.
- **Common mistake — overriding a method with a different signature:**
  Python does not enforce signature compatibility between parent and child;
  a subclass method with extra required parameters or an incompatible
  return type will still "work" until something calls it polymorphically
  through the base type and breaks. Keeping the same signature is what makes
  the polymorphic call sites (`processor.process(data)`,
  `stream.process_batch(batch)`) safe.
- **Error handling as part of the interface, not an afterthought:** in ex2,
  every adapter's `process()` wraps its work in `try/except` and returns a
  descriptive error string instead of propagating the exception, and
  `NexusManager.simulate_recovery()` deliberately raises and catches a
  `ValueError` to model a recoverable failure — the exercise treats
  "processing failed gracefully" as part of the expected contract, not a bug.

---

## 📝 License

* **Curriculum:** [42 Porto](https://www.42network.org/campus/42-porto/)

> *This project is part of the 42 Student Network curriculum.*
