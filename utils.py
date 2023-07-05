#!/usr/bin/env python3

def resize_from_center(bbox, scale_w, scale_h, scale_both):

    if scale_both:
        scale_h = scale_w

    if scale_w == 0 or scale_h == 0:
        return bbox 

    kw = bbox[2] * scale_w - bbox[2]
    kh = bbox[3] * scale_h - bbox[3]
    
    bbox[0] -= kw / 2
    bbox[1] -= kh / 2
    bbox[2] += kw
    bbox[3] += kh
 
    if bbox[0] < 0:
        bbox[2] += bbox[0]
        bbox[0] = 0

    if bbox[1] < 0:
        bbox[3] += bbox[1]
        bbox[1] = 0

    if bbox[0] + bbox[2] > 1:
        bbox[2] = 1 - bbox[0]

    if bbox[1] + bbox[3] > 1:
        bbox[3] = 1 - bbox[1]

    return bbox
