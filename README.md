# Advent of Code 2025

## Setup

### Install dependencies

    uv sync

### Login to advent of code

    Go to: https://adventofcode.com/ and login with your account

### Get AOC token from browser cache

    mkdir -p ~/.config/aocd
    aocd-token > ~/.config/aocd/token

### Generate all files using the template

    uv run generate

## Usage

### Test solution against the examples

    uv run test [DAY]

### Solve puzzle

    uv run solve [DAY]

### Notes

- This project now uses `uv` instead of Poetry. Use `uv add <pkg>` to add dependencies and `uv add --group dev <pkg>` for dev-only tools.
- Running `uv sync` will create `uv.lock`. 

