import music21
'''양자화된 음표를 받아서 악보를 만든 후 midi로 출력'''
def convert_output(quantized_note, predictions_per_note) :
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

    # 인식된 악보를 MIDI파일에 저장
    converted_audio_file_as_midi = 'Audios/output.mid'
    fp = sc.write('midi', fp=converted_audio_file_as_midi)
    sc.show('midi')