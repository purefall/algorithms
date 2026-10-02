# Sorting Intervals

Review after attempts.

## Peak Load and Earliest Interval

Aggregate simultaneous events before assessing load between timestamps; merge adjacent equal-peak spans.

O(n log n) time, O(n) space.

## All Peak Load Intervals

Peak spans separated by a lower load remain distinct; touching peak spans merge.

O(n log n) time, O(n) space.

## Bounded Timestamp Peak

A small bounded time domain replaces comparison sorting with a difference array.

O(n+T) time, O(T) space.

## Merge Closed Intervals

Sort by start, then compare only with the current merged interval.

O(n log n) time, O(n) space.

