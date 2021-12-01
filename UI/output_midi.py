import music21
def mk_score(quantized_note, predictions_per_note) :
    '''악보를 만듭니다.'''
    sc = music21.stream.Score()
    '''실제 노래와 일치하도록 속도를 조정합니다.'''
    bpm = 50 * 50 / predictions_per_note
    print('bpm: ', bpm)
    a = music21.tempo.MetronomeMark(number=bpm)
    sc.insert(0, a)

    for snote in quantized_note:
        d = 'half'
        if snote == 'Rest':
            sc.append(music21.note.Rest(type=d))
        else:
            sc.append(music21.note.Note(snote, type=d))
    return sc

def midi_play(sc) :
    sc.show('midi')

def midi_save(sc, filename) :
    sc.write('midi', fp=filename)
