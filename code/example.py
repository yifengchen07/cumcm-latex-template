"""Minimal reproducible example for the appendix and supporting materials."""

from __future__ import annotations
def weighted_objective(values: list[float], weights: list[float]) -> float:
    """Return a weighted Chebyshev objective for normalized criteria."""
    if len(values) != len(weights):
        raise ValueError("values and weights must have the same length")
    if abs(sum(weights) - 1.0) > 1e-9:
        raise ValueError("weights must sum to one")
    return max(value * weight for value, weight in zip(values, weights))
if __name__ == "__main__":
    sample = weighted_objective([0.42, 0.36, 0.51], [0.4, 0.35, 0.25])
    print(sample)
