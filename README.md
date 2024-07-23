This project is to capture periodic screenshots from an MJPEG video stream.

I wrote this to capture timelapse footage from my iPhone running the DroidCam application.

## How to use

1. Install the requirements
```
pip install -r requirements.txt
```

2. Setup the `.env` file
```
echo "STREAM_URL=http://ip:port/video'" > .env
```

2. Run the script
```
python main.py
```

Screenshots are saved in the `snapshots` directory.

## Future improvements
- Move to a Docker container for easy deployments on home network
- Integrate with ffmpeg to turn the screenshots into a timelapse video

