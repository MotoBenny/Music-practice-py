from fretboard import Fretboard


def test_fretboard_exists():
    assert Fretboard


def test_EString():
    frets = Fretboard()
    expected = ['E', 'F', "F#", 'G', 'G#', 'A',
                'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
    assert frets.EString == expected


def test_BString():
    frets = Fretboard()
    expected = ['B', 'C', 'C#', 'D', 'D#', 'E',
                'F', "F#", 'G', 'G#', 'A', 'A#', 'B']
    assert frets.BString == expected


def test_GString():
    frets = Fretboard()
    expected = ['G', 'G#', 'A', 'A#', 'B', 'C',
                'C#', 'D', 'D#', 'E', 'F', "F#", 'G']
    assert frets.GString == expected


def test_DString():
    frets = Fretboard()
    expected = ['D', 'D#', 'E', 'F', "F#", 'G',
                'G#', 'A', 'A#', 'B', 'C', 'C#', 'D']
    assert frets.DString == expected


def test_AString():
    frets = Fretboard()
    expected = ['A', 'A#', 'B', 'C', 'C#', 'D',
                'D#', 'E', 'F', "F#", 'G', 'G#', 'A']
    assert frets.AString == expected
