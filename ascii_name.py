#!/usr/bin/env python3
"""
ASCII Art Name Generator
Displays a name in colorful ASCII art
"""

import sys
import random


def get_ascii_art(text):
    """Generate ASCII art for the given text using a simple font"""
    # Simple ASCII art font mapping for uppercase letters
    font = {
        'A': [
            "  ███  ",
            " ██ ██ ",
            "███████",
            "██   ██",
            "██   ██"
        ],
        'B': [
            "██████ ",
            "██   ██",
            "██████ ",
            "██   ██",
            "██████ "
        ],
        'C': [
            " █████ ",
            "██     ",
            "██     ",
            "██     ",
            " █████ "
        ],
        'D': [
            "██████ ",
            "██   ██",
            "██   ██",
            "██   ██",
            "██████ "
        ],
        'E': [
            "███████",
            "██     ",
            "█████  ",
            "██     ",
            "███████"
        ],
        'F': [
            "███████",
            "██     ",
            "█████  ",
            "██     ",
            "██     "
        ],
        'G': [
            " █████ ",
            "██     ",
            "██  ███",
            "██   ██",
            " █████ "
        ],
        'H': [
            "██   ██",
            "██   ██",
            "███████",
            "██   ██",
            "██   ██"
        ],
        'I': [
            "███",
            " ██",
            " ██",
            " ██",
            "███"
        ],
        'J': [
            "     ██",
            "     ██",
            "     ██",
            "██   ██",
            " █████ "
        ],
        'K': [
            "██   ██",
            "██  ██ ",
            "█████  ",
            "██  ██ ",
            "██   ██"
        ],
        'L': [
            "██     ",
            "██     ",
            "██     ",
            "██     ",
            "███████"
        ],
        'M': [
            "███   ███",
            "████ ████",
            "██ ███ ██",
            "██     ██",
            "██     ██"
        ],
        'N': [
            "██   ██",
            "███  ██",
            "██ █ ██",
            "██  ███",
            "██   ██"
        ],
        'O': [
            " █████ ",
            "██   ██",
            "██   ██",
            "██   ██",
            " █████ "
        ],
        'P': [
            "██████ ",
            "██   ██",
            "██████ ",
            "██     ",
            "██     "
        ],
        'Q': [
            " █████ ",
            "██   ██",
            "██   ██",
            "██  ███",
            " ███ ██"
        ],
        'R': [
            "██████ ",
            "██   ██",
            "██████ ",
            "██  ██ ",
            "██   ██"
        ],
        'S': [
            " █████ ",
            "██     ",
            " █████ ",
            "     ██",
            " █████ "
        ],
        'T': [
            "███████",
            "  ██   ",
            "  ██   ",
            "  ██   ",
            "  ██   "
        ],
        'U': [
            "██   ██",
            "██   ██",
            "██   ██",
            "██   ██",
            " █████ "
        ],
        'V': [
            "██   ██",
            "██   ██",
            "██   ██",
            " ██ ██ ",
            "  ███  "
        ],
        'W': [
            "██     ██",
            "██     ██",
            "██  █  ██",
            "██ ███ ██",
            " ███ ███ "
        ],
        'X': [
            "██   ██",
            " ██ ██ ",
            "  ███  ",
            " ██ ██ ",
            "██   ██"
        ],
        'Y': [
            "██   ██",
            " ██ ██ ",
            "  ███  ",
            "  ██   ",
            "  ██   "
        ],
        'Z': [
            "███████",
            "    ██ ",
            "   ██  ",
            "  ██   ",
            "███████"
        ],
        ' ': [
            "    ",
            "    ",
            "    ",
            "    ",
            "    "
        ]
    }

    text = text.upper()
    lines = ["", "", "", "", ""]

    for char in text:
        if char in font:
            for i in range(5):
                lines[i] += font[char][i] + "  "

    return lines


def colorize(text, color_code):
    """Apply ANSI color code to text"""
    return f"\033[{color_code}m{text}\033[0m"


def main():
    if len(sys.argv) < 2:
        name = "Nahum Cohen"
    else:
        name = " ".join(sys.argv[1:])

    # ANSI color codes
    colors = [
        '91',  # Bright Red
        '92',  # Bright Green
        '93',  # Bright Yellow
        '94',  # Bright Blue
        '95',  # Bright Magenta
        '96',  # Bright Cyan
    ]

    ascii_lines = get_ascii_art(name)

    print()
    for line in ascii_lines:
        # Apply random color to each line or use gradient effect
        color = random.choice(colors)
        print(colorize(line, color))
    print()


if __name__ == "__main__":
    main()
