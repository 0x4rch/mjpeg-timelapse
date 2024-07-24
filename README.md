This project is to capture periodic screenshots from an MJPEG video stream.

I wrote this to capture timelapse footage from my iPhone running the DroidCam application.

## How to use

1. Install the requirements
```
pip install -r requirements.txt
```

2. Setup the `.env` file
```
echo "STREAM_URL=http://ip:port/video" > .env
```

2. Run the script
```
python main.py
```

Screenshots are saved in the `snapshots` directory.

## Docker instructions

1. Build the docker image
```bash
docker build -t mjpeg-timelapse .
```

2. Run the docker container
```bash
docker run --env-file .env -v $(pwd)/snapshots:/app/snapshots -d --network host mjpeg-timelapse
```
> Note: We use host networking to allow the container to access the local network.  If your device is on an external network I would reccomend using a bridge network for greater security.

If all goes well you should see an output like:
```log
2024-07-24 17:43:12 Python 3.9.19
2024-07-24 17:43:12 Environment Variables:
2024-07-24 17:43:12 HOSTNAME=docker-desktop
2024-07-24 17:43:12 PYTHON_PIP_VERSION=23.0.1
2024-07-24 17:43:12 HOME=/root
2024-07-24 17:43:12 PYTHONUNBUFFERED=1
2024-07-24 17:43:12 GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568
2024-07-24 17:43:12 PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/e03e1607ad60522cf34a92e834138eb89f57667c/public/get-pip.py
2024-07-24 17:43:12 STREAM_URL=http://ip:port/video
2024-07-24 17:43:12 PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
2024-07-24 17:43:12 LANG=C.UTF-8
2024-07-24 17:43:12 PYTHON_VERSION=3.9.19
2024-07-24 17:43:12 PYTHON_SETUPTOOLS_VERSION=58.1.0
2024-07-24 17:43:12 PWD=/app
2024-07-24 17:43:12 PYTHON_GET_PIP_SHA256=ee09098395e42eb1f82ef4acb231a767a6ae85504a9cf9983223df0a7cbd35d7
2024-07-24 17:43:13 Snapshot saved as snapshots/snapshot_1721864593.jpg
```

## Future improvements
- Integrate with ffmpeg to turn the screenshots into a timelapse video
