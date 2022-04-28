import time
import random

print("5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메류를 추천해드려요.")
print("동일한 메뉴는 안돼요!")

menu_list=[]

while True:
    menu = input("메뉴 추가:")
    menu_list.append(menu)

    if len  