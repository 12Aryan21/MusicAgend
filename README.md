# MusicAgend
Music Recommendation 
# Simple Reflex Music Agent

## Project Title
Simple Reflex Music Agent

## Overview
A lightweight command-line AI music agent that recommends songs based on a user's expressed mood or activity using a rule-based (simple reflex) approach.

## Features
- Detects mood/activity keywords from user input.
- Recommends a song from a small knowledge base.
- Modular Python implementation with unit tests.
- Easy to extend knowledge base and vocab.

## Technologies / Tools
- Python 3.8+
- Standard library only (no external dependencies)
- Optional: run unit tests with `pytest`

## How to run
1. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```

2. Run the agent:
   ```bash
   python main.py
   ```

3. To run tests (if `pytest` is installed):
   ```bash
   pytest
   ```

## Project Structure
```
VITyarthi_MusicAgent/
├─ main.py
├─ agent.py
├─ knowledge.py
├─ vocab.py
├─ utils.py
├─ tests/
│  └─ test_agent.py
├─ README.md
├─ statement.md
├─ report.pdf
└─ requirements.txt
```
