#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Checks if all boxes can be unlocked or not."""
    change = True
    missing_keys = set(range(1, len(boxes)))
    unvisited = set(range(len(boxes)))

    while change and missing_keys:
        change = False
        for box in unvisited.copy():
            if box not in missing_keys:
                change = True
                for new_key in boxes[box]:
                    if new_key in unvisited and new_key in missing_keys:
                        missing_keys.remove(new_key)
                unvisited.remove(box)
    return len(missing_keys) == 0
