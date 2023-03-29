

tagRef = {
   'dsp': 'Digital Signal Processing',
   'time': 'Time',
   'gen': 'Signal Generators',
   'fil': 'Filters',
   'envl': 'Envelope Generators',
   'comm': 'Communications',
   'math': 'Math',
   'rel': 'Relational Operators',
   'logic': 'Logical Operators',
   'con': 'Data Conversion',
   'list': 'List Processing',
}


# to add:
# drip
# tabdump: get a table as a list! veyr useful
# sprintf: convert characters to numbers





ref = {

'mult' : {
   'title' : '*',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Multiplier.
""",
   'xref' : [''],
   'tags' : ['math'],
},


'plus' : {
   'title' : '+',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Addition.
""",
   'xref' : [''],
   'tags' : ['math'],
},

'divide' : {
   'title' : '/',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Division.

Note: it is always better to use multiplication by fraction for scaling downward.
""",
   'xref' : [''],
   'tags' : ['math'],
},

'minus' : {
   'title' : '-',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Subtraction.
""",
   'xref' : [''],
   'tags' : ['math'],
},

'pow' : {
   'title' : 'pow',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Exponentiate a number. The object returns the value at the left inlet to the power of the right inlet where the left inlet is the base and the right inlet is the exponent. For example: 2 to the power of 2 = 4 (i.e. 2 Squared)
""",
   'xref' : [''],
   'tags' : ['math'],
},

'max' : {
   'title' : 'max',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Returns the greater of the two numbers passed to its inlets. For example, if the creation argument (or right inlet) is equal to 10, and you send 9 to the left inlet then the object will return 10 If you pass it an 11, then object returns 11.
""",
   'xref' : ['min'],
   'tags' : ['math'],
},

'min' : {
   'title' : 'min',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Returns the lesser of the two numbers passed to its inlets. For example, if the creation argument (or right inlet) is equal to 10, and you send 9 to the left inlet then the object will return 9 If you pass it an 11, then object returns 10
""",
   'xref' : ['max'],
   'tags' : ['math'],
},

# relational operators
'gt' : {
   'title' : '>',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Evaluate two numbers; output 1 if the left inlet value is greater than the right inlet value, else 0.
""",
   'xref' : [''],
   'tags' : ['rel'],
},
'gtoe' : {
   'title' : '>=',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Evaluate two numbers; output 1 if the left inlet value is greater than or equal to the right inlet value, else 0.
""",
   'xref' : [''],
   'tags' : ['rel'],
},
'e' : {
   'title' : '==',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Evaluate two numbers; output 1 if equal, else 0.
""",
   'xref' : [''],
   'tags' : ['rel'],
},
'ne' : {
   'title' : '!=',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Evaluate two numbers; output 1 if not equal, else 0.
""",
   'xref' : [''],
   'tags' : ['rel'],
},
'lte' : {
   'title' : '<=',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Evaluate two numbers; output 1 if the left inlet value is less than or equal to the right inlet value, else 0.
""",
   'xref' : [''],
   'tags' : ['rel'],
},
'lt' : {
   'title' : '<',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Evaluate two numbers; output 1 if the left inlet value is less than the right inlet value, else 0.
""",
   'xref' : [''],
   'tags' : ['rel'],
},
'mod' : {
   'title' : 'mod',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Takes a number in its left inlet and will divide that number by either the creation argument or the number given at its left inlet and will produce the value of the remainder at its outlet. If no creation argument is given, then the default value is 1.
""",
   'xref' : [''],
   'tags' : ['rel', 'math'],
},
'div' : {
   'title' : 'div',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Takes a number in its left inlet and will divide that number by either the creation argument or the number given at its left inlet and will produce the result without a remainder. If no creation argument is given, then the default value is 1
""",
   'xref' : [''],
   'tags' : ['rel', 'math'],
},

'sin' : {
   'title' : 'sin',
     'aka' : '',
   'tilde' : 0,
   'doc' : """
""",
   'xref' : [''],
   'tags' : ['math'],
},
'cos' : {
   'title' : 'cos',
     'aka' : '',
   'tilde' : 0,
   'doc' : """
""",
   'xref' : [''],
   'tags' : ['math'],
},
'tan' : {
   'title' : 'tan',
     'aka' : '',
   'tilde' : 0,
   'doc' : """
""",
   'xref' : [''],
   'tags' : ['math'],
},
'atan' : {
   'title' : 'atan',
     'aka' : '',
   'tilde' : 0,
   'doc' : """
""",
   'xref' : [''],
   'tags' : ['math'],
},
'atan2' : {
   'title' : 'atan2',
     'aka' : '',
   'tilde' : 0,
   'doc' : """
""",
   'xref' : [''],
   'tags' : ['math'],
},
'sqrt' : {
   'title' : 'sqrt',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Square-root.
""",
   'xref' : [''],
   'tags' : ['math'],
},
'log' : {
   'title' : 'log',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Natural logarithm.
""",
   'xref' : [''],
   'tags' : ['math'],
},
'expr' : {
   'title' : 'expr',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Evaluate arbitrary expressions.
""",
   'xref' : ['expr-tilde'],
   'tags' : ['math'],
},
'abs' : {
   'title' : 'abs',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Absolute value.
""",
   'xref' : [''],
   'tags' : ['math'],
},

# logic operators

'bit-and' : {
   'title' : '&',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Bitwise and.
""",
   'xref' : [''],
   'tags' : ['logic'],
},
'bit-or' : {
   'title' : '|',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Bitwise or.
""",
   'xref' : [''],
   'tags' : ['logic'],
},
'left-shift' : {
   'title' : '<<',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Left shift.
""",
   'xref' : [''],
   'tags' : ['logic'],
},
'right-shift' : {
   'title' : '>>',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Right shift.
""",
   'xref' : [''],
   'tags' : ['logic'],
},
'logical-and' : {
   'title' : '&&',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Logical and.
""",
   'xref' : [''],
   'tags' : ['logic'],
},
'logical-or' : {
   'title' : '||',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Logical or.
""",
   'xref' : [''],
   'tags' : ['logic'],
},
'modulus' : {
   'title' : '%',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Modulus.
""",
   'xref' : [''],
   'tags' : ['math'],
},

# other objects

'append' : {
   'title' : 'append',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Add item to a list. [append] maintains a pointer to a scalar, or else an empty pointer to the head of a list. You may set the pointer using the leftmost inlet. The creation arguments specify the template of a new scalar to append, and the names of the fields (there should be at least one) you will wish to initialize. To append an object, send a number to the leftmost inlet. [append]'s pointer is updated to point to the new scalar, and the new pointer is also output.
""",
   'xref' : [],
},



'counter' : {
   'title' : 'counter',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Count the number of bangs received. Can be used to create a list of increasing numbers that changes direction and can reset, jump to minimum, and jump to maximum. Arguments: [counter max], [counter min max], [counter dir min max]""",
   'xref' : [''],
},


'until' : {
   'title' : 'until',
     'aka' : '',
   'tilde' : 0,
   'doc' : """After receiving a number or a bang in the left inlet, [until] will continue to produce bangs until either the provided number is reached or a bang is received in the right inlet. Providing a number in the left inlet makes [until] function identical to [uzi] in Max.""",
   'xref' : [''],
},



'delay' : {
   'title' : 'delay',
     'aka' : 'del',
   'tilde' : 0,
   'doc' : """Bang after a timed delay. The [delay] object sends a bang to its outlet after a delay in milliseconds specified by its right inlet or its creation argument. Only bang messages are delayed. 

[delay]'s left inlet accepts a number, or one of two messages: "bang" or "stop". If a number is sent to its inlet, [delay] will set the delay time equal to that number and schedule the outgoing "bang". The "stop" method will inform [delay] to cancel its scheduled output.

[delay] accepts only one "bang" at a time. It cannot process multiple delays. In other words, sending a "bang" to a [delay] which is already set will reschedule its output, canceling the old one.
""",
   'xref' : [],
   'tags' : ['time'],
},

'float' : {
   'title' : 'float',
     'aka' : 'f',
   'tilde' : 0,
   'doc' : """Providing a float in the right inlet will store the value and not provide output. A bang or float in the left inlet sends output immediately.""",
   'xref' : ['int', 'zl-reg'],
},

'int' : {
   'title' : 'int',
     'aka' : 'i',
   'tilde' : 0,
   'doc' : """Providing a number in the right inlet will store the value and not provide output. A bang or number in the left inlet sends output immediately. Can also be used to convert a float to an integer value.""",
   'xref' : ['float', 'zl-reg'],
},

'loadbang' : {
   'title' : 'loadbang',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Send "bang" automatically when patch loads. The inlet is inactive and serves no purpose.""",
   'xref' : [],
},

# 'list-append' : {
#    'title' : 'list append',
#      'aka' : '',
#    'tilde' : 0,
#    'doc' : """Add left inlet list behind right inlet list.
# 
# Note: not the same as [append].
# """,
#    'xref' : ['zl-join'],
# },
# `
# 'list-prepend' : {
#    'title' : 'list prepend',
#      'aka' : '',
#    'tilde' : 0,
#    'doc' : """Add left inlet list in front of right inlet list.
# 
# Note: not the same as [prepend].
# """,
#    'xref' : ['zl-join'],
# },


'prepend' : {
   'title' : 'prepend',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Add left inlet message in front of construction argument message.
""",
   'xref' : ['zl-join'],
},




'mtof' : {
   'title' : 'mtof',
     'aka' : '',
   'tilde' : 0,
   'doc' : """MIDI pitch to frequency conversion.""",
   'xref' : ['mtof-tilde'],
   'tags' : ['con'],
},
'ftom' : {
   'title' : 'ftom',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Frequency to midi pitch conversion""",
   'xref' : [],
   'tags' : ['con'],
},
'powtodb' : {
   'title' : 'powtodb',
     'aka' : '',
   'tilde' : 0,
   'doc' : """""",
   'xref' : [],
   'tags' : ['con'],
},
'rmstodb' : {
   'title' : 'rmstodb',
     'aka' : '',
   'tilde' : 0,
   'doc' : """The [dbtorms] and [rmstodb] objects convert from decibels to linear ("RMS") amplitude, so that 100 dB corresponds to an "RMS" of 1 Zero amplitude (strictly speaking, minus infinity dB) is clipped to zero dB, and zero dB, which should correspond to 0.0001 in "RMS", is instead rounded down to zero.""",
   'xref' : [],
   'tags' : ['con'],
},
'dbtorms' : {
   'title' : 'dbtorms',
     'aka' : '',
   'tilde' : 0,
   'doc' : """The [dbtorms] and [rmstodb] objects convert from decibels to linear ("RMS") amplitude, so that 100 dB corresponds to an "RMS" of 1 Zero amplitude (strictly speaking, minus infinity dB) is clipped to zero dB, and zero dB, which should correspond to 0.0001 in "RMS", is instead rounded down to zero.""",
   'xref' : [],
   'tags' : ['con'],
},
'dbtopow' : {
   'title' : 'dbtopow',
     'aka' : '',
   'tilde' : 0,
   'doc' : """""",
   'xref' : [],
   'tags' : ['con'],
},


'line' : {
   'title' : 'line',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Ramp generator. [line]'s left inlet defines the "target" value. The right inlet defines the "time" value. The "target, time" pair of numbers inform [line] to produce a numeric "ramp" from its current value (whatever that might be at any given moment) to the new value within the alloted time which is defined at the right inlet.""",
   'xref' : ['line-tilde', 'vline-tilde'],
},


'metro' : {
   'title' : 'metro',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Sends a series of bangs at a constant rate.""",
   'tags' : ['time'],
},

'moses' : {
   'title' : 'moses',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Moses takes numbers and outputs them at left if they're less than a control value, and at right if they're greater or equal to it. The creation argument initializes the control value (10 in this example) and the right inlet changes it.""",
   'xref' : [''],
   'tags' : ['math'],
},

# midi objects
'notein' : {
   'title' : 'notein',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Read incoming stream of MIDI notes. The [notein] object reads incoming MIDI notes and reports their note number, velocity and channel number. Without the argument it reads from all MIDI channels.""",
   'tags' : ['midi'],
},

'stripnote' : {
   'title' : 'stripnote',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Stripnote takes note-off (zero-velocity) messages out of a stream of MIDI-style note message and passes the others through unchanged.""",
   'tags' : ['midi'],
},

'ctlin' : {
   'title' : 'ctlin',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Read incoming Control Change message from MIDI.""",
   'tags' : ['midi'],
},
'pgmin' : {
   'title' : 'pgmin',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Read incoming Program Change message from MIDI.""",
   'tags' : ['midi'],
},
'bendin' : {
   'title' : 'bendin',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Read incoming pitch bend values from MIDI.""",
   'tags' : ['midi'],
},



# other objects
'clip' : {
   'title' : 'clip',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Force a number between a range. Minimum and maximum can be assigned as creation arguments.
""",
   'xref' : [],
},


'gate' : {
   'title' : 'gate',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Route one input to one or more outputs based on a number. The number of outlets can be configured with a creation argument. The leftmost inlet controls which outlet is active; outlet selection number counts from 1, where 0 is none. The rightmost inlet is the data to be gated.""",
   'xref' : [],
   'tags' : [''],
},

'pipe' : {
   'title' : 'pipe',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Delay a message. Delay time is specified in milliseconds.""",
   'xref' : ['delay'],
   'tags' : ['time'],
},

'pack' : {
   'title' : 'pack',
     'aka' : '',
   'tilde' : 0,
   'doc' : """The pack object takes a series of inputs and then outputs a concatenated list. The number of creation arguments determines the number of inlets while the type of creation arguments determines the types of messages that [pack] should expect to receive at each inlet - although with some peculiarities described below.

Any message to the first inlet will force [pack] to output its package - its list of values. A bang to the first inlet will force [pack] to output the current values without resetting any of them.""",
   'xref' : ['unpack'],
},

'random' : {
   'title' : 'random',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Generates random numbers between 0 and N-1, where N is the creation argument or the value of the right inlet.""",
   'xref' : [],
},

'route' : {
   'title' : 'route',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Route messages according to their first element. Route can be given exact messages to match or data types. Route checks the first element of a message against each of its creation arguments, which may be numbers or symbols (but not a mixture of the two unless the data types are defined explicitly), then sends the messages through the appropriate outlets. If a match is found, and the message contains only ONE element, then a bang is sent out the corresponding outlet. If a match if found, and the message contains multiple elements (a list), then all the list elements except the first element is sent out the corresponding outlet. Differs from [select] in that the complete message (not just a bang) is passed for lists.""",
   'xref' : ['select'],
},


'select' : {
   'title' : 'select',
     'aka' : 'sel',
   'tilde' : 0,
   'doc' : """In its simplest form [select] checks its input against the constant "6" (which is defined by the creation argument). If they match, the first outlet gives "bang"; otherwise the input is simply sent through to the second outlet.

[select] can also be used to match symbols like the example in the upper-right of this patch. It important to note that the FIRST creation argument indicates to the [select] object which data type to expect. If your first creation argument is a symbol, like "dog", then the object will test only symbols and numbers will be ignored!
""",
   'xref' : ['route'],
},



'timer' : {
   'title' : 'timer',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Measures elapsed time between right inlet and left inlet bangs in milliseconds.
""",
   'xref' : [],
},

'key' : {
   'title' : 'key',
     'aka' : '',
   'tilde' : 0,
   'doc' : """""",
   'xref' : [],
},
'keyup' : {
   'title' : 'keyup',
     'aka' : '',
   'tilde' : 0,
   'doc' : """""",
   'xref' : [],
},
'keyname' : {
   'title' : 'keyname',
     'aka' : '',
   'tilde' : 0,
   'doc' : """""",
   'xref' : [],
},



'tabwrite' : {
   'title' : 'tabwrite',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Write to a named array by providing value and index pairs.
""",
   'xref' : ['tabread'],
},


'tabread' : {
   'title' : 'tabread',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Read from a named array by providing an index.""",
   'xref' : ['tabwrite'],
},


'trigger' : {
   'title' : 'trigger',
     'aka' : 't',
   'tilde' : 0,
   'doc' : """Sequence messages in right-to-left order and convert data. Can be abbreviated as a f; float as f, bang as b, symbol as s, list as l, anything as a.

Whenever going from one outlet to multiple inlets with a message, use [trigger] to make explicit where messages are going.
""",
   'xref' : [],
},


'unpack' : {
   'title' : 'unpack',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Combine several atoms into one message. The pack object takes a series of inputs and then outputs a concatenated list. The number of creation arguments determines the number of inlets while the type of creation arguments determines the types of messages that [pack] should expect to receive at each inlet.
""",
   'xref' : ['pack'],
},


'zl-ecils' : {
   'title' : 'zl ecils',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Split a list provided in the left inlet at an index value provided in the right inlet. The remainder of the list is provided out the right outlet.

Note: index values start at 1 and count from the right of the list.
""",
   'xref' : [],
},

'zl-group' : {
   'title' : 'zl group',
     'aka' : '',
   'tilde' : 0,
   'doc' : """A list, of a size specified in the creation argument or by a value provided to the right inlet, is output after being received in the left inlet. Values can be provided to the left inlet either a single list or as series of values. 
""",
   'xref' : [],
},

'zl-iter' : {
   'title' : 'zl iter',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Given a list in the left inlet, output lists of a size specified in the creation argument or by a value provided to the right inlet.
""",
   'xref' : [],
},

'zl-join' : {
   'title' : 'zl join',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Join two lists; output is provided after list in left inlet is received.
""",
   'xref' : [],
},


'zl-len' : {
   'title' : 'zl len',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Return the length of the list from the left outlet.
""",
   'xref' : [],
},


'zl-reg' : {
   'title' : 'zl reg',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Store a list in the right inlet; bang it out later.
""",
   'xref' : [],
},

'zl-rotate' : {
   'title' : 'zl rotate',
     'aka' : 'zl rot',
   'tilde' : 0,
   'doc' : """Rotate a list provided in the left inlet by the number provided in the right inlet.
""",
   'xref' : [],
},

'zl-sect' : {
   'title' : 'zl sect',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Output the elements that are common to both input lists. 
""",
   'xref' : [],
},

'zl-slice' : {
   'title' : 'zl slice',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Split a list provided in the left inlet at an index value provided in the right inlet. The remainder of the list is provided out the left outlet.

Note: index values start at 1 and count from the left of the list.
""",
   'xref' : [],
},

'zl-union' : {
   'title' : 'zl union',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Returns a combination of both lists. 
""",
   'xref' : [],
},

'zl-rev' : {
   'title' : 'zl rev',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Reverse a list.
""",
   'xref' : [],
},

'zl-nth' : {
   'title' : 'zl nth',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Given an index value provided in the right inlet and a list in the left inlet, output the value at the specified index. 

Note: index values start at 1. If the index is greater than the length of the list, no output is returned.
""",
   'xref' : [],
},

'inlet' : {
   'title' : 'inlet',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Within an abstraction, provide an inlet for numbers or symbols.

Note: for signals use [inlet~]""",
   'xref' : ['outlet'],
   'tags' : ['comm'],
},

'outlet' : {
   'title' : 'outlet',
     'aka' : '',
   'tilde' : 0,
   'doc' : """Within an abstraction, provide an outlet for numbers or symbols.

Note: for signals use [outlet~]""",
   'xref' : ['inlet'],
   'tags' : ['comm'],
},





# signal objects

'readsf-tilde' : {
   'title' : 'readsf~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Reading and playing a one or more channel AIFF or WAVE audio file. Similar to [sfplay~] in Max/MSP. 
""",
   'xref' : [''],
   'tags' : [''],
},




'clip-tilde' : {
   'title' : 'clip~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Force a signal between a minimum and a maximum value. When the input signal is beyond the range, the limit value is returned. 
""",
   'xref' : ['max-tilde', 'min-tilde'],
   'tags' : [''],
},



'delay-tilde' : {
   'title' : 'delay~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Delay a signal in the left inlet by a number of samples as set in the right inlet. Multiply the delay time by the sampling rate to set the delay time in seconds.  
""",
   'xref' : ['delread-tilde', 'delwrite-tilde', 'vd-tilde'],
   'tags' : ['dsp'],
},

'delread-tilde' : {
   'title' : 'delread~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Delay a signal. One or more independent [delread~] objects can read a delay line from one named [delwrite~] object. The delay line must be named as a construction argument. A float input will set the delay time in milliseconds. Creation order matters: for non-recursive algorithms, create [delread~] after [delwrite~]. Similar to [tapout~] in Max/MSP.
""",
   'xref' : ['delwrite-tilde', 'vd-tilde', 'delay-tilde'],
   'tags' : ['dsp'],
},
'delwrite-tilde' : {
   'title' : 'delwrite~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Delay a signal. Provide a signal as input to add to a delay line. One or more [delread~] or [vd~] objects can read from the delay line created with the [delwrite~] object. Creation order matters: for non-recursive algorithms, create [delread~] after [delwrite~]. Similar to [tapin~] in Max/MSP.
""",
   'xref' : ['delread-tilde', 'vd-tilde', 'delay-tilde'],
   'tags' : ['dsp'],
},
'vd-tilde' : {
   'title' : 'vd~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Delay a signal. One or more independent [vd~] objects can read a delay line from one named [delwrite~] object. The delay line must be named as a construction argument. A signal input will set the delay time in milliseconds. Similar to [tapout~] in Max/MSP.
""",
   'xref' : ['delwrite-tilde', 'delay-tilde', 'delread-tilde'],
   'tags' : ['dsp'],
},




'mult-tilde' : {
   'title' : '*~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Signal multiplier (scaling).

Note: rightmost inlet will not accept a signal input if an object creation argument is provided.
""",
   'xref' : [''],
   'tags' : ['math'],
},


'plus-tilde' : {
   'title' : '+~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Signal addition (mixing).
""",
   'xref' : [''],
   'tags' : ['math'],
},

'divide-tilde' : {
   'title' : '/~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Signal division.

Note: it is always better to use multiplication by a floating-point value than division.
""",
   'xref' : [''],
   'tags' : ['math'],
},


'minus-tilde' : {
   'title' : '-~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Signal subtraction.
""",
   'xref' : [''],
   'tags' : ['math'],
},
'pow-tilde' : {
   'title' : 'pow~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Exponentiate a signal.
""",
   'xref' : [''],
   'tags' : ['math'],
},


'max-tilde' : {
   'title' : 'max~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Return the larger of two signals.
""",
   'xref' : ['clip-tilde', 'min-tilde'],
   'tags' : ['math'],
},
'min-tilde' : {
   'title' : 'min~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Return the smaller of two signals.
""",
   'xref' : ['clip-tilde', 'max-tilde'],
   'tags' : ['math'],
},


# converters


'mtof-tilde' : {
   'title' : 'mtof~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """MIDI pitch to frequency conversion.""",
   'xref' : ['mtof'],
   'tags' : ['con'],
},
'ftom-tilde' : {
   'title' : 'ftom~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Frequency to midi pitch conversion""",
   'xref' : [],
   'tags' : ['con'],
},
'rmstodb-tilde' : {
   'title' : 'rmstodb~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """""",
   'xref' : [],
   'tags' : ['con'],
},
'dbtorms-tilde' : {
   'title' : 'dbtorms~',
     'aka' : '',
   'tilde' : 0,
   'doc' : """""",
   'xref' : [],
   'tags' : ['con'],
},


# others


'dac' : {
   'title' : 'dac~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Real-time audio output for Pd. Accept arguments (numbers) which indicate which audio channels are to be used by Pd. By default, this object is stereo and communicate on audio channels 1 and 2 (left and right respectively).
""",
   'xref' : [],
   'tags' : ['dsp'],

},

'env-tilde' : {
   'title' : 'env~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Envelope follower. The [env~] object takes a signal and outputs its RMS amplitude in dB (with 1 normalized to 100 dB.) Output is bounded below by zero. The analysis is "Hanning" (raised cosine) windowed.
""",
   'xref' : [''],
},

'threshold-tilde' : {
   'title' : 'threshold~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Outputs bangs when an input signal increases beyond or falls below two thresholds. For each threshold there is a debounce time, a time in milliseconds before re-triggering is available. Construction arguments are high threshold, high threshold debounce time, low threshold, low threshold debounce time.
""",
   'xref' : [''],
},


'expr-tilde' : {
   'title' : 'expr~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Evaluate signals as mathematical expressions.
""",
   'xref' : ['expr'],
   'tags' : ['gen', 'math'],
},

'line-tilde' : {
   'title' : 'line~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Audio ramp generator. The [line~] object generates linear ramps whose levels and timing are determined by messages you send it. The messages may be a single target value (causing the output to jump to the target) or a target and a time in milliseconds (to start a new ramp).
""",
   'xref' : ['vline-tilde', 'line'],
   'tags' : ['gen', 'envl'],
},


'vline-tilde' : {
   'title' : 'vline~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """High-precision audio ramp generator. The [vline~] object, like [line~], generates linear ramps whose levels and timing are determined by messages you send it. The messages consist of a target value, a time interval (zero if not supplied), and an initial delay (also zero if not supplied.) Ramps may start and stop between audio samples, in which case the output is interpolated accordingly.

Any number of future ramps may be scheduled and [vline~] will remember them and execute them in order. They must be specified in increasing order of initial delay however, since a segment cancels all planned segments at any future time.
""",
   'xref' : ['vline-tilde'],
   'tags' : ['gen', 'envl'],
},

'ead-tilde' : {
   'title' : 'ead~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Exponential attack decay envelope. First inlet triggers the envelope. Second inlet (or first construction argument) sets attack time. Third inlet (or second construction argument) set decay time.
""",
   'xref' : ['vline-tilde', 'line', 'line-tilde'],
   'tags' : ['envl'],
},




'lop-tilde' : {
   'title' : 'lop~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """One-pole low pass filter. Rolloff is fixed.

Note: signals are not permitted to control cutoff frequency.

Applications: A [lop~ 30] (or similar low frequency) is an excellent way to smooth a control signal from [line] into an audio signal suitable for use as an envelope.
""",
   'xref' : ['moog-tilde', 'onepole-tilde'],
   'tags' : ['fil'],
},

'hip-tilde' : {
   'title' : 'hip~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """One-pole high pass filter. Rolloff is fixed.

Note: signals are not permitted to control cutoff frequency.
""",
   'xref' : [''],
   'tags' : ['fil'],
},

'vcf-tilde' : {
   'title' : 'vcf~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Signal-controlled bandpass filter.

Note: signals are not permitted to control Q.
""",
   'xref' : ['bpf-tilde'],
   'tags' : ['fil'],
},

'bpf-tilde' : {
   'title' : 'bpf~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Signal-controlled bandpass filter.

Note: signals are not permitted to control Q or center frequency.
""",
   'xref' : ['vcf-tilde'],
   'tags' : ['fil'],
},

'moog-tilde' : {
   'title' : 'moog~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Signal-controlled resonant lowpass filter.
""",
   'xref' : ['lop-tilde', 'onepole-tilde'],
   'tags' : ['fil'],
},

'onepole-tilde' : {
   'title' : 'onepole~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """One pole lowpass filter with singal-controlled cutoff frequency.
""",
   'xref' : ['lop-tilde', 'moog-tilde'],
   'tags' : ['fil'],
},






'noise-tilde' : {
   'title' : 'noise~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Uniformly distributed white noise; the output is between -1 and 1.
""",
   'xref' : ['pink-tilde'],
   'tags' : ['gen'],
},

'pink-tilde' : {
   'title' : 'pink~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Pink noise generator.
""",
   'xref' : ['noise-tilde'],
   'tags' : ['gen'],
},



'osc-tilde' : {
   'title' : 'osc~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Sine wave oscillator; output is between -1 and 1.

Applications: can be converted to a square wave with [expr~ $1v > .5]
""",
   'xref' : [],
   'tags' : ['gen'],
},


'phasor-tilde' : {
   'title' : 'phasor~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Sawtooth oscillator. Ramps from 0 to 1; can be considered a Sawtooth waveform between 0 and 1. 

Applications: Can be converted to a square wave with [expr~ $v1 > .5]. Pulse width modulation is available with a dynamic comparison using [expr~ $v1 > $v2]. Can be used to drive [tabread4~] and similar objects. A low frequency [phasor~] into a [bp~] can produce a sharp click.
""",
   'xref' : [],
   'tags' : ['gen'],
},


'samphold-tilde' : {
   'title' : 'samphold~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """The [samphold~] object samples its left input whenever its right input decreases in value (as a [phasor~] does each period, for example.) Both inputs are audio signals.

The "set" message sets the output value (which continues to be updated as normal afterward.) The "reset" message causes [samphold~] to act as if the specified value were the most recent value of the control input. Use this, for example, if you reset the incoming phasor but don't want the jump reflected in the output. Plain "reset" is equivalent to "reset infinity" which forces the next input to be sampled.
""",
   'xref' : [],
   'tags' : ['gen'],
},



'sig-tilde' : {
   'title' : 'sig~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Convert control message to a signal.

Note: while some tilde object inlets will convert floats into signals, better to explicitly convert to a signal with [sig~].
""",
   'xref' : [],
   'tags' : ['gen'],
},


'snapshot-tilde' : {
   'title' : 'snapshot~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Convert a signal to a number on demand. The [snapshot~] object takes a signal and converts it to a control value whenever it receives a bang in its left outlet. This object is particularly useful for monitoring outputs.
""",
   'xref' : [],
},



'wrap-tilde' : {
   'title' : 'wrap~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Remainder modulo 1. The [wrap~] object gives the difference between the input and the largest integer not exceeding it (for positive numbers this is the fractional part).
""",
   'xref' : [],
   'tags' : ['math'],
},




'send' : {
   'title' : 'send~',
     'aka' : 's~',
   'tilde' : 1,
   'doc' : """Send a signal. Use $0-name for instance-localized communication.
""",
   'xref' : ['receive'],
   'tags' : ['comm'],
},
'receive' : {
   'title' : 'receive~',
     'aka' : 's~',
   'tilde' : 1,
   'doc' : """Receive a signal. Use $0-name for instance-localized communication.
""",
   'xref' : ['send'],
   'tags' : ['comm'],
},




'switch' : {
   'title' : 'switch~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Can be used to turn DSP of a patch or sub-patch on or off.

Only one object in any window; acts on entire window and sub-windows. 
""",
   'xref' : [],
   'tags' : ['dsp'],
},




'tabwrite-tilde' : {
   'title' : 'tabwrite~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Write a signal in an array. Tabwrite~ records an audio signal sequentially into an array. Sending it "bang" writes from beginning to end of the array. To avoid writing all the way to the end, you can send a "stop" message at an appropriate later time. The "start" message allows skipping a number of samples at the beginning. (Starting and stopping occur on block boundaries, typically multiples of 64 samples, in the input signal.)
""",
   'xref' : ['tabwrite-tilde'],
},

'tabread4-tilde' : {
   'title' : 'tabread4~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """A 4-point interpolating table lookup object.

This object permits reading smoothly from any array at the audio rate with 4-point polynomial interpolation. Indexes should start at index 1 to permit initial interpolation.
""",
   'xref' : ['tabread4-tilde'],
   'tags' : ['gen']
},


'tabsend-tilde' : {
   'title' : 'tabsend~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Writes one block of a signal continuously to an array.""",
   'xref' : ['tabwrite-tilde', 'tabreceive-tilde'],
},

'tabreceive-tilde' : {
   'title' : 'tabreceive~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Read a block of a signal from an array continuously.""",
   'xref' : ['tabsend-tilde', 'tabwrite-tilde'],
},



'block' : {
   'title' : 'block~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """Block size and on/off control for DSP.

Only one object in any window; acts on entire window and sub-windows. 
""",
   'xref' : [],
   'tags' : ['dsp'],

},


'throw' : {
   'title' : 'throw~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """""",
   'xref' : ['catch'],
   'tags' : ['comm'],
},

'catch' : {
   'title' : 'catch~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """""",
   'xref' : ['throw'],
   'tags' : ['comm'],
},


'inlet-tilde' : {
   'title' : 'inlet~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """""",
   'xref' : ['outlet-tilde'],
   'tags' : ['comm'],
},

'outlet-tilde' : {
   'title' : 'outlet~',
     'aka' : '',
   'tilde' : 1,
   'doc' : """""",
   'xref' : ['inlet-tilde'],
   'tags' : ['comm'],
},



}
