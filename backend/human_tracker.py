from supervision.geometry.dataclasses import Point
from supervision.tools.line_counter import LineCounter
from supervision.video.source import get_video_frames_generator
from supervision.video.sink import VideoSink
from supervision.video.dataclasses import VideoInfo
from ultralytics import YOLO

# load model
model = YOLO(MODEL_PATH)
model.fuse()

# predict
detections = model(frame)


video_info = VideoInfo.from_video_path(SOURCE_VIDEO_PATH)

generator = get_video_frames_generator(SOURCE_VIDEO_PATH)

with VideoSink(TARGET_VIDEO_PATH, video_info) as sink:
    for frame in tqdm(generator, total=video_info.total_frames):
        frame = ...
        sink.write_frame(frame)


LINE_START = Point(50, 1500)
LINE_END = Point(3790, 1500)

line_counter = LineCounter(start=LINE_START, end=LINE_END)

for frame in frames:
    detections = ...
    line_counter.update(detections=detections)
