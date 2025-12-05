# Advent of Code 2025

## Setup

### Install dependencies

    uv sync

### Login to advent of code

    Go to: https://adventofcode.com/ and login with your account

### Get AOC token from browser cache

1) Open Chrome DevTools > Application > Cookies:
2) Copy the value of the session cookie

![session-cookie.png](session-cookie.png)

3) Run the following commands:

    mkdir -p ~/.config/aocd
    cat <session-cookie-value> > ~/.config/aocd/session

### Generate all files using the template

    uv run generate

## Usage

### Test solution against the examples

    uv run test [DAY]

### Solve puzzle

    uv run solve [DAY]

