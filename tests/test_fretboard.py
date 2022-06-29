from fretboard import Fretboard

def test_fretboard_exists():
    assert Fretboard
    
    
def test_highE_list():
    frets = Fretboard()
    expected = ['E','F', "F#", 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
    assert frets.EString == expected
    