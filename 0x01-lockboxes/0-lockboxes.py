#!/usr/bin/python3
"""
LockBoxes Challenge.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    Args:
    - boxes (list of lists): list of boxes,
    where each contains keys to other boxes.
    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    unlocked = [0]  # List to track unlocked boxes
    for box_index in unlocked:
        for key in boxes[box_index]:
            if key not in unlocked and 0 <= key < len(boxes):
                unlocked.append(key)

    return len(unlocked) == len(boxes)
