#!/usr/bin/env python3

def resize_from_center(bbox, scale_w, scale_h, scale_both):

	if scale_both:
		scale_w = scale_h

	if scale_w == 0 or scale_h == 0:
		return bbox

	w = bbox[2]
	h = bbox[3]

	dx = scale_w * w
	dy = scale_h * h
	xc = bbox[0] + w/2
	yc = bbox[1] + h/2

	bbox_new = [0] * 4

	bbox_new[0] = round(max(xc-dx/2, 0), 3)

	bbox_new[1] = round(max(yc-dy/2, 0), 3)
	# x_max = round(min(xc+dx, 1), 3)
	# y_max = round(min(yc+dy, 1), 3)
	bbox_new[2] = round(min(dx, 1), 3)
	bbox_new[3] = round(min(dy, 1), 3)

	return bbox_new