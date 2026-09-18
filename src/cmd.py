import subprocess

def render(path: str, output_video_directory_path: str,
    name: str, weights: list, fps: int):
    for i in range(len(weights)): weights[i] = str(weights[i])
    cmd = [
        'ffmpeg',
        '-i', path,
        '-vf', f"tmix=frames={len(weights)}:weights='{' '.join(weights)}',fps={fps}",
        '-c:v', 'h264_amf',
        '-rc', 'cqp',
        '-qp_i', '16',
        '-qp_p', '18',
        '-qp_b', '20',
        '-quality', 'quality',
        '-usage', 'transcoding',
        '-c:a', 'copy',
        f'{output_video_directory_path}\\{name} (RENDER).mp4'
    ]
    try:
        result = subprocess.run(cmd, check = True, capture_output = True, text = True)
    except subprocess.CalledProcessError as e:
        print(f"ffmpeg error: {e.stderr}")
    return

def get_video_fps(video_path: str):
    cmd = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=r_frame_rate',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        video_path
    ]
    try:
        result = subprocess.run(cmd, check = True, capture_output = True, text = True)
    except subprocess.CalledProcessError as e:
        print(f"ffprobe error: {e.stderr}")
    return int(result.stdout.split("/")[0])/int(result.stdout.split("/")[1])
