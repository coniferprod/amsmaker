# AMSMaker

AMSMaker is a tool for creating AMS (Ableton Meta Sound) files for Ableton's Simpler and Sampler instruments.
You can export AMS files from Ableton Operator, but since they are simple text files, they can easily be generated
with a utility like AMSMaker. This opens up a wealth of possibilities for sound design.

## Operation

AMSMaker generates AMS files based on an additive synthesis method developed and patented by Philip Y. Dahl in 1999.
The patent on the method has expired in 2019.

The variant of the method used by AMSMaker utilizes five parameters. There is a small selection of pre-made waveform
definitions, with values for the parameters already set.

TODO: Read the parameter values as command line parameters.

## Requirements

* Python 3.7 or later (may work with Python 2.x if you squint, but [seriously](https://www.theregister.co.uk/2019/09/09/the_end_of_python_2_2020/))

## References

* [Ableton Operator and AMS Files](https://www.mybackroombeats.com/ableton-live/blog/2019/5/15/ableton-operator-and-ams-files) at [My Backroom Beats](https://www.mybackroombeats.com)
* [Method for additive synthesis of sound](https://patents.google.com/patent/US6143974), U.S. Patent 6143974
