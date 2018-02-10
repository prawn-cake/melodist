# -*- coding: utf-8 -*-


NOTES = ('A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#')
INTERVALS = [2, 2, 1, 2, 2, 2, 1]
FRETS = 22
CHORD_PROGRESSIONS = [
    (1, 4, 5),
    (1, 4, 5, 4),

    (1, 5, 4),
    (1, 5, 6, 4),
    (1, 5, 6, 3, 4),

    (1, 6, 4, 5),
    (1, 6, 2, 5),
]

# NOTE: minor - major - diminished chords progression map
# 1-4-5 are majors, 2-3-6 are minors, 7th is diminished
PROGRESSION_MAP = {1: '', 2: 'm', 3: 'm', 4: '', 5: '', 6: 'm', 7: 'dim'}


def build_scale(note):
    starting_idx = NOTES.index(note.upper())

    first_note = NOTES[starting_idx]
    yield first_note

    notes = NOTES * 3
    for step in INTERVALS:
        yield notes[starting_idx + step]
        starting_idx += step


def generate_progressions(root_note):
    scale = list(build_scale(root_note))
    for prog in CHORD_PROGRESSIONS:
        # NOTE: use num - 1 cuz it's 0-indexed array
        yield [scale[num - 1] + PROGRESSION_MAP[num] for num in prog]


if __name__ == '__main__':
    assert list(build_scale('C')) == ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
    assert list(build_scale('E')) == ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E']
    print(list(generate_progressions('C')))
    print(list(generate_progressions('A#')))
    print(list(build_scale('A')))
