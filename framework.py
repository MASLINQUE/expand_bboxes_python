#!/usr/bin/env python3

from utils import resize_from_center

class FrameWorker():
    
    def __init__(self) -> None:
        pass

    def frame_processing(self, frame, sw, sh, sb):

        items = frame.get('items')

        if len(items) == 0:

            return frame

        for item in items:
            bbox = item.get('bbox')
            bbox_new = resize_from_center(bbox, sw, sh, sb)
            
            item['bbox'] = bbox_new

        frame['items'] = items

        return frame



