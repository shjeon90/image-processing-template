import cv2
import qimage2ndarray
from utils import *
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap, QPainter
from IpShape import *

class IpImageProcess:
    def __init__(self, *args, **kwargs):
        self.parent = args[0]

    def clear(self):
        self.parent.clear()
        self.parent.img = self.parent.img_orig.copy()
        self.parent.update()

    def get_gray_alpha(self):
        img_orig = self.parent.img_orig.toImage()
        img_orig_rec = qimage2ndarray.recarray_view(img_orig)
        img_orig_nd = recarray_to_ndarray(img_orig_rec)
        img_orig_nd = img_orig_nd

        alpha = img_orig_nd[:, :, -1].astype(np.uint8)
        img_gray = np.mean(img_orig_nd[:, :, :-1], -1).astype(np.uint8)

        # return img_orig_nd
        return img_gray, alpha

    def do_postprocess(self, img, alpha):
        img = img.astype(np.uint8)
        img_rgb = gray_to_rgb(img)
        img_rgba = np.concatenate((
            img_rgb, alpha[..., np.newaxis]
        ), -1)

        self.parent.img = QPixmap.fromImage(qimage2ndarray.array2qimage(img_rgba, normalize=False))
        self.parent.update()

    def do_postprocess_mark(self, coords):
        for coord in coords:
            ellipse = IpEllipse()
            ellipse.init(QPoint(coord[0]-5, coord[1]-5))
            ellipse.update(QPoint(coord[0]+5, coord[1]+5))

            self.parent.shape_list.append(ellipse)
        self.parent.update()

    def set_threshold(self, thr):
        pass


    def set_hist(self):
        pass

    def set_gaussian_filter(self):
        pass

    def set_laplacian_filter(self):
        pass

    def set_bilateral_filter(self):
        pass

    def scale_image(self, p):
        pass

    def rotate_image(self, r):
        pass

    def reflect_image(self):
        pass

    def perspective_transformation(self, perspective_pts):
        pass

    def harris_corner_detect(self):
        pass

    def fast_feature_detect(self):
        pass

    def blob_detect(self):
        pass

    def orb_descriptor(self):
        pass

    def feature_match(self, img_temp):
        pass