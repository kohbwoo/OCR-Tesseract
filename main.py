

import cv2 #OpenCV
from PIL import Image
import pytesseract
import numpy as np
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' #테서렉트 경로 지정

file = r'S.jpg'#변환한 파일 선택
img = cv2.imread(file) #불러올 파일 저장

while True:
    language = int(input("1. English + 한국어\n2. English\n3. 한국어\n4. Number")) #언어 선택
    if language == 1:
        language = 'eng+kor'
        onlyNum = False
        break
    elif language == 2:
        language = 'eng'
        onlyNum = False
        break
    elif language == 3:
        language = 'kor'
        onlyNum = False
        break
    elif language == 4:
        language = 'eng'
        onlyNum = True
        break

    else:
        print("잘못된 입력입니다.")
        continue


h, w, c = img.shape #이미지 행렬로 변환
boxes = pytesseract.image_to_boxes(img) #텍스트로 인식되는 데이터 박스 태깅
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 3)
if onlyNum == True:
    output = (pytesseract.image_to_string(Image.open(file), lang=language, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')) #이미지 -> 문자열 추출, lang 언어설정
else:
    output = (pytesseract.image_to_string(Image.open(file), lang=language))  # 이미지 -> 문자열 추출, lang 언어설정
final_str = output[:-1] #문자열 마지막 텍스트 제거
print(final_str) #출력
cv2.imshow('img', img) #박스 태깅 된 이미지 띄우기



cv2.waitKey(0) #0 입력하여 종료