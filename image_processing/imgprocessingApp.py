import cv2
import numpy as np
import sys
import os
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
from PIL import Image
from numpy import sqrt
from PyQt5 import QtCore,QtGui
from PIL import Image,ImageFilter

class Imgprocess(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.aboutus = QLabel("Berke Sayın 30719074",self)
        self.openfile = QPushButton("Dosya Aç")
        self.save_file = QPushButton("Kaydet")
        #self.image=QLabel()
        self.aboutus.setFont(QFont("Times",10))
        self.aboutus.setStyleSheet("border: 1px solid black;")
        self.aboutus.setAlignment(QtCore.Qt.AlignCenter)

        #self.image.setPixmap(QtGui.QPixmap("ip_illustration.png"))


        v_box = QVBoxLayout()

        v_box.addWidget(self.aboutus)
        v_box.addStretch()
        """v_box.addWidget(self.image)
        v_box.addStretch()"""
        v_box.addWidget(self.openfile)
        v_box.addWidget(self.save_file)
        self.setLayout(v_box)

        self.openfile.clicked.connect(self.file_open)
        self.save_file.clicked.connect(self.savefile)
        self.save = None
    def file_open(self):
        dosya_ismi = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(dosya_ismi[0])
        img = cv2.resize(img, (500, 500))
        cv2.imshow("Orjinal image", img)

    def savefile(self):
        fname, filter = QFileDialog.getSaveFileName(None, 'Save File', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img=cv2.resize(fname,(100,100))
        cv2.imwrite(img, self.save)

    def rotate_right(self):
        # opening the image
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (500, 500))
        cv2.imshow("Original Image", img)

        h = img.shape[0]  # height of the image
        w = img.shape[1]  # width of the image
        c = img.shape[2]  # number of channel
        newImg = np.zeros((w, h, c), dtype=np.uint8)  # creating new 3d array

        # using 3 foor loop for rotating the image to the right side
        for i in range(w - 1):
            for j in range(h - 1):
                for k in range(c):
                    # channel is same but values of the w and h changing
                    newImg[i, j, k] = img[h - j - 1, i, k]

        cv2.imshow("Right rotated image", newImg)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def rotate_left(self):
        # opening the image
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (500, 500))
        cv2.imshow("Original Image", img)
        h = img.shape[0]
        w = img.shape[1]
        c = img.shape[2]
        newImg = np.zeros((w, h, c), dtype=np.uint8)

        for i in range(w - 1):
            for j in range(h - 1):
                for k in range(c):
                    newImg[i, j, k] = img[j, h - i - 1, k]

        cv2.imshow("Left rotated image", newImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def reflect(self): #quite similar with left and right rotation
        # opening the image
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (500, 500))
        cv2.imshow("Original Image", img)
        h = img.shape[0]
        w = img.shape[1]
        c = img.shape[2]
        newImg = np.zeros((h, w, c), dtype=np.uint8)

        for i in range(h - 1):
            for j in range(w - 1):
                for k in range(c):
                    newImg[i, j, k] = img[i, w - j - 1, k]

        cv2.imshow("Reflected image", newImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def take_negative(self):
        # opening the image
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (500, 500))
        cv2.imshow("Original Image", img)
        negative_img = 255 - img

        cv2.imshow("Negative image", negative_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def grayScale(self):
        # opening the image
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (500, 500))
        red = img[:, :, 0]
        green = img[:, :, 1]
        blue = img[:, :, 2]

        imgGray = 0.2989 * red + 0.5870 * green + 0.1140 * blue
        plt.imshow(imgGray, cmap='gray')
        plt.show()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def HistGraph(self):

        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (500, 500))
        cv2.imshow("Original Image", img)
        cv2.waitKey(0)

        red = np.zeros((256), dtype=int)
        green = np.zeros((256), dtype=int)
        blue = np.zeros((256), dtype=int)
        I = np.zeros((256), dtype=int)
        k = 0
        while k < 256:
            red[k] = np.count_nonzero(img[:, :, 2] == k)
            green[k] = np.count_nonzero(img[:, :, 1] == k)
            blue[k] = np.count_nonzero(img[:, :, 0] == k)
            I[k] = np.count_nonzero(img == k)
            k = k + 1
        intensity = np.arange(0, 256, 1)

        plt.figure(figsize=(12, 7))
        plt.subplot(221)
        plt.bar(intensity, red, color="red", width=0.5)
        # plt.xlabel("intensity")
        plt.ylabel("frequency")
        plt.title("RED")
        plt.subplot(222)
        plt.bar(intensity, green, color="green", width=0.5)
        # plt.xlabel("intensity")
        plt.ylabel("frequency")
        plt.title("GREEN")

        plt.subplot(223)
        plt.bar(intensity, blue, color="blue", width=0.5)
        plt.xlabel("intensity")
        plt.ylabel("frequency")
        plt.title("BLUE")

        plt.subplot(224)
        plt.bar(intensity, I, color="black", width=0.5)
        plt.xlabel("intensity")
        plt.ylabel("frequency")
        plt.title("Intensity")

        plt.suptitle("Histogram")
        plt.show()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def HistogramEqualization(self):
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0],0)
        img = cv2.resize(img, (500, 500))
        cv2.imshow("Original Image", img)

        cv2.waitKey(0)

        normal = np.zeros((256,), dtype=np.float16)

        h, w = img.shape

        for i in range(h):
            for j in range(w):
                g = img[i, j]
                normal[g] = normal[g] + 1


        tmp = 1.0 / (h * w)
        heq = np.zeros((256,), dtype=np.float16)

        for i in range(256):
            for j in range(i + 1):
                heq[i] += normal[j] * tmp;
            heq[i] = round(heq[i] * 255);

        heq = heq.astype(np.uint8)

        for i in range(h):
            for j in range(w):
                g = img[i, j]
                img[i, j] = heq[g]

        cv2.imshow('Histogram Equalization', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def derivative(self):
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (640,480))
        cv2.imshow("Original Image", img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        height, width = img.shape

        """cv2.imshow("orjinal", img)"""

        newImg = np.zeros_like(img)

        print(file_name)
        object_name = file_name[0].split("/")
        print(object_name[-1])

        for i in range(0, height - 2):
            for j in range(0, width - 2):
                Gy = (-1) * img[i, j] + (-2) * img[i, j + 1] + (-1) * img[i, j + 2] + 1 * img[i + 2, j] + 2 * img[
                    i + 2, j + 1] + 1 * img[i + 2, j + 2]
                Gx = (-1) * img[i, j] + (-2) * img[i + 1, j] + (-1) * img[i + 2, j] + 1 * img[i, j + 2] + 2 * img[
                    i + 1, j + 2] + 1 * img[i + 2, j + 2]
                G = sqrt(Gx ** 2 + Gy ** 2)
                newImg[i + 1, j + 1] = G

        the_path = "C:\\Users\\berke.sayin\\PycharmProjects\\pythonProject1\\images\\derivative-img\\derivative_" + object_name[-1]
        print(the_path)

        cv2.imwrite(the_path, newImg)
        newImg = cv2.imread(the_path)

        cv2.imshow("Derivative Sobel2", newImg)
        cv2.imshow("Derivative Sobel", img)
        self.save = newImg
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def LowPass(self):
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (640, 480))
        cv2.imshow("Original Image", img)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #taking image shapes
        img_h = img.shape[0]
        img_w = img.shape[1]

        #creating kernel
        kernel = np.ones((7,7))
        kernel_h = kernel.shape[0]
        kernel_w = kernel.shape[1]
        kernelsize = kernel_h*kernel_w

        #new matrix for zero padding
        new_h = img_h+kernel_h-1
        new_w = img_w+kernel_w-1

        zeropadding=np.zeros((new_h,new_w))
        newimage = np.zeros(((img_h,img_w)))

        #zero padding procces
        for i in range(img_h):
            for j in range(img_w):
                zeropadding[i+3, j+3]=img[i,j] #the number that we use is depending on kernel size

        #low pass filter with 4 for loops
        for i in range(img_h):
            for j in range(img_w):
                total = 0
                for k in range(i, i+kernel_h):
                    for l in range(j, j+kernel_w):
                        total = total + zeropadding[k,l]
                newimage[i, j] = round(total*1 / kernelsize, 1)

        #image output
        plt.imshow(newimage, cmap='gray')
        self.save = newimage
        plt.show()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def HighPass(self):
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (640, 480))
        cv2.imshow("Original Image", img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        height = img.shape[0]
        width = img.shape[1]

        # iki adet kenar sayıları birer arttırılmış boş arraylar
        padding_img = np.zeros((height + 2, width + 2))
        newimg = np.zeros((height + 2, width + 2))

        # Zero padding işlemi
        for i in range(height):
            for j in range(width):
                padding_img[i + 1, j + 1] = img[i, j]

        # kernel işlemi
        for i in range(height):
            for j in range(width):
                total = ((-1) * padding_img[i, j] + (-1) * padding_img[i, j + 1] + (-1) * padding_img[i, j + 2] +
                     (-1) * padding_img[i + 1, j] + (9) * padding_img[i + 1, j + 1] + (-1) * padding_img[i + 1, j + 2] +
                     (-1) * padding_img[i + 2, j] + (-1) * padding_img[i + 2, j + 1] + (-1) * padding_img[i + 2, j + 2]
                     )
                if total <= 0:
                    total = 0
                    newimg[i + 1, j + 1] = round(total * 1 / 9, 1)
                else:
                    newimg[i + 1, j + 1] = round(total * 1 / 9, 1)

        # resim çıktısı
        plt.imshow(newimg, cmap='gray')
        self.save = newimg
        plt.show()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def otsu_Threshold(self):
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (640, 480))
        cv2.imshow("Original Image", img)

        image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        hist = cv2.calcHist([image_gray], [0], None, [255], [0, 255])
        # print(hist)

        within = []
        for i in range(len(hist)):
            x, y = np.split(hist, [i])
            x1 = np.sum(x) / img.shape[0] * img.shape[1]
            y1 = np.sum(y) / img.shape[0] * img.shape[1]

            x2 = np.sum([j * t for j, t in enumerate(x)]) / np.sum(x)
            y2 = np.sum([j * t for j, t in enumerate(y)]) / np.sum(y)

            x3 = np.sum([(j - x2) ** 2 * t for j, t in enumerate(x)]) / np.sum(x)
            x3 = np.nan_to_num(x3)
            y3 = np.sum([(j - y2) ** 2 * t for j, t in enumerate(y)]) / np.sum(y)
            within.append(x1 * x3 + y1 * y3)
        m = np.argmin(within)

        (tresh, Bin) = cv2.threshold(image_gray, m, 255, cv2.THRESH_BINARY)

        cv2.imshow("Binary", Bin)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def erosion_(self):
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (640, 480))
        cv2.imshow("original", img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (thresh, bin) = cv2.threshold(gray, 177, 255, cv2.THRESH_BINARY)

        filtre = np.ones((7, 7))
        S = bin.shape
        F = filtre.shape

        bin = bin / 255

        R = S[0] + F[0] - 1
        C = S[1] + F[1] - 1

        N = np.zeros((R, C))

        for i in range(S[0]):
            for j in range(S[1]):
                N[i + 1, j + 1] = bin[i, j]

        for i in range(S[0]):
            for j in range(S[1]):
                k = N[i:i + F[0], j:j + F[1]]
                result = (k == filtre)
                final = np.all(result == True)  # all yerine any
                if final:
                    bin[i, j] = 1
                else:
                    bin[i, j] = 0
        cv2.imshow("erosion", bin)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def dilation_(self):
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (640, 480))
        cv2.imshow("Original Image", img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (thresh, bin) = cv2.threshold(gray, 177, 255, cv2.THRESH_BINARY)

        filtre = np.ones((7, 7))
        S = bin.shape
        F = filtre.shape

        bin = bin / 255

        R = S[0] + F[0] - 1
        C = S[1] + F[1] - 1

        N = np.zeros((R, C))

        for i in range(S[0]):
            for j in range(S[1]):
                N[i + 1, j + 1] = bin[i, j]

        for i in range(S[0]):
            for j in range(S[1]):
                k = N[i:i + F[0], j:j + F[1]]
                result = (k == filtre)
                final = np.any(result == True)  # all yerine any
                if final:
                    bin[i, j] = 1
                else:
                    bin[i, j] = 0
        cv2.imshow("dilation", bin)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def opening_closing(self):
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        orginal_img = cv2.imread(file_name[0])
        orginal_img = cv2.resize(orginal_img, (640, 480))
        cv2.imshow("Original Image", orginal_img)

        gray = cv2.cvtColor(orginal_img, cv2.COLOR_BGR2GRAY)
        (thresh, bin) = cv2.threshold(gray, 177, 255, cv2.THRESH_BINARY)

        filtre = np.ones((7, 7))

        def erosion(img, filtre):

            S = img.shape
            F = filtre.shape

            img = img / 255

            R = S[0] + F[0] - 1
            C = S[1] + F[1] - 1
            N = np.zeros((R, C))
            for i in range(S[0]):
                for j in range(S[1]):
                    N[i + 1, j + 1] = img[i, j]

            for i in range(S[0]):
                for j in range(S[1]):
                    k = N[i:i + F[0], j:j + F[1]]
                    result = (k == filtre)
                    final = np.all(result == True)  # all yerine any
                    if final:
                        img[i, j] = 1
                    else:
                        img[i, j] = 0
            return img * 255

        def dilation(img, filtre):

            S = img.shape
            F = filtre.shape

            img = img / 255

            R = S[0] + F[0] - 1
            C = S[1] + F[1] - 1
            N = np.zeros((R, C))
            for i in range(S[0]):
                for j in range(S[1]):
                    N[i + 1, j + 1] = img[i, j]

            for i in range(S[0]):
                for j in range(S[1]):
                    k = N[i:i + F[0], j:j + F[1]]
                    result = (k == filtre)
                    final = np.any(result == True)  # all yerine any
                    if final:
                        img[i, j] = 1
                    else:
                        img[i, j] = 0
            return img * 255

        opening1 = erosion(bin, filtre)
        opening2 = dilation(opening1, filtre)
        cv2.imshow("opening", opening2)

        closing1 = dilation(bin, filtre)
        closing2 = erosion(closing1, filtre)
        cv2.imshow("closing", closing2)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def boundry_Extraction(self):
        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (640, 480))
        cv2.imshow("Original Image", img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (thresh, bin) = cv2.threshold(gray, 177, 255, cv2.THRESH_BINARY)

        filtre = np.ones((7, 7))
        image = bin.shape
        F = filtre.shape

        bin_org = bin
        bin = bin / 255
        bin_org = bin_org / 255
        # zero padding
        R = image[0] + F[0] - 1
        C = image[1] + F[1] - 1

        New = np.zeros((R, C))

        for i in range(image[0]):
            for j in range(image[1]):
                New[i + 1, j + 1] = bin[i, j]

        for i in range(image[0]):
            for j in range(image[1]):
                k = New[i:i + F[0], j:j + F[1]]
                result = (k == filtre)
                final = np.all(result == True)
                if final:
                    bin[i, j] = 1
                else:
                    bin[i, j] = 0

        boundry = np.zeros((image[0], image[1]))

        for i in range(image[0]):
            for j in range(image[1]):
                boundry[i, j] = bin_org[i, j] - bin[i, j]

        cv2.imshow("Erosion", bin)
        cv2.imshow("Boundry Extraction", boundry)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def gamaLog(self):
        pencere2.show()

class Pencere2(QWidget):
    def __init__(self):
        super().__init__()
        self.page2()

    def page2(self):
        self.setWindowTitle("Log And Gama Corrections")
        self.setGeometry(100, 100, 100, 100)
        self.label = QLabel("Logaritma dönüşümü için log tabanı girin:")
        self.textbox = QLineEdit()
        self.logcalculate = QPushButton("Hesapla")
        self.label2 = QLabel("Kuvvet dönüşümü için gama değerini girin:")
        self.textbox2 = QLineEdit()
        self.powcalculate = QPushButton("Hesapla")

        v_box=QVBoxLayout()
        h_box=QHBoxLayout()
        h_box.addWidget(self.label)
        h_box.addWidget(self.textbox)
        h_box.addWidget(self.logcalculate)
        v_box.addStretch()

        h_box2=QHBoxLayout()
        h_box2.addWidget(self.label2)
        h_box2.addWidget(self.textbox2)
        h_box2.addWidget(self.powcalculate)

        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)

        self.setLayout(v_box)

        self.logcalculate.clicked.connect(self.logCorrection)
        self.powcalculate.clicked.connect(self.power)


    def getLogValue(self):
        return float(self.textbox.text())
    def logCorrection(self):
        x = self.getLogValue()

        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        image = cv2.imread(file_name[0])
        image = cv2.resize(image, (640, 480))
        cv2.imshow("Original Image", image)

        c = 255 / np.log1p(np.max(image))
        log_image = c * (np.log1p(image)) / (np.log1p(x))

        log_image = np.array(log_image, dtype=np.uint8)

        cv2.imshow("Log Correction", log_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def getPowValue(self):
        return float(self.textbox2.text())
    def power(self):
        gama = self.getPowValue()

        def gammaCorrection(src, gamma):
            table = [((i / 255) ** gamma) * 255 for i in range(256)]
            table = np.array(table, np.uint8)

            return cv2.LUT(src, table)

        file_name = QFileDialog.getOpenFileName(None, 'File Name', os.getenv("HOME"), filter='(*.png *.jpeg *.jpg)')
        img = cv2.imread(file_name[0])
        img = cv2.resize(img, (640, 480))
        cv2.imshow("Original Image", img)

        gammaImg = gammaCorrection(img, gama)

        # cv2.imshow('Original', img)
        cv2.imshow('Gama Correction', gammaImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pencere = Imgprocess()

        self.setCentralWidget(self.pencere)

        self.menus()

    def menus(self):
        menubar = self.menuBar()
        file = menubar.addMenu("Menu-1")
        file2 = menubar.addMenu("Menu-2")
        file3 = menubar.addMenu("Menu-3")
        file4=menubar.addMenu("Menu-4")

        rotateRight = QAction("Sağa döndür", self)
        rotateLeft = QAction("Sola döndür", self)
        reflection = QAction("Yansıma", self)
        negative = QAction("Negatif Al", self)
        powerlog=QAction("Power/Log Correction",self)

        grayscale = QAction("Gray Scale", self)
        histgraph = QAction("Histogram Grafigi",self)
        histequalization = QAction("Histogram Esitleme",self)

        derivativefilt=QAction("Türev",self)
        lowpassfilter=QAction("Alçak Geçiren",self)
        highpassfilter=QAction("Yüksek Geçiren",self)

        otsuthresh=QAction("Otsu Threshold",self)
        erosion=QAction("Erosion",self)
        dilation=QAction("Dilation",self)
        open_close=QAction("Opening/Closing",self)
        boundryextraction=QAction("Boundry Extraction",self)




        file.addAction(rotateRight)
        file.addAction(rotateLeft)
        file.addAction(reflection)
        file.addAction(negative)
        file.addAction(powerlog)

        file2.addAction(grayscale)
        file2.addAction(histgraph)
        file2.addAction(histequalization)

        file3.addAction(derivativefilt)
        file3.addAction(lowpassfilter)
        file3.addAction(highpassfilter)

        file4.addAction(otsuthresh)
        file4.addAction(erosion)
        file4.addAction(dilation)
        file4.addAction(open_close)
        file4.addAction(boundryextraction)


        self.setGeometry(150, 150, 300, 300)
        self.setStyleSheet("background:QColor(200,100,150);")
        self.setWindowTitle("İmage Processing App")
        self.setWindowIcon(QtGui.QIcon('muz.png'))
        self.show()

        file.triggered.connect(self.response)
        file2.triggered.connect(self.response)
        file3.triggered.connect(self.response)
        file4.triggered.connect(self.response)

    def response(self, action):
        if action.text() == "Sağa döndür":
            self.pencere.rotate_right()
        elif action.text() == "Sola döndür":
            self.pencere.rotate_left()
        elif action.text() == "Yansıma":
            self.pencere.reflect()
        elif action.text() == "Negatif Al":
            self.pencere.take_negative()
        elif action.text() == "Power/Log Correction":
            self.pencere.gamaLog()
        elif action.text() == "Gray Scale":
            self.pencere.grayScale()
        elif action.text() == "Histogram Grafigi":
            self.pencere.HistGraph()
        elif action.text() == "Histogram Esitleme":
            self.pencere.HistogramEqualization()
        elif action.text() == "Türev":
            self.pencere.derivative()
        elif action.text() == "Alçak Geçiren":
            self.pencere.LowPass()
        elif action.text() == "Yüksek Geçiren":
            self.pencere.HighPass()
        elif action.text() == "Otsu Threshold":
            self.pencere.otsu_Threshold()
        elif action.text() == "Erosion":
            self.pencere.erosion_()
        elif action.text() == "Dilation":
            self.pencere.dilation_()
        elif action.text() == "Opening/Closing":
            self.pencere.opening_closing()
        elif action.text() == "Boundry Extraction":
            self.pencere.boundry_Extraction()



app = QApplication(sys.argv)
pencere2 = Pencere2()
menu = Menu()

sys.exit(app.exec_())
