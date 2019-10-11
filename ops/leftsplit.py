from __future__ import division

CODE = 'leftsplit'

class LeftSplit:
    def __init__(self):
        self.code = CODE

    def process(self, img):
        height, width, channels = img.shape
        split_point = int(width / 2)
        left = 0
        upper = 0

        return img[upper:height, left: split_point]


    @staticmethod
    def match_code(code):
        if code == CODE:
            return LeftSplit()
