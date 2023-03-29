

SynthDef("noise", { arg dur, ampStart, ampEnd; 
   var amp;
   amp = Line.ar(ampStart, ampEnd, dur, doneAction: 2);
   Out.ar(0, WhiteNoise.ar(amp));
 }).writeDefFile;
s.sendSynthDef("noise");

// /s_new defName nodeID addAction targetNode
s.sendMsg("/s_new", "noise", -1, 1, 1, "dur", 2, "ampStart", 0, "ampEnd", 0.2);

s.sendMsg("/s_new", "noise", -1, 1, 1, "dur", 2, "ampStart", 0.2, "ampEnd", 0);
