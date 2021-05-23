import cv2
from PIL import Image
import pytesseract
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' #테서렉트 경로 지정
img = cv2.imread('Sample\H123.png') # 불러올 파일 지정 -> img 에 저장

h, w, c = img.shape #이미지 행렬로 변환

boxes = pytesseract.image_to_boxes(img) #텍스트로 인식되는 데이터 박스 태깅
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 1)


output = (pytesseract.image_to_string(Image.open('Sample\H123.png'), lang='eng+kor')) #이미지 -> 문자열 추출, lang 언어설정

final_str = output[:-1] #문자열 마지막 텍스트 제거
print(final_str) #출력

cv2.imshow('img', img) #박스 태깅 된 이미지 띄우기
cv2.waitKey(0) #0 입력하여 종료