# psyflow

**psyflow** is a lightweight helper library designed to streamline PsychoPy experiment development. It provides modular, reusable functions for screen flow (e.g., showing instructions, countdowns) and seed control (e.g., reproducible trial sequences).

---

## 📦 Features

- 🧠 Show instructions (image- or text-based)
- ✅ Display goodbye/exit screens
- ⏱️ Countdown timers (static or real-time)
- 👤 GUI-based subject info collection
- 🎲 Seed management (random/same/individualized)

---

## 📥 Installation

### 🔗 From GitHub (recommended)

```bash
pip install git+ssh://git@github.com/TaskBeacon/psyflow.git 
```
### Or for editable local development:
``` bash
git clone https://github.com/TaskBeacon/psyflow.git
cd psyflow
pip install -e .
```

## 🔧 Usage
Import from psyflow
```python
from psychopy import visual

from psyflow.screenflow import (
    show_instructions,
    show_goodbye,
    show_static_countdown,
    show_realtime_countdown,
    get_subject_info
)

from psyflow.seedcontrol import (
    setup_seed,
    setup_seed_for_settings
)
```

###  Countdown and goodbye
```python
win = visual.Window(fullscr=False)

show_static_countdown(win, start=3)
show_goodbye(win, outro_text="Experiment complete!")
```

### 🧪 Reproducible Seeding
```python
from types import SimpleNamespace

settings = SimpleNamespace(TotalBlocks=3)
subdata = ['101', '25', 'Female', 'Asian']

# Adds settings.GeneralSeed and settings.blockSeed
settings = setup_seed_for_settings(settings, subdata, mode="indiv")
```

## 📁 Module Structure
* psyflow.screenflow: Display instructions, goodbye messages, countdowns, and GUI dialogs.

* psyflow.seedcontrol: Utilities for random seed setup and reproducibility.

## 📜 License
MIT License © Zhipeng Cao