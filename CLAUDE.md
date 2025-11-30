# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple Python utility that generates colorful ASCII art from text input. The project consists of a single standalone script (`ascii_name.py`) with no external dependencies beyond the Python standard library.

## Running the Application

```bash
# Basic usage
python ascii_name.py <name>

# Example
python ascii_name.py John

# Multi-word names
python ascii_name.py John Doe
```

The script is executable and can also be run directly:
```bash
./ascii_name.py <name>
```

## Code Architecture

### Main Components

- **`get_ascii_art(text)`** (ascii_name.py:11-214): Core function that converts text to ASCII art. Contains a hardcoded font dictionary mapping uppercase letters A-Z and space to their 5-line ASCII art representations. Returns a list of 5 strings representing the horizontal lines of the output.

- **`colorize(text, color_code)`** (ascii_name.py:217-219): Applies ANSI color codes to text for terminal output.

- **`main()`** (ascii_name.py:222-248): Entry point that handles command-line arguments, generates ASCII art, and prints with random colors.

### Design Notes

- The font is defined inline as a dictionary with 5-line character definitions
- Each character in the font has consistent height (5 lines) but varying widths
- Colors are randomly applied per line using ANSI escape codes (91-96)
- Only uppercase letters A-Z and space are supported; other characters are silently ignored
