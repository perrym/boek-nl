from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Stap:
    naam: str
    invoer: str
    uitvoer: str
    status: str = "gepland"

pipeline = [
    Stap("Audio extraheren", "training.mp4", "audio.wav"),
    Stap("Transcript maken", "audio.wav", "transcript.txt"),
    Stap("Frames selecteren", "training.mp4", "frames/"),
    Stap("Beeldanalyse", "frames/", "frame_labels.json"),
    Stap("Samenvatting", "transcript.txt + frame_labels.json", "samenvatting.md"),
]

for stap in pipeline:
    stap.status = "gesimuleerd"
    log = {**asdict(stap), "tijd": datetime.now().isoformat(timespec="seconds")}
    print(log)
