# Audio Breadth First Search / Depth First Search

## Idea
- Each node will have a `note` attribute that is one of the 12 notes in a single octave.
  - Future plans: add modifications that you can apply to each note (delay, flanger, chorus, fuzz, distortion, etc.)
- When performing the traversal, visited nodes will audibly play their note
  - System sounds could be cool for this -- retro vibes
- Hearing the different sound patterns will help understand the difference between BFS and DFS
  - Add more algorithms in the future (Dijkstra, Primm, etc.)

## Language?
- Python vs C/C++?
  - Python
    - Pygame, PyAudio, MIDI Libs (mido, music21)
    - Matplotlib, NetworkX for visualization of traversal paths
    - Slow, so might struggle with very large BSTs
      - Only plan on using small trees atm though, obviou
  - C/C++
    - Speed/Efficiency: Better for large trees if they end up being used
    - Responsiveness/Timing: better optimization for audio timing and speed
    - Audio libs: PortAudio for cross-platform audio playback, OpenAL for 3D and interactive audio stuff, FMOD or SDL for comprehensive sound handling
    - Probably longer development time
  - Will start with python, and try C/C++ at a later time

## Project Organization
- 

## General


## Features


## Acknowledgements
