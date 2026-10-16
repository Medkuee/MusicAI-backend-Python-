# MusicAI (Python backend)

This is the AI part of my 2023 Computer Science graduation project, MusicAI. It's a small Flask server. It takes the notes a user plays in the [MusicAI-mobile](https://github.com/Medkuee/MusicAI-mobile) app, continues the melody with Google Magenta's **pretrained** Melody RNN, and exports the result as MIDI and MusicXML.

It's an academic prototype, not a production service.

## How a recording becomes music

`main.py` does the following for each request:

1. **Receive the notes.** The app sends 10 notes. Each has a piano key index (0–87), a start time in ms and a duration in seconds.
2. **Build a `NoteSequence`.** Each key index is converted to a MIDI pitch (`key + 21`), and times are converted to seconds. The sequence uses a fixed 60 BPM and velocity 80.
3. **Continue the melody.** The pretrained `lookback_rnn` model (`models/lookback_rnn.mag`) continues the melody from just after the last note, up to 512 steps (about 128 s at 60 BPM). Temperature is 1.0. Melody RNN is monophonic, so it generates a single melody line.
4. **Export.** `note_seq` writes the result (your notes plus the continuation) to `<name>.mid`. `music21` then converts that to `<name>.mxl` for the sheet music view.

## API

`POST /create-music`

```json
{
  "name": "14",
  "notes": [{ "note": 39, "startTime": 0, "duration": 0.32, "noteValue": "C4" }]
}
```

- `name` is the music id from the Node backend. It must be 1–64 letters, numbers, `-` or `_`, because it's used as the filename.
- `notes` takes 1–100 notes. Invalid input returns `400` with `{ "error": "..." }`.
- On success, it writes `<name>.mid` and `<name>.mxl` and returns `Data submitted successfully`.

The server runs on Flask's default `http://127.0.0.1:5000`.

## Connection to the mobile app

The mobile app first saves the recording in [MusicAI-backend](https://github.com/Medkuee/MusicAI-backend). It then sends the same notes here, with the new music id as `name`.

This server writes the output files straight into the mobile app's source folder (`../MusicAI-mobile/src/screens/main/guest/guestFavoriteScreen/music-output/`). The app's WebViews load them from there through the Metro dev server. So it only works when the repos are cloned side by side and everything runs on one machine. You can change the folder with `OUTPUT_DIR` in `.env`.

## Pretrained models vs. my own work

**Pretrained (not mine).** These are [Magenta](https://github.com/magenta/magenta) Melody RNN bundles released by Google, in `models/`:

- `lookback_rnn.mag` is the only one used by the app.
- `basic_rnn.mag`, `attention_rnn.mag` and `mono_rnn.mag` are other Melody RNN variants. The app doesn't use them.

I didn't train or fine-tune these.

**My own experiments.** None of these are used by the app:

- `utilts.py` converts note CSVs into training formats.
- `onlyNotesCategory.py` is a Keras LSTM that predicts the next note from the previous three, trained on a single piece.
- `threeOutputs.py` is an LSTM that predicts start time, end time and pitch together. `third_model.h5` is its trained weights.
- `pianoPlayer.py` is an earlier version of the server. It ignores the input and converts a fixed CSV piece to MIDI and MusicXML.
- `notesCrawler.py` is an unfinished Selenium scraper.
- `pythonTests/` is a scratch folder for trying out libraries.

The final app uses the pretrained Magenta model, not these experiments.

## Tech stack

Python 3, Flask, Magenta (Melody RNN), note-seq, music21, python-dotenv. The experiments also use TensorFlow/Keras, NumPy and pygame.

## Running locally

```bash
python3 -m venv env
source env/bin/activate
pip install flask magenta note-seq music21 python-dotenv
cp .env.example .env
python3 main.py
```

The model loads at startup, so the first start takes a while. This setup hasn't been re-tested recently. Magenta is no longer actively developed and depends on older TensorFlow versions, so it may not install on recent Python versions. An older Python 3 is more likely to work.

`requirements.txt` is a full, unpinned `pip freeze` of my environment at the time. It includes macOS-only `pyobjc` packages and everything the experiments needed. The `pip install` line above is the minimum for `main.py`.

## Data and third-party files

These files are in the repo for reference. Check their licenses before reusing or redistributing them:

- `data/`, `csv-classical/`: note label CSVs that appear to come from the MusicNet dataset.
- `mp3/`: single-note piano samples. The same set is in the mobile app.
- `soundfonts/`: piano SoundFonts, source not documented.
- `soundwave/`: WAV files, source not documented.
- `models/*.mag`: Magenta pretrained bundles, published by the Magenta project.
- `pythonTests/opensheetmusicdisplay.min.js`: a vendored copy of OpenSheetMusicDisplay.
