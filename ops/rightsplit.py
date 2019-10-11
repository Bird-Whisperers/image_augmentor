from __future__ import division

CODE = 'rightsplit'

class RightSplit:
    def __init__(self):
        self.code = CODE

    def process(self, img):
        height, width, channels = img.shape
        split_point = int(width / 2)
        upper = 0
        return img[upper:height, split_point: width]


    @staticmethod
    def match_code(code):
        if code == CODE:
            return RightSplit()
