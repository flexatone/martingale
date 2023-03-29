


from music21 import stream, note, pitch, meter


def ambitus():


    pitchList = []
    for i in range(1, 8):
        mGroup = ['c%s' % i, 'f#%s' % i]
        pitchList.append(mGroup)
        
    s = stream.Stream()
    for i in range(len(pitchList)):    
        mGroup = pitchList[i]
        m = stream.Measure()
        ts = meter.TimeSignature('4/4')
        m.append(ts)
        for pitchName in mGroup:
            n = note.Note(pitchName)
            n.quarterLength = 2
            n.addLyric(n.nameWithOctave)
            n.addLyric('midi: %s' % n.midi)
            n.addLyric('fq: %.2f' % n.frequency)
            m.append(n)
        m.insert(m.bestClef())
        s.append(m.makeBeams())
    
    s.show()


if __name__ == '__main__':
    ambitus()