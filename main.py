import cv2
from PIL import Image
import pytesseract
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' #테서렉트 경로 지정
img = cv2.imread('Sample\Kor\Timetable.png') # 불러올 파일 지정 -> img 에 저장

language = int(input("1. English\n2. korean")) #언어 선택 (한+영 혼합 기능 추가필!!)
if language == 1:
    language = 'eng'
elif language == 2:
    language = 'kor'

prossess = int(input("1. 원본\n2. 흑백\n")) #원본 / 그레이스케일 선 택
if prossess == 1:
    h, w, c = img.shape #이미지 행렬로 변환
    boxes = pytesseract.image_to_boxes(img) #텍스트로 인식되는 데이터 박스 태깅
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 1)
    output = (pytesseract.image_to_string(Image.open('Sample\Kor\Timetable.png'), lang=language)) #이미지 -> 문자열 추출, lang 언어설정
    final_str = output[:-1] #문자열 마지막 텍스트 제거
    print(final_str) #출력
    cv2.imshow('img', img) #박스 태깅 된 이미지 띄우기
elif prossess == 2:
    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('Sample\Gray\Gray.png', im_gray)
    h, w, c = img.shape  # 이미지 행렬로 변환
    boxes = pytesseract.image_to_boxes(im_gray)  # 텍스트로 인식되는 데이터 박스 태깅
    for b in boxes.splitlines():
        b = b.split(' ')
        im_gray = cv2.rectangle(im_gray, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 1)
    output = (pytesseract.image_to_string(im_gray, lang=language)) # 이미지 -> 문자열 추출, lang 언어설정
    final_str = output[:-1]  # 문자열 마지막 텍스트 제거
    print(final_str)  # 출력
    cv2.imshow('img', im_gray)  # 박스 태깅 된 이미지 띄우기

cv2.waitKey(0) #0 입력하여 종료