
<h1 align="center">
    <br>
    Av1an
    </br>
</h1>

<h2 align="center">All-in-one tool for streamlining av1 encoding</h2>

![alt text](https://cdn.discordapp.com/attachments/665440744567472169/666865780012482571/Screenshot_20200115_064531.png)

<h2 align="center">Easy And Efficient </h2>

Start using AV1 encoding. All open-source encoders are supported (Aomenc, Rav1e, SVT-AV1)

Example with default parameters:

    ./av1an.py -i input

With your own parameters:

    ./av1an.py -i input -enc aomenc -e '--cpu-used=3 --end-usage=q --cq-level=30' -a '-c:a libopus -b:a 24k'

<h2 align="center">Usage</h2>

    -i   --file_path        Input file (relative or absolute path)
    
    -enc --encoder          Encoder to use (aomenc or rav1e or svt_av1. Default: aomenc. 
                            Example: -enc rav1e)
    
    -e   --encoding_params  Encoder settings flags (If not set, will be used default parameters. 
                            Required for SVT-AV1s)
    
    -a   --audio_params     FFmpeg audio settings flags (Default: copy audio from source to output)
    
    -t   --workers          Maximum number of workers (overrides automatically set number of workers.
                            Aomenc recommended value is YOUR_THREADS - 2 (Single thread per worker)
                            Rav1e and SVT-AV1 uses multiple threads, 
                            Example: '--tile-rows 2 --tile-cols 2' load 2.5 - 3.5 threads
                            4 rav1e workers is optimal for 6/12 cpu 
    
    -tr  --threshold        PySceneDetect threshold (Optimal values in range 15 - 50.
                            Bigger value = less sensitive )
    
    -p   --pass             Set number of passes for encoding (Default: Aomenc: 2, Rav1e: 1)
                            At current moment 2nd pass Rav1e and SVT-AV1 not working
    
    -log --logging          Path to .log file(Default: no logging) 

<h2 align="center">Main Features</h2>

**Spliting video by scenes for parallel encoding** because AV1 encoders currently not good at multithreading, encoding is limited to single or couple of threads at the same time.

[PySceneDetect](https://pyscenedetect.readthedocs.io/en/latest/) used for spliting video by scenes and running multiple encoders.

Simple and clean console look

Automatic determination of how many workers the host can handle

Building encoding queue with bigger files first, minimizing waiting for last scene to encode

Both video and audio encoding option with FFmpeg

And many more to go..

## Dependencies

* [FFmpeg](https://ffmpeg.org/download.html)
* [AOMENC](https://aomedia.googlesource.com/aom/) For Aomenc encoder
* [Rav1e](https://github.com/xiph/rav1e) For Rav1e encoder
* [PyScenedetect](https://pyscenedetect.readthedocs.io/en/latest/) 
* [mkvmerge/python-pymkv](https://pypi.org/project/pymkv/)
