# Extracting Audio (.mp3) from Movie File (.mov)
---------

### Used Tools
- **FFmpeg** (program): industry-standard tool which reads/encodes media
- `ffmpeg-python` (library): a thin Python wrapper that builds and runs **FFmpehg** commands from Python (`pip install ffmpeg-python`)
  - FFmpeg must be installed on system
----------

## Steps

1. Install FFmpeg
- mac: `brew install ffmpeg`
- Ubuntu:`suco apt update && sudo apt install ffmpeg`

Verify
- `ffmpeg -version`

2. Install the Python wrapper
- `pip install ffmpeg-python`
  - package name is ffmpeg-python, imported as `ffmpeg`

3. Python Script
```
import ffmpeg

in_path = 'path_to_movie_file.mov`

out_path = 'outputname.mp3'

#build and run drop video (-vn_, encode MP3 with libmp3lame at 192 kbps
try:
  (
  
    ffmpeg
    .input(in_path)
    .output(
      out_path,          
      **{'vm': None},    # -vn (no video)
      acodec = 'libmp3lame',   # MP3 encoder
      audio_bitrate='192k'    # chose 128k - 320k
    )
    .overwrite_output()       #allow replacing existing file
    .run()
  )
  print("Audio Conversion Finished. Path:", out_path)
except ffmpeg.Error as e:
  print("audio conversion failed")
  print("error details:", e.stderr.decode())
```

4. Run the script
`python scriptname.py`

Breakdown:
- `vn`: "video none" aka, no video included in output file
- `acadec='libmp3lame': use the LAME MP3 encoder
- `audio_bitrate='192k'`: constant bitrate; can use '128k', '256k', or '320k'
- `try/except`: catches error from using FFmpeg
- `ffmpeg.Error`: the exception raised if FFmpeg fails (wrong path, codec missing, etc.).
- `e.stderr.decode(): shows FFmpeg's error log in case you want to debug

  
