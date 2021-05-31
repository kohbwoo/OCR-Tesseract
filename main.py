
from tkinter import filedialog
from tkinter import *
import os
import cv2  # OpenCV
from PIL import Image
import pytesseract


window = Tk()
window.title("Tesseract-OCR")
window.geometry('300x400')
textbox = Entry(window)


def click():
    filename = filedialog.askopenfilename(initialdir=os.getcwd())

    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'  # 테서렉트 경로 지정
    file = filename  # 변환한 파일 선택
    img = cv2.imread(file)  # 불러올 파일 저장
    textbox.insert(0, str(file))

    def btn1():
        img = cv2.imread(textbox.get())
        h, w, c = img.shape  # 이미지 행렬로 변환
        boxes = pytesseract.image_to_boxes(img)  # 텍스트로 인식되는 데이터 박스 태깅
        for b in boxes.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 3)
        output = (pytesseract.image_to_string(Image.open(file), lang='eng+kor'))  # 이미지 -> 문자열 추출, lang 언어설정
        final_str = output[:-1]  # 문자열 마지막 텍스트 제거
        label = Label(window, text=final_str)  # 출력
        label.place(x=50, y=100)
        f = open(os.path.splitext(filename)[0]+".txt", "w")
        f.write(final_str)
        f.close()
        cv2.imshow('img', img)  # 박스 태깅 된 이미지 띄우기

        cv2.waitKey(0)  # 0 입력하여 종료

    def btn2():
        img = cv2.imread(textbox.get())
        h, w, c = img.shape  # 이미지 행렬로 변환
        boxes = pytesseract.image_to_boxes(img)  # 텍스트로 인식되는 데이터 박스 태깅
        for b in boxes.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 3)
        output = (pytesseract.image_to_string(Image.open(file), lang='eng'))  # 이미지 -> 문자열 추출, lang 언어설정
        final_str = output[:-1]  # 문자열 마지막 텍스트 제거
        label = Label(window, text=final_str)  # 출력
        label.place(x=50, y=100)
        f = open(os.path.splitext(filename)[0] + ".txt", "w")
        f.write(final_str)
        f.close()
        cv2.imshow('img', img)  # 박스 태깅 된 이미지 띄우기

        cv2.waitKey(0)  # 0 입력하여 종료

    def btn3():
        img = cv2.imread(textbox.get())
        h, w, c = img.shape  # 이미지 행렬로 변환
        boxes = pytesseract.image_to_boxes(img)  # 텍스트로 인식되는 데이터 박스 태깅
        for b in boxes.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 3)
        output = (pytesseract.image_to_string(Image.open(file), lang='kor'))  # 이미지 -> 문자열 추출, lang 언어설정
        final_str = output[:-1]  # 문자열 마지막 텍스트 제거
        label = Label(window, text=final_str)  # 출력
        label.place(x=50, y=100)
        f = open(os.path.splitext(filename)[0] + ".txt", "w")
        f.write(final_str)
        f.close()
        cv2.imshow('img', img)  # 박스 태깅 된 이미지 띄우기

        cv2.waitKey(0)  # 0 입력하여 종료

    def btn4():
        img = cv2.imread(textbox.get())
        h, w, c = img.shape  # 이미지 행렬로 변환
        boxes = pytesseract.image_to_boxes(img)  # 텍스트로 인식되는 데이터 박스 태깅
        for b in boxes.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 3)
        output = (pytesseract.image_to_string(Image.open(file), lang='eng',
                                                  config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'))  # 이미지 -> 문자열 추출, lang 언어설정
        final_str = output[:-1]  # 문자열 마지막 텍스트 제거
        label = Label(window, text=final_str)  # 출력
        label.place(x=100, y=100)
        f = open(os.path.splitext(filename)[0] + ".txt", "w")
        f.write(final_str)
        f.close()
        cv2.imshow('img', img)  # 박스 태깅 된 이미지 띄우기

        cv2.waitKey(0)  # 0 입력하여 종료


    engkorbtn = Button(window, text="영어+한글", command=btn1)
    engkorbtn.place(x=50, y=60)
    engbtn = Button(window, text="영어", command=btn2)
    engbtn.place(x=120, y=60)
    korbtn = Button(window, text="한글", command=btn3)
    korbtn.place(x=160, y=60)
    numbtn = Button(window, text="숫자", command=btn4)
    numbtn.place(x=200, y=60)

filebtn = Button(window, text="파일선택", command=click)
filebtn.place(x=200, y=26)
textbox.place(x=50, y=30)

window.mainloop()