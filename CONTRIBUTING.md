# Contributing to SkyNetics

Thank you for your interest in contributing to the SkyNetics Avalanche Rescue Drone project!

## Development Setup

1. Fork the repo.
2. Clone your fork locally.
3. Run `pip install -r requirements.txt`.
4. Run tests with `pytest tests/`.

## Architecture Guidelines
- Keep hardware interfaces in `drone/` and `sensors/`.
- Keep ML/inference logic in `ai/`.
- Do not mix business logic with hardware drivers.

## Submitting Pull Requests
- Ensure tests pass locally.
- Keep PRs focused on one feature.
- Write a clear description of the problem solved.
