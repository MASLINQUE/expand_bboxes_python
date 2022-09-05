#!/usr/bin/env python3

def resize_from_center(bbox, scale_w, scale_h, scale_both):

	if scale_both:
		scale_h = scale_w

	if scale_w == 0 or scale_h == 0:
		return bbox

	wim = bbox[2]
	him = bbox[3]

	dx = scale_w * wim
	dy = scale_h * him
	
	xc = bbox[0] + wim/2
	yc = bbox[1] + him/2


	x = round(max(xc-dx/2, 0), 3)
	y = round(max(yc-dy/2, 0), 3)
	w = round(min(dx, 1), 3)
	h = round(min(dy, 1), 3)

	return [x,y,w,h]