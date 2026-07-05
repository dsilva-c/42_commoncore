#!/usr/bin/env python3
"""
Exercise 1: Polymorphic Streams

Advanced polymorphic streaming system using ABC, method overriding,
isinstance(), list comprehensions, and try/except.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    """Abstract base class for all data streams."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self._batch_count: int = 0
        self._total_items: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a summary string."""
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter data based on an optional criteria string."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return generic stream statistics."""
        return {
            "stream_id": self.stream_id,
            "batches_processed": self._batch_count,
            "total_items": self._total_items,
        }


class SensorStream(DataStream):
    """Stream handler for environmental sensor readings."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self._stream_type: str = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor readings and return temperature analysis."""
        try:
            numeric_readings: List[float] = [
                float(item) for item in data_batch
                if isinstance(item, (int, float))
            ]
            count = len(data_batch)
            self._batch_count += 1
            self._total_items += count
            if numeric_readings:
                avg_temp = sum(numeric_readings) / len(numeric_readings)
                return (
                    f"Sensor analysis: {count} readings processed, "
                    f"avg temp: {avg_temp:.1f}°C"
                )
            return f"Sensor analysis: {count} readings processed"
        except Exception as e:
            return f"Sensor stream error: {str(e)}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter sensor data; 'critical' keeps only readings above 30."""
        if criteria == "critical":
            return [
                item for item in data_batch
                if isinstance(item, (int, float)) and float(item) > 30
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return sensor-specific statistics."""
        stats = super().get_stats()
        stats["stream_type"] = self._stream_type
        return stats


class TransactionStream(DataStream):
    """Stream handler for financial transaction data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self._stream_type: str = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transactions and return net-flow analysis."""
        try:
            count = len(data_batch)
            self._batch_count += 1
            self._total_items += count
            buys = [
                item for item in data_batch
                if isinstance(item, str) and item.startswith("buy:")
            ]
            sells = [
                item for item in data_batch
                if isinstance(item, str) and item.startswith("sell:")
            ]
            buy_total = sum(
                int(b.split(":")[1])
                for b in buys
                if b.split(":")[1].isdigit()
            )
            sell_total = sum(
                int(s.split(":")[1])
                for s in sells
                if s.split(":")[1].isdigit()
            )
            net = sell_total - buy_total
            sign = "+" if net >= 0 else ""
            return (
                f"Transaction analysis: {count} operations, "
                f"net flow: {sign}{net} units"
            )
        except Exception as e:
            return f"Transaction stream error: {str(e)}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter transactions; 'large' keeps only amounts > 100."""
        if criteria == "large":
            result: List[Any] = []
            for item in data_batch:
                if isinstance(item, str) and ":" in item:
                    parts = item.split(":")
                    if len(parts) == 2 and parts[1].isdigit():
                        if int(parts[1]) > 100:
                            result.append(item)
            return result
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return transaction-specific statistics."""
        stats = super().get_stats()
        stats["stream_type"] = self._stream_type
        return stats


class EventStream(DataStream):
    """Stream handler for system event data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self._stream_type: str = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process events and report error count."""
        try:
            count = len(data_batch)
            self._batch_count += 1
            self._total_items += count
            error_count = sum(
                1 for item in data_batch
                if isinstance(item, str) and "error" in item.lower()
            )
            return (
                f"Event analysis: {count} events, "
                f"{error_count} error detected"
            )
        except Exception as e:
            return f"Event stream error: {str(e)}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        """Filter events; 'error' keeps only error events."""
        if criteria == "error":
            return [
                item for item in data_batch
                if isinstance(item, str) and "error" in item.lower()
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return event-specific statistics."""
        stats = super().get_stats()
        stats["stream_type"] = self._stream_type
        return stats


class StreamProcessor:
    """Unified polymorphic orchestrator for multiple stream types."""

    def __init__(self) -> None:
        self._streams: List[DataStream] = []

    def register_stream(self, stream: DataStream) -> None:
        """Register a stream for processing."""
        self._streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> List[str]:
        """Process batches through all registered streams."""
        results: List[str] = []
        for stream, batch in zip(self._streams, batches):
            try:
                result = stream.process_batch(batch)
                results.append(result)
            except Exception as e:
                results.append(f"Error in {stream.stream_id}: {str(e)}")
        return results

    def get_all_stats(self) -> List[Dict[str, Union[str, int, float]]]:
        """Retrieve statistics from all registered streams."""
        return [stream.get_stats() for stream in self._streams]


def main() -> None:
    """Demonstrate the polymorphic stream system."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    sensor_batch = [22.5, 65.0, 1013.0]
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(f"{sensor.process_batch(sensor_batch)}\n")

    transaction = TransactionStream("TRANS_001")
    print("Initializing Transaction Stream...")
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")
    trans_batch = ["buy:100", "sell:150", "buy:75"]
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(f"{transaction.process_batch(trans_batch)}\n")

    event = EventStream("EVENT_001")
    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    event_batch = ["login", "error", "logout"]
    print("Processing event batch: [login, error, logout]")
    print(f"{event.process_batch(event_batch)}\n")

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()
    processor.register_stream(SensorStream("SENSOR_002"))
    processor.register_stream(TransactionStream("TRANS_002"))
    processor.register_stream(EventStream("EVENT_002"))

    mixed_batches: List[List[Any]] = [
        [18.5, 22.0],
        ["buy:300", "sell:50", "buy:200", "sell:75"],
        ["startup", "warning", "shutdown"],
    ]

    results = processor.process_all(mixed_batches)
    labels = ["Sensor data", "Transaction data", "Event data"]
    print("Batch 1 Results:")
    for label, result in zip(labels, results):
        print(f"- {label}: {result.split(':', 1)[-1].strip()}")

    print()
    sensor2 = SensorStream("SENSOR_003")
    critical_data: List[Any] = [15.0, 35.5, 42.0, 28.0, 38.5]
    filtered = sensor2.filter_data(critical_data, criteria="critical")
    print("Stream filtering active: High-priority data only")
    trans2 = TransactionStream("TRANS_003")
    large_trans: List[Any] = ["buy:50", "sell:200", "buy:30", "sell:500"]
    large_filtered = trans2.filter_data(large_trans, criteria="large")
    print(
        f"Filtered results: {len(filtered)} critical sensor alerts, "
        f"{len(large_filtered)} large transaction"
    )

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
