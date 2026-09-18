from pathlib import Path

# src
import cmd
import weight_preset

def main():

    ok_video_extension = [".mp4", ".mkv"]
    input_video_directory_path = ""
    output_video_directory_path = ""
    output_video_fps = 0
    frame_blending_mode = []

    # load cfg file
    with open("cfg", "r") as cfg:
        for ln in cfg:
            ln = ln.strip().split()
            if "input_video_directory_path" in ln:
                input_video_directory_path = ln[1]
            elif "output_video_directory_path" in ln:
                output_video_directory_path = ln[1]
            elif "output_video_fps" in ln:
                output_video_fps = int(ln[1])
            elif "frame_blending_mode" in ln:
                frame_blending_mode = ln[1]

    if not Path(input_video_directory_path).is_dir(): return

    for video_file_path in Path(input_video_directory_path).iterdir():
        if video_file_path.is_file() and video_file_path.suffix.lower() in ok_video_extension:
            input_video_fps = cmd.get_video_fps(video_file_path)
            weights = []

            # validate output_video_fps
            while output_video_fps > input_video_fps:
                print(f"output_video_fps ({output_video_fps}) is higher than input_video_fps ({input_video_fps})")
                output_video_fps = int(input(f"output video FPS -> "))

            # configure weights[] before rendering
            for i in range(int(input_video_fps/output_video_fps)):
                weights.append(0)

            if frame_blending_mode == "u": # "uniform"
                weights = weight_preset.uniform(weights)
            elif frame_blending_mode in ["g", "n"]: # "gaussian", "normal"
                sigma = int(frame_blending_mode.split("/")[1])
                weights = weight_preset.gaussian(weights, sigma)
            elif frame_blending_mode == "c": # "custom"
                weights = weight_preset.custom(weights)
            # print(f"Weights: {weights}") # testing

            cmd.render(
                video_file_path,
                output_video_directory_path,
                video_file_path.with_suffix("").name,
                weights,
                output_video_fps
            )

    return

if __name__ == "__main__":
    main()
