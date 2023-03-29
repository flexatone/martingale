


from music21 import stream, note, pitch, meter, dynamics

def ambitus():


    ampList = [.1, .25, .4, .6, .75, .9]
        
    s = stream.Stream()
    for i in range(len(ampList)):    
        m = stream.Measure()
        ts = meter.TimeSignature('8/4')
        m.append(ts)

        dm = dynamics.Dynamic(ampList[i])

        n = note.Note('g')
        n.quarterLength = 1
        n.addLyric('unit interval: %.2f' % ampList[i])
        n.addLyric('midi velocity: %s' % int(round(ampList[i] * 127)))

        m.append(dm)
        m.append(n)

        s.append(m.makeBeams())
    
    s.show()


if __name__ == '__main__':
    ambitus()