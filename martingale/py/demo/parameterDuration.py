


from music21 import stream, note, pitch, meter
from athenaCL.libATH import rhythm

def ambitus():


    ampList = [(.125, '8,1'), (.25, '4,1'), (.5, '4,2'), 
               (1, '1,1'), (2, '1,2'), (4, '1,4'), (8, '1,8')]
        
    s = stream.Stream()
    for bpm in [60, 120, 240]:
        beatDur = 60. / bpm
        for i in range(len(durList)):    
            m = stream.Measure()
            ts = meter.TimeSignature('8/4')
            m.append(ts)
    
            pt = rhythm.Pulse(durList[i][1])

            n = note.Note('g')
            n.quarterLength = durList[i][0]
            n.addLyric('%s' % n.duration.type)
            n.addLyric('@%sbpm: %.3fs' % (bpm, 
                       n.duration.quarterLength * beatDur))
            n.addLyric('pulse triple: %s' % pt)
            m.append(n)
            s.append(m.makeBeams())
    
    s.show()


if __name__ == '__main__':
    ambitus()