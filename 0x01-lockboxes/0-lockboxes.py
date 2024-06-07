#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """checks if all boxes can be unlocked or not. bruh"""
    change = True
    missing_keys = list(range(1, len(boxes)))
    unvisited = list(range(len(boxes)))

    while (change):
        change = False
        for box in unvisited:
            if box not in missing_keys:
                change = True
                for new_key in boxes[box]:
                    if new_key in unvisited and new_key in missing_keys:
                        missing_keys.pop(missing_keys.index(new_key))
                unvisited.pop(unvisited.index(box))
    return len(unvisited) == 0
