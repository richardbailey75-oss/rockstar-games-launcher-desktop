"""Rockstar Games Launcher Desktop — A desktop helper that finds Rockstar Games Launcher library directories and archives screenshot and workshop files locally."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='rockstar_games_launcher_desktop',
        description='A desktop helper that finds Rockstar Games Launcher library directories and archives screenshot and workshop files locally.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Rockstar Games Launcher Desktop')
    print('Dated copies of Rockstar Games Launcher library data, nothing uploaded.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
