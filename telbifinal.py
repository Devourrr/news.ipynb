# telbi 큰 카테 고리 4가지
#음식 운동 날씨 뉴스
#6월 2일 할꺼 
#음성파일 저장 오류, 스케줄 짜기
#쓰레드 넣기 현재 오류 쓰레드안에 키보드 구현하는거
#음식에 driver.quit 넣기 부분 부분 마다
#6월 3일 
from gtts import gTTS
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
    updater,
)
import telebot # pip install pyTelegramBotAPI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import time
from PIL import Image
import schedule   #pip install schedule
import telegram
import threading
import random
from gtts import gTTS #pip install gTTS
import pyautogui #pip install pyautogui

first_Click = pyautogui.locateCenterOnScreen('dnbt.PNG')
second_Click = pyautogui.locateCenterOnScreen('plbt.PNG')

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
TOKEN = "1795391045:AAFsmAKo_ResztkMR96grDLq-Ftyf1luPmY"
bot = telebot.TeleBot(TOKEN)
now = time.localtime()
chat_id = 1756656744
result = ""

opts = webdriver.ChromeOptions()
opts.add_argument('window-size=960,750')

CATEGORY = range(1)

EXERCISE,MEAL,NEWS,WEATHER,CARDIOEXERCISE,WEIGHTTRAINING,KOREA,JAPAN,USA,CHINA,CORONA,STOCK,REALESTATE,VIRTUALCURRENCY = range(14)

def start(update:Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s  started the conversation.", user.first_name)
    keyboard = [
        [
            InlineKeyboardButton("1.운동", callback_data=str(EXERCISE)),
            InlineKeyboardButton("2.식사", callback_data=str(MEAL)),
            InlineKeyboardButton("3.뉴스", callback_data=str(NEWS)),
            InlineKeyboardButton("4.날씨", callback_data=str(WEATHER)),
            
            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "안녕하세요 텔비입니다." + "원하시는걸 선택해주세요!", reply_markup=reply_markup
        )
    return CATEGORY

def exercise(update:Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("유산소 운동", callback_data=str(CARDIOEXERCISE)),
            InlineKeyboardButton("무산소 운동", callback_data=str(WEIGHTTRAINING)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="어떤 운동 하시겠어요?", reply_markup=reply_markup)
    return CATEGORY

def cardioexercise(update:Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="유산소 운동을 안내해드립니다.")
    driver = webdriver.Chrome('chromedriver.exe')
    engine = pyttsx3.init()
    cardio= ['점핑잭', '버피 테스트', '계단 오르기','스트레칭','걷기', '조깅', '달리기', '자전거']
    health_result = random.choice(cardio)
    # bot.send_message(chat_id, health_result)
    if health_result == cardio[0]:
        driver.get(f'https://www.google.com/search?q={cardio[0]} 효과')
        jump = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/ul').text
        jm_info = f'실내에서 할 수 있는 유산소 운동 중 {health_result}을 추천합니다. 점핑잭 운동효과, {jump}'
        tts = gTTS(jm_info, lang='ko')
        tts.save("jm_info.ogg")
        audio = open("jm_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, jm_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)

    elif health_result == cardio[1]:
        driver.get(f'https://www.google.com/search?q={cardio[1]} 효과')
        buf = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        bf_info = f'실내에서 할 수 있는 유산소 운동 중  {health_result}를 추천합니다. 버피테스트 운동효과, {buf}'
        tts = gTTS(bf_info, lang='ko')
        tts.save("bf_info.ogg")
        audio = open("bf_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, bf_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)

    elif health_result == cardio[2]:
        driver.get(f'https://www.google.com/search?q={cardio[2]} 효과')
        stair = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div[2]/ul').text
        str_info = '실내에서 할 수 있는 유산소 운동 중  {health_result}를 추천합니다. 계단 오르기 운동효과, {stair}'
        tts = gTTS(str_info, lang='ko')
        tts.save("str_info.ogg")
        audio = open("str_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, str_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)

    elif health_result == cardio[3]:
        driver.get(f'https://www.google.com/search?q={cardio[3]} 효과')
        strch =driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[1]/div/span[1]/span').text
        sr_info = f'실내에서 할 수 있는 유산소 운동  {health_result}을 추천합니다. 스트레칭 운동 효과, {strch}'
        tts = gTTS(sr_info, lang='ko')
        tts.save("sr_info.ogg")
        audio = open("sr_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, sr_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)

        
    elif health_result == cardio[4]:
        driver.get(f'https://www.google.com/search?q={cardio[4]} 효과')
        walk = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div[2]/ul').text
        wk_info = f'야외에서 할 수 있는 유산소 운동 중 {health_result}운동을 추천합니다. 걷기 운동 효과 {walk}'
        tts = gTTS(wk_info, lang='ko')
        tts.save("wk_info.ogg")
        audio = open("wk_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, wk_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)
        
    elif health_result == cardio[5]:
        driver.get(f'https://www.google.com/search?q={cardio[5]} 효과')
        jog = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div[2]/ul').text
        jg_info = f'야외에서 할 수 있는 유산소 운동 중 {health_result}을 추천합니다. 조깅 운동효과, {jog}'
        tts = gTTS(jg_info, lang='ko')
        tts.save("jg_info.ogg")
        audio = open("jg_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, jg_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)
        
    elif health_result == cardio[6]:
        driver.get(f'https://www.google.com/search?q={cardio[6]} 효과')
        run = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[1]/div/span[1]/span').text
        rn_info = f'야외에서 할 수 있는 유산소 운동 중 {health_result}를 추천합니다. 달리기 운동 효과, {run}'
        tts = gTTS(rn_info, lang='ko')
        tts.save("rn_info.ogg")
        audio = open("rn_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, rn_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)

    elif health_result == cardio[7]:
        driver.get(f'https://www.google.com/search?q={cardio[7]} 효과')
        bic = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div[2]/ul').text
        bc_info = f' 야외에서 할 수 있는 유산소 운동 중 {health_result}운동을 추천합니다. 자전거 운동 효과. {bic}'
        tts = gTTS(bc_info, lang='ko')
        tts.save("bc_info.ogg")
        audio = open("bc_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, bc_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)
    
    return ConversationHandler.END

def weighttraining(update:Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    driver = webdriver.Chrome('chromedriver.exe')
    engine = pyttsx3.init()
    query.edit_message_text(text="무산소 운동을 안내해드립니다.")
    weight = ['팔굽혀펴기','윗몸일으키기','턱걸이','플랭크','벤치프레스','데드리프트','스쿼트','밀리터리프레스'] 
    #  무산소 실내4야외4
    
    health_result = random.choice(weight)
    if health_result == weight[0]:
        driver.get(f'https://www.google.com/search?q={anaerobic[0]} 효과')
        pus = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div[2]/ul').text
        pu_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다. 팔굽혀펴기 운동 효과, {pus}' 
        tts = gTTS(pu_info, lang='ko')
        tts.save("pu_info.ogg")
        audio = open("pu_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, pu_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)

    elif health_result == weight[1]:
        driver.get(f'https://www.google.com/search?q={weight[1]} 효과')
        stup = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        st_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다. 윗몸일으키기 운동 효과, {stup}'
        tts = gTTS(st_info, lang='ko')
        tts.save("st_info.ogg")
        audio = open("st_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, st_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)

    elif health_result == weight[2]:
        driver.get(f'https://www.google.com/search?q={weight[2]} 효과')
        pul = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        pl_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다. 턱걸이 운동 효과, {pul}'
        tts = gTTS(pl_info, lang='ko')
        tts.save("[pl_info.ogg")
        audio = open("pl_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, pl_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)

    elif health_result == weight[3]:
        driver.get(f'https://www.google.com/search?q={weight[3]} 효과')
        plk = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        plk_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다. 플랭크 운동 효과, {plk}'
        tts = gTTS(plk_info, lang='ko')
        tts.save("plk_info.ogg")
        audio = open("plk_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, plk_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)


    elif health_result == weight[4]:
        driver.get(f'https://www.google.com/search?q={weight[4]} 효과')
        bnp = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        bp_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다. 벤치 프레스 운동 효과, {bnp}'
        tts = gTTS(bp_info, lang='ko')
        tts.save("bp_info.ogg")
        audio = open("bp_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, bp_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)

    elif health_result == weight[5]:
        driver.get(f'https://www.google.com/search?q={weight[5]} 효과')
        dlft = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        dl_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다. 데드리프트 운동 효과, {dlft}'
        tts = gTTS(dl_info, lang='ko')
        tts.save("dl_info.ogg")
        audio = open("dl_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, dl_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)

    elif health_result == weight[6]:
        driver.get(f'https://www.google.com/search?q={weight[6]} 효과')
        squ =driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        sq_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다. 스쿼트 운동 효과, {squ}'
        tts = gTTS(sq_info, lang='ko')
        tts.save("sq_info.ogg")
        audio = open("sq_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, sq_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)

    else:
        driver.get(f'https://www.google.com/search?q={weight[7]} 효과')
        mlp = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        mp_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다. 밀리터리 프레스 운동 효과, {mlp}'
        tts = gTTS(mp_info, lang='ko')
        tts.save("mp_info.ogg")
        audio = open("mp_info.ogg", 'rb')
        time.sleep(0.5)
        driver.quit()
        bot.send_message(chat_id, mp_info)
        bot.send_audio(chat_id, audio=audio)
        pyautogui.click(second_Click)
    return ConversationHandler.END


def meal(update:Update,_: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    keyboard =[
        [
            InlineKeyboardButton("한식", callback_data=str(KOREA)),
            InlineKeyboardButton("일식", callback_data=str(JAPAN)),
            InlineKeyboardButton("양식", callback_data=str(USA)),
            InlineKeyboardButton("중식", callback_data=str(CHINA)),
            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="음식 메뉴를 선택해주세요!", reply_markup=reply_markup)
    return CATEGORY

def korea(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="한식을 선택하셨습니다!")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.implicitly_wait(10)
    driver.get('http://dogumaster.com/select/menu')
    query.edit_message_text(text= "메뉴 선택 중입니다 . . . ")
    meal = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[1]/label[2]')
    korean_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[2]')
    korean_food.click()
    Alone_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[3]/label[2]')
    Alone_food.click()
    randomMenu_click = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[5]')
    randomMenu_click.click()
    time.sleep(1.5)
    result = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text
    query.edit_message_text(text="오늘은 " + result + " 을(를) 추천드릴게요.")
    driver.get('https://www.google.com/')
    input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search.clear()
    input_search.send_keys(result, Keys.ENTER)
    food_image_search = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div//*[text()="이미지"]')
    food_image_search.click()
    food_image_choice = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    food_image = food_image_choice.get_attribute('src')
    img_folder = 'C:/Users/ds_a/Desktop/python/조별과제/foodPhoto'
    if not os.path.isdir(img_folder):
        os.mkdir(img_folder)
    urllib.request.urlretrieve(food_image, img_folder+'test.jpg')
    food_Photo = Image.open(img_folder+'test.jpg')
    driver.quit()
    bot.send_photo(chat_id, food_Photo.resize((120,120)))
    keyword = result
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(f'https://www.diningcode.com/isearch.php?query={keyword}')
    location = driver.find_element(By.XPATH,'//*[@id="contents"]/div[1]/div/img')
    action_loc = webdriver.ActionChains(driver)
    action_loc.move_to_element(location)
    action_loc.click() # 내 위치 업데이트
    action_loc.perform() #action함수 실행
    time.sleep(0.3)
    shop = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[1]').text.split('.')
    score = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/p[3]')
    voice1 = f'내 주변 {keyword} 맛집검색결과:\n맛집 점수 {score.text}, 상위{shop[0]}순위 {shop[1]}입니다.\n이동경로를 탐색하겠습니다.'
    bot.send_message(chat_id, voice1)
    destination = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[3]')
    dt = destination.text # 목적지, 맛집주소
    driver.get('https://map.kakao.com/') # 맛집 길찾기 시작
    time.sleep(1)
    direction = driver.find_element(By.XPATH,'//*[@id="search.tab2"]/a')
    box = driver.find_element(By.XPATH,'/html/body/div[10]/div/div/img')
    action_box = webdriver.ActionChains(driver)
    action_box.move_to_element(box)
    action_box.click()
    action_box.perform()
    direction.click()
    startpoint = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input0"]')
    ds = '서울특별시 강동구 천호동 432-11' # 대신it학원 주소
    action_start = webdriver.ActionChains(driver)
    action_start.move_to_element(startpoint)
    action_start.click()
    action_start.perform()
    startpoint.send_keys(ds, Keys.ENTER) # 출발지입력
    time.sleep(1.5)
    des = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
    des.send_keys(dt, Keys.ENTER) # 목적지입력
    time.sleep(1.5)
    public_tr = driver.find_element(By.XPATH, '//*[@id="transittab"]')
    public_tr.click()
    time.sleep(1)
    no_pass = driver.find_elements(By.XPATH, '//*[@id="info.flagsearch"]/div[7]/div/div[1]/h3')
    if len(no_pass) == 0:
        pub_time = driver.find_element(By.XPATH, '//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[1]')
        pub_info = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[2]')
        voice3 = f'대중교통 이용시 예상소요시간 {pub_time.text}, {pub_info.text}. 교통카드를 챙겨주세요.\n'
    else:
        voice3 = "대중교통 경로가 없습니다."
        pass
    work = driver.find_element(By.XPATH, '//*[@id="walktab"]')
    work.click()
    time.sleep(1)
    work_fast_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_fast_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    work_slow_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_slow_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    voice4 = f'도보 이용시 최단거리는 {work_fast_time.text}, {work_fast_dis.text}, 편안한 길은 {work_slow_time.text}, {work_slow_dis.text}\n'
    kor_info = voice3 + voice4
    screen = driver.find_element_by_class_name("cont_map")
    element_png = screen.screenshot_as_png
    with open('test.png', 'wb') as file:
        file.write(element_png)
    tts = gTTS(kor_info, lang='ko')
    tts.save("kor_info.ogg")
    audio = open("kor_info.ogg", 'rb')
    time.sleep(0.5)
    driver.quit()
    bot.send_photo(chat_id, element_png)
    bot.send_message(chat_id, kor_info)
    bot.send_audio(chat_id, audio=audio)
    pyautogui.click(second_Click)
    return ConversationHandler.END

def japan(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    #keyboard
    query.edit_message_text(text="일식을 선택하셨습니다!")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.implicitly_wait(10)
    driver.get('http://dogumaster.com/select/menu')
    query.edit_message_text(text= "메뉴 고민 중입니다 . . . ")
    meal = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[1]/label[2]')
    japan_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[4]')
    japan_food.click()
    Alone_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[3]/label[2]')
    Alone_food.click()
    randomMenu_click = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[5]')
    randomMenu_click.click()
    time.sleep(1)
    result = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text
    query.edit_message_text(text="오늘은 " + result + " 을(를) 추천드릴게요.")
    driver.quit()
    time.sleep(1)
    driver.get('https://www.google.com/')
    input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search.clear()
    input_search.send_keys(result, Keys.ENTER)
    food_image_search = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div//*[text()="이미지"]')
    food_image_search.click()
    food_image_choice = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    food_image = food_image_choice.get_attribute('src')
    img_folder = 'C:/Users/ds_a/Desktop/python/조별과제/foodPhoto'
    if not os.path.isdir(img_folder):
        os.mkdir(img_folder)
    urllib.request.urlretrieve(food_image, img_folder+'test.jpg')
    food_Photo = Image.open(img_folder+'test.jpg')
    bot.send_photo(chat_id, food_Photo.resize((120,120)))
    keyword = result
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(f'https://www.diningcode.com/isearch.php?query={keyword}')
    location = driver.find_element(By.XPATH,'//*[@id="contents"]/div[1]/div/img')
    action_loc = webdriver.ActionChains(driver)
    action_loc.move_to_element(location)
    action_loc.click() # 내 위치 업데이트
    action_loc.perform() #action함수 실행
    time.sleep(0.3)
    shop = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[1]').text.split('.')
    score = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/p[3]')
    voice1 = f'내 주변 {keyword} 맛집검색결과:\n맛집 점수 {score.text}, 상위{shop[0]}순위 {shop[1]}입니다.\n이동경로를 탐색하겠습니다.'
    bot.send_message(chat_id, voice1)
    destination = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[3]')
    dt = destination.text # 목적지, 맛집주소
    driver.get('https://map.kakao.com/') # 맛집 길찾기 시작
    time.sleep(1)
    direction = driver.find_element(By.XPATH,'//*[@id="search.tab2"]/a')
    box = driver.find_element(By.XPATH,'/html/body/div[10]/div/div/img')
    action_box = webdriver.ActionChains(driver)
    action_box.move_to_element(box)
    action_box.click()
    action_box.perform()
    direction.click()
    startpoint = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input0"]')
    ds = '서울특별시 강동구 천호동 432-11' # 대신it학원 주소
    action_start = webdriver.ActionChains(driver)
    action_start.move_to_element(startpoint)
    action_start.click()
    action_start.perform()
    startpoint.send_keys(ds, Keys.ENTER) # 출발지입력
    time.sleep(1.5)
    des = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
    des.send_keys(dt, Keys.ENTER) # 목적지입력
    time.sleep(1.5)
    public_tr = driver.find_element(By.XPATH, '//*[@id="transittab"]')
    public_tr.click()
    time.sleep(1)
    no_pass = driver.find_elements(By.XPATH, '//*[@id="info.flagsearch"]/div[7]/div/div[1]/h3')
    if len(no_pass) == 0:
        pub_time = driver.find_element(By.XPATH, '//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[1]')
        pub_info = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[2]')
        voice3 = f'대중교통 이용시 예상소요시간 {pub_time.text}, {pub_info.text}. 교통카드를 챙겨주세요.\n'
    else:
        voice3 = "대중교통 경로가 없습니다."
        pass
    work = driver.find_element(By.XPATH, '//*[@id="walktab"]')
    work.click()
    time.sleep(1)
    work_fast_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_fast_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    work_slow_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_slow_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    voice4 = f'도보 이용시 최단거리는 {work_fast_time.text}, {work_fast_dis.text}, 편안한 길은 {work_slow_time.text}, {work_slow_dis.text}\n 입니다.'
    screen = driver.find_element_by_class_name("cont_map")
    element_png = screen.screenshot_as_png
    with open('test.png', 'wb') as file:
        file.write(element_png)
    jap_info = voice3 + voice4 
    tts = gTTS(jap_info, lang='ko')
    tts.save("jap_info.ogg")
    audio = open("jap_info.ogg", 'rb')
    time.sleep(0.5)
    driver.quit()
    bot.send_photo(chat_id, element_png)
    bot.send_message(chat_id, jap_info)
    bot.send_audio(chat_id, audio=audio)
    pyautogui.click(second_Click)
    return ConversationHandler.END

def usa(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="양식을 선택하셨습니다.")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.implicitly_wait(10)
    driver.get('http://dogumaster.com/select/menu')
    query.edit_message_text(text= "메뉴 고민 중 입니다 . . . ")
    meal = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[1]/label[2]')
    usa_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[5]')
    usa_food.click()
    Alone_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[3]/label[2]')
    Alone_food.click()
    randomMenu_click = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[5]')
    randomMenu_click.click()
    time.sleep(1.5)
    result = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text
    query.edit_message_text(text="오늘은 " + result + " 을(를) 추천드립니다.")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.get('https://www.google.com/')
    input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search.clear()
    input_search.send_keys(result, Keys.ENTER)
    food_image_search = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div//*[text()="이미지"]')
    food_image_search.click()
    food_image_choice = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    food_image = food_image_choice.get_attribute('src')
    img_folder = 'C:/Users/ds_a/Desktop/python/조별과제/foodPhoto'
    if not os.path.isdir(img_folder):
        os.mkdir(img_folder)
    urllib.request.urlretrieve(food_image, img_folder+'test.jpg')
    food_Photo = Image.open(img_folder+'test.jpg')
    bot.send_photo(chat_id, food_Photo.resize((120,120)))
    keyword = result
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(f'https://www.diningcode.com/isearch.php?query={keyword}')
    location = driver.find_element(By.XPATH,'//*[@id="contents"]/div[1]/div/img')
    action_loc = webdriver.ActionChains(driver)
    action_loc.move_to_element(location)
    action_loc.click() # 내 위치 업데이트
    action_loc.perform() #action함수 실행
    time.sleep(0.3)
    shop = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[1]').text.split('.')
    score = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/p[3]')
    voice1 = f'내 주변 {keyword} 맛집검색결과:\n맛집 점수 {score.text}, 상위{shop[0]}순위 {shop[1]}입니다.\n이동경로를 탐색하겠습니다.'
    bot.send_message(chat_id, voice1)
    destination = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[3]')
    dt = destination.text # 목적지, 맛집주소
    driver.get('https://map.kakao.com/') # 맛집 길찾기 시작
    time.sleep(1)
    direction = driver.find_element(By.XPATH,'//*[@id="search.tab2"]/a')
    box = driver.find_element(By.XPATH,'/html/body/div[10]/div/div/img')
    action_box = webdriver.ActionChains(driver)
    action_box.move_to_element(box)
    action_box.click()
    action_box.perform()
    direction.click()
    startpoint = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input0"]')
    ds = '서울특별시 강동구 천호동 432-11' # 대신it학원 주소
    action_start = webdriver.ActionChains(driver)
    action_start.move_to_element(startpoint)
    action_start.click()
    action_start.perform()
    startpoint.send_keys(ds, Keys.ENTER) # 출발지입력
    time.sleep(1.5)
    des = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
    des.send_keys(dt, Keys.ENTER) # 목적지입력
    time.sleep(1.5)
    public_tr = driver.find_element(By.XPATH, '//*[@id="transittab"]')
    public_tr.click()
    time.sleep(1)
    no_pass = driver.find_elements(By.XPATH, '//*[@id="info.flagsearch"]/div[7]/div/div[1]/h3')
    if len(no_pass) == 0:
        pub_time = driver.find_element(By.XPATH, '//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[1]')
        pub_info = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[2]')
        voice3 = f'대중교통 이용시 예상소요시간 {pub_time.text}, {pub_info.text}. 교통카드를 챙겨주세요.\n'
    else:
        voice3 = "대중교통 경로가 없습니다."
        pass
    work = driver.find_element(By.XPATH, '//*[@id="walktab"]')
    work.click()
    time.sleep(1)
    work_fast_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_fast_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    work_slow_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_slow_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    voice4 = f'도보 이용시 최단거리는 {work_fast_time.text}, {work_fast_dis.text}, 편안한 길은 {work_slow_time.text}, {work_slow_dis.text}\n'
    screen = driver.find_element_by_class_name("cont_map")
    element_png = screen.screenshot_as_png
    with open('test.png', 'wb') as file:
        file.write(element_png)
    usa_info = voice3 + voice4
    tts = gTTS(usa_info, lang='ko')
    tts.save("usa_info.ogg")
    audio = open("usa_info.ogg", 'rb')
    time.sleep(0.5)
    driver.quit()
    bot.send_photo(chat_id, element_png)
    bot.send_message(chat_id, usa_info)
    bot.send_audio(chat_id, audio=audio)
    pyautogui.click(second_Click)
    return ConversationHandler.END
    
def china(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="중식을 선택하셨습니다.")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.implicitly_wait(10)
    driver.get('http://dogumaster.com/select/menu')
    query.edit_message_text(text= "메뉴 고민 중 입니다 . . . ")
    meal = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[1]/label[2]')
    china_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[3]')
    china_food.click()
    Alone_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[3]/label[2]')
    Alone_food.click()
    randomMenu_click = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[5]')
    randomMenu_click.click()
    time.sleep(1.5)
    result = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text
    query.edit_message_text(text="오늘은 " + result + " 을(를) 추천드립니다.")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.get('https://www.google.com/')
    input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search.clear()
    input_search.send_keys(result, Keys.ENTER)
    food_image_search = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div//*[text()="이미지"]')
    food_image_search.click()
    food_image_choice = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    food_image = food_image_choice.get_attribute('src')
    img_folder = 'C:/Users/ds_a/Desktop/python/조별과제/foodPhoto'
    if not os.path.isdir(img_folder):
        os.mkdir(img_folder)
    urllib.request.urlretrieve(food_image, img_folder+'test.jpg')
    food_Photo = Image.open(img_folder+'test.jpg')
    bot.send_photo(chat_id, food_Photo.resize((120,120)))
    keyword = result
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(f'https://www.diningcode.com/isearch.php?query={keyword}')
    location = driver.find_element(By.XPATH,'//*[@id="contents"]/div[1]/div/img')
    action_loc = webdriver.ActionChains(driver)
    action_loc.move_to_element(location)
    action_loc.click() # 내 위치 업데이트
    action_loc.perform() #action함수 실행
    time.sleep(0.3)
    shop = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[1]').text.split('.')
    score = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/p[3]')
    voice1 = f'내 주변 {keyword} 맛집검색결과:\n맛집 점수 {score.text}, 상위{shop[0]}순위 {shop[1]}입니다.\n이동경로를 탐색하겠습니다.'
    bot.send_message(chat_id, voice1)
    destination = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[3]')
    dt = destination.text # 목적지, 맛집주소
    driver.get('https://map.kakao.com/') # 맛집 길찾기 시작
    time.sleep(1)
    direction = driver.find_element(By.XPATH,'//*[@id="search.tab2"]/a')
    box = driver.find_element(By.XPATH,'/html/body/div[10]/div/div/img')
    action_box = webdriver.ActionChains(driver)
    action_box.move_to_element(box)
    action_box.click()
    action_box.perform()
    direction.click()
    startpoint = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input0"]')
    ds = '서울특별시 강동구 천호동 432-11' # 대신it학원 주소
    action_start = webdriver.ActionChains(driver)
    action_start.move_to_element(startpoint)
    action_start.click()
    action_start.perform()
    startpoint.send_keys(ds, Keys.ENTER) # 출발지입력
    time.sleep(1.5)
    des = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
    des.send_keys(dt, Keys.ENTER) # 목적지입력
    time.sleep(1.5)
    public_tr = driver.find_element(By.XPATH, '//*[@id="transittab"]')
    public_tr.click()
    time.sleep(1)
    no_pass = driver.find_elements(By.XPATH, '//*[@id="info.flagsearch"]/div[7]/div/div[1]/h3')
    if len(no_pass) == 0:
        pub_time = driver.find_element(By.XPATH, '//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[1]')
        pub_info = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[2]')
        voice3 = f'대중교통 이용시 예상소요시간 {pub_time.text}, {pub_info.text}. 교통카드를 챙겨주세요.\n'
    else:
        voice3 = "대중교통 경로가 없습니다."
        pass
    work = driver.find_element(By.XPATH, '//*[@id="walktab"]')
    work.click()
    time.sleep(1)
    work_fast_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_fast_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    work_slow_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_slow_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    voice4 = f'도보 이용시 최단거리는 {work_fast_time.text}, {work_fast_dis.text}, 편안한 길은 {work_slow_time.text}, {work_slow_dis.text}\n'
    screen = driver.find_element_by_class_name("cont_map")
    element_png = screen.screenshot_as_png
    with open('test.png', 'wb') as file:
        file.write(element_png)
    chi_info = voice3 + voice4
    tts = gTTS(chi_info, lang='ko')
    tts.save("chi_info.ogg")
    audio = open("chi_info.ogg", 'rb')
    time.sleep(0.5)
    driver.quit()
    bot.send_photo(chat_id, element_png)
    bot.send_message(chat_id, chi_info)
    bot.send_audio(chat_id, audio=audio)
    pyautogui.click(second_Click)
    return ConversationHandler.END

def news(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    keyboard =[
        [
            InlineKeyboardButton("헤드라인", callback_data=str(HEADLINE))),
            InlineKeyboardButton("정치", callback_data=str(POLITICS)),
            InlineKeyboardButton("경제", callback_data=str(ECONOMY)),
            InlineKeyboardButton("사회", callback_data=str(SOCIETY)),
            

        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="카테고리를 선택해주세요", reply_markup=reply_markup)
    return CATEGORY

def headline(update: Update, _: CallbackContext) -> int:
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://news.naver.com')

    hdline = '#today_main_news > div.hdline_news > ul > li> div.hdline_article_tit > a'
    hd_tit=driver.find_elements_by_css_selector(hdline)

    tit = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').text
    tit2 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').text
    tit3 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').text
    tit4 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[4]/div[1]/a').text
    tit5 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[5]/div[1]/a').text
    
    hdnews = f'''
    네이버 뉴스 헤드라인 : 
    1. {tit},
    2. {tit2},
    3. {tit3},
    4. {tit4},
    5. {tit5}
    '''
    
    bot.reply_to(message,hdnews)
    time.sleep(0.5)
    tts = gTTS(hdnews, lang='ko')
    tts.save("hdnews.ogg")
    audio = open("hdnews.ogg",'rb')
    bot.send_audio(chat_id = chat_id, audio = audio)
    time.sleep(0.5)
    driver.quit()
    pyautogui.click(second_Click)
    return ConversationHandler.END

def politics(update: Update, _: CallbackContext) -> int:
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://news.naver.com')

    pol = '#section_politics > div.com_list > div > ul > li > a'
    
    tit = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').text
    tit2 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').text
    tit3 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').text
    tit4 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[4]/div[1]/a').text
    tit5 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[5]/div[1]/a').text
    
    plnews = f'''
    네이버 뉴스 정치 : 
    1. {tit},
    2. {tit2},
    3. {tit3},
    4. {tit4},
    5. {tit5}
    '''

    bot.reply_to(message,plnews)
    time.sleep(0.5)
    tts = gTTS(plnews, lang='ko')
    tts.save("plnews.ogg")
    audio = open("plnews.ogg",'rb')
    bot.send_audio(chat_id = chat_id, audio = audio)
    time.sleep(0.5)
    driver.quit()
    pyautogui.click(second_Click)
    return ConversationHandler.END

def economy(update: Update, _: CallbackContext) -> int:
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://news.naver.com')
    ec_list = []
    eco = '#section_economy > div.com_list > div > ul > li > a '
    eco_tit=driver.find_elements_by_css_selector(eco)
    
    tit = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').text
    tit2 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').text
    tit3 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').text
    tit4 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[4]/div[1]/a').text
    tit5 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[5]/div[1]/a').text

    txt = f'''네이버 뉴스 경제 : 
    1. {tit},
    2. {tit2},
    3. {tit3},
    4. {tit4},
    5. {tit5}
    '''
    bot.reply_to(message,txt)
    time.sleep(0.5)
    tts = gTTS(txt, lang='ko')
    tts.save("txt.ogg")
    audio = open("txt.ogg",'rb')
    bot.send_audio(chat_id = chat_id, audio = audio)
    pyautogui.click(second_Click)
    return ConversationHandler.END

def society(update: Update, _: CallbackContext) -> int:
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://news.naver.com')

    soc = '#section_society > div.com_list > div > ul > li > a '
    
    tit = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').text
    tit2 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').text
    tit3 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').text
    tit4 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[4]/div[1]/a').text
    tit5 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[5]/div[1]/a').text
    
    txt = f'''네이버 뉴스 사회 : 
    1. {tit},
    2. {tit2},
    3. {tit3},
    4. {tit4},
    5. {tit5}
    '''
    bot.reply_to(message,txt)
    time.sleep(0.5)
    tts = gTTS(txt, lang='ko')
    tts.save("txt.ogg")
    audio = open("txt.ogg",'rb')
    bot.send_audio(chat_id = chat_id, audio = audio)
    pyautogui.click(second_Click)
    return ConversationHandler.END
    
def weather(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.google.com/search?q=오늘날씨')
    time.sleep(0.5)
    weather= driver.find_element(By.XPATH,'//*[@id="wob_dc"]')
    weather_info = weather.text
    svg = driver.find_element(By.XPATH,'//*[@id="wob_gsvg"]')
    tmp_list = svg.text.split('\n')
    map_list = list(map(float, tmp_list))
    tmp_max = max(map_list)
    tmp_min = min(map_list)
    tmp_gap = float(tmp_max) - float(tmp_min)
    tmp_avg = sum(map_list)/len(map_list)
    voice_tmp = f'오늘의 날씨정보는 {weather_info}, 최고기온 {tmp_max}도,최저기온 {tmp_min}도,평균기온 {tmp_avg}도, 일교차는{tmp_gap}도 입니다.\n'    
    v_w_info =""
    voice_tmp_gap= ""
    voice_cl = ""

    if weather_info == '광역성 소나기':
        v_w_info1 = f'{weather_info}가 예정되어 있습니다. 휴대용 우산을 챙겨주세요.\n'
        v_w_info = v_w_info1
    elif weather_info == '비':
        v_w_info2 = f'{weather_info}가 예정되어 있습니다. 우산을 챙겨주세요.\n'
        v_w_info = v_w_info2

    if tmp_gap > 7.5:
        voice_tmp_gap1 = f'오늘은 일교차가 큽니다. 얇은 옷을 겹쳐입거나 외투를 준비해주세요.\n'
        voice_tmp_gap = voice_tmp_gap1
    else:
        voice_tmp_gap2 = f'오늘은 일교차가 크지 않습니다.\n'
        voice_tmp_gap = voice_tmp_gap2

    if tmp_avg >= 10 and tmp_avg <=16:
        voice_cl1 = f'기온별 옷차림 추천, 평균 {tmp_avg}도에는 자켓, 셔츠, 가디건, 간절기 야상, 살구색 스타킹을 추천드릴게요!'
        voice_cl = voice_cl1
    elif tmp_avg > 16 and tmp_avg <= 19:
        voice_cl2 = f'기온별 옷차림 추천, {tmp_avg}도에는 니트, 가디건, 후드티, 맨투맨, 청바지, 면바지, 슬랙스, 원피스을 추천드릴게요!'
        voice_cl = voice_cl2
    elif tmp_avg >19 and tmp_avg <=  22:
        voice_cl3 = f'기온별 옷차림 추천, {tmp_avg}도에는 긴팔티, 가디건, 후드티, 면바지 ,슬랙스, 스키니을 추천드릴게요!'
        voice_cl = voice_cl3
    elif tmp_avg >22 and tmp_avg <= 26:
        voice_cl4 = f'기온별 옷차림 추천, {tmp_avg}도에는 반팔, 얇은 셔츠, 얇은 긴팔, 반바지, 면바지을 추천드릴게요!'
        voice_cl = voice_cl4
    elif tmp_avg > 26:
        voice_cl5 = f'기온별 옷차림 추천, {tmp_avg}도에는 나시티, 반바지, 민소매, 원피스을 추천드릴게요!'
        voice_cl = voice_cl5
    elif tmp_avg < 10:
        voice_cl6 = f'기온별 옷차림 추천, {tmp_avg}도에는 패딩점퍼, 코트, 야상, 목도리, 장갑, 히트텍을 추천드릴게요!'
        voice_cl = voice_cl6

    weather_message = voice_tmp + v_w_info + voice_tmp_gap + voice_cl
    tts = gTTS(weather_message, lang='ko')
    tts.save("weather_message.ogg")
    audio = open("weather_message.ogg",'rb')
    time.sleep(0.5)
    driver.quit()
    bot.send_message(chat_id,weather_message)
    bot.send_audio(chat_id, audio=audio)
    pyautogui.click(second_Click)
    return ConversationHandler.END

def main() -> None:
    updater = Updater("1709776665:AAF-sEQXF2TAW67-aOno7o4zrDoiGSeeRrU")
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states={
            CATEGORY: [
                CallbackQueryHandler(exercise, pattern='^' + str(EXERCISE) + '$'),
                CallbackQueryHandler(cardioexercise, pattern='^' + str(CARDIOEXERCISE) + '$'),
                CallbackQueryHandler(weighttraining, pattern='^' + str(WEIGHTTRAINING) + '$'),
                CallbackQueryHandler(news, pattern='^' + str(NEWS) + '$'),
                CallbackQueryHandler(corona, pattern='^' + str(CORONA) + '$'),
                CallbackQueryHandler(stock, pattern='^' + str(STOCK) + '$'),
                CallbackQueryHandler(realestate, pattern='^' + str(REALESTATE) + '$'),
                CallbackQueryHandler(virtualcurrency, pattern='^' + str(VIRTUALCURRENCY) + '$'),
                CallbackQueryHandler(weather, pattern='^' + str(WEATHER) + '$'),
                CallbackQueryHandler(meal, pattern='^' + str(MEAL) + '$'),
                CallbackQueryHandler(korea, pattern='^' + str(KOREA) + '$'),
                CallbackQueryHandler(japan, pattern='^' + str(JAPAN) + '$'),
                CallbackQueryHandler(usa, pattern='^' + str(USA) + '$'),
                CallbackQueryHandler(china, pattern='^' + str(CHINA) + '$'),
                
            ],
        },
        fallbacks= [CommandHandler('start', start)]
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()

def wakeup_time():
    bot.send_message(chat_id, "안녕하세요. 주인님 오늘도 힘찬 하루 ! 시간계획을 실행합니다.")
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.google.com/search?q=오늘날씨')
    time.sleep(1)
    weather= driver.find_element(By.XPATH,'//*[@id="wob_dc"]')
    weather_info = weather.text
    svg = driver.find_element(By.XPATH,'//*[@id="wob_gsvg"]')
    tmp_info = svg.text
    tmp_list = svg.text.split('\n')
    map_list = list(map(float, tmp_list))

    tmp_max = max(map_list)
    tmp_min = min(map_list)
    print(tmp_max, tmp_min)
    tmp_gap = float(tmp_max) - float(tmp_min)
    voice_tmp = f'오늘의 날씨정보는 {weather_info}, 최고기온 섭씨{tmp_max}도, 최저기온 섭씨{tmp_min}도, 일교차는{tmp_gap}도 입니다.'
    print(tmp_gap)

    bot.send_message(chat_id, voice_tmp)    
    
    engine.setProperty('rate', 150)
    engine.save_to_file(voice_tmp, "tmp_v1.mp3")
    engine.runAndWait()
    pyttsx3.init(driverName='sapi5') 
    time.sleep(1)
    bot.send_audio(chat_id=chat_id, audio=open('tmp_v1.mp3', 'rb'))

    if weather_info == '광역성 소나기':
        v_w_info1 = f'{weather_info}가 예정되어 있습니다. 휴대용 우산을 챙겨주세요.'
        bot.send_message(chat_id.v_w_info)
        engine.setProperty('rate', 150)
        engine.save_to_file(v_w_info, "w_info_voice.mp3")
        engine.runAndWait()
        pyttsx3.init(driverName='sapi5') 
        time.sleep(1)
        bot.send_audio(chat_id=chat_id, audio=open('w_info_voice.mp3', 'rb'))
    elif weather_info == '비':
        v_w_info2 = f'{weather_info}가 예정되어 있습니다. 우산을 챙겨주세요'
        bot.send_message(chat_id.v_w_info2)
        engine.setProperty('rate', 150)
        engine.save_to_file(v_w_info2, "w_info_voice2.mp3")
        engine.runAndWait()
        pyttsx3.init(driverName='sapi5') 
        time.sleep(1)
        bot.send_audio(chat_id=chat_id, audio=open('w_info_voice2.mp3', 'rb'))


    if tmp_gap > 7.5:
        voice_tmp_gap1 = f'오늘 일교차는 {tmp_gap}입니다. 얇은 옷을 겹쳐입거나 외투를 준비해주세요.'
        bot.send_message(chat_id, voice_tmp_gap1)
        engine.setProperty('rate', 150)
        engine.save_to_file(voice_tmp_gap1, "v_tmp_gap.mp3")
        engine.runAndWait()
        pyttsx3.init(driverName='sapi5') 
        time.sleep(1)
        bot.send_audio(chat_id=chat_id, audio=open('v_tmp_gap.mp3', 'rb'))

    elif tmp_gap == 7.5:
        voice_tmp_gap2 = f'오늘 일교차는 {tmp_gap}입니다. 적정 일교차입니다.'
        bot.send_message(chat_id, voice_tmp_gap2)
        engine.setProperty('rate', 150)
        engine.save_to_file(voice_tmp_gap2, "v_tmp_gap2.mp3")
        engine.runAndWait()
        pyttsx3.init(driverName='sapi5') 
        time.sleep(1)
        bot.send_audio(chat_id=chat_id, audio=open('v_tmp_gap2.mp3', 'rb'))
    else:
        voice_tmp_gap3 = f'오늘 일교차는 {tmp_gap}입니다. 일교차가 크지 않습니다.'
        bot.send_message(chat_id, voice_tmp_gap3)
        engine.setProperty('rate', 150)
        engine.save_to_file(voice_tmp_gap3, "v_tmp_gap3.mp3")
        engine.runAndWait()
        pyttsx3.init(driverName='sapi5') 
        time.sleep(1)
        bot.send_audio(chat_id=chat_id, audio=open('v_tmp_gap3.mp3', 'rb'))


    tmp_avg = sum(map_list)/len(map_list)

    voice_tmp_avg = f'오늘의 평균 온도는 섭씨 {tmp_avg}도 입니다.'
    bot.send_message(chat_id, voice_tmp_avg)
    engine.setProperty('rate', 150)
    engine.save_to_file(voice_tmp_avg, "voice_tmp_avg.mp3")
    engine.runAndWait()
    pyttsx3.init(driverName='sapi5') 
    time.sleep(1)
    bot.send_audio(chat_id=chat_id, audio=open('voice_tmp_avg.mp3', 'rb'))

    if tmp_avg >= 10 and tmp_avg <=16:
        voice_cl = f'기온별 옷차림 추천, {tmp_avg}도에는 자켓, 셔츠, 가디건, 간절기 야상, 살구색 스타킹이 적합합니다.'
        bot.send_message(chat_id, voice_cl)
        engine.setProperty('rate', 150)
        engine.save_to_file(voice_cl, "voice_cl.mp3")
        engine.runAndWait()
        pyttsx3.init(driverName='sapi5') 
        time.sleep(1)
        bot.send_audio(chat_id=chat_id, audio=open('voice_cl.mp3', 'rb'))
    elif tmp_avg >= 17 and tmp_avg <= 19:
        voice_cl2 = f'기온별 옷차림 추천, {tmp_avg}도에는 니트, 가디건, 후드티, 맨투맨, 청바지, 면바지, 슬랙스, 원피스가 적합합니다.'
        bot.send_message(chat_id, voice_cl2)
        engine.setProperty('rate', 150)
        engine.save_to_file(voice_cl2, "voice_cl2.mp3")
        engine.runAndWait()
        pyttsx3.init(driverName='sapi5') 
        time.sleep(1)
        bot.send_audio(chat_id=chat_id, audio=open('voice_cl2.mp3', 'rb'))
    elif tmp_avg >=20 and tmp_avg <=  22:
        voice_cl3 = f'기온별 옷차림 추천, {tmp_avg}도에는 긴팔티, 가디건, 후드티, 면바지 ,슬랙스, 스키니가 적합합니다'
        bot.send_message(chat_id, voice_cl3)
        engine.setProperty('rate', 150)
        engine.save_to_file(voice_cl3, "voice_cl3.mp3")
        engine.runAndWait()
        pyttsx3.init(driverName='sapi5') 
        time.sleep(1)
        bot.send_audio(chat_id=chat_id, audio=open('voice_cl3.mp3', 'rb'))
    elif tmp_avg >=23 and tmp_avg <= 26:
        voice_cl4 = f'기온별 옷차림 추천, {tmp_avg}도에는 반팔, 얇은 셔츠, 얇은 긴팔, 반바지, 면바지가 적합합니다.'
        bot.send_message(chat_id, voice_cl4)
        engine.setProperty('rate', 150)
        engine.save_to_file(voice_cl4, "voice_cl4.mp3")
        engine.runAndWait()
        pyttsx3.init(driverName='sapi5') 
        time.sleep(1)
        bot.send_audio(chat_id=chat_id, audio=open('voice_cl4.mp3', 'rb'))
    elif tmp_avg > 27:
        voice_cl5 = f'기온별 옷차림 추천, {tmp_avg}도에는 나시티, 반바지, 민소매, 원피스가 적합합니다.'
        bot.send_message(chat_id, voice_cl5)
        engine.setProperty('rate', 150)
        engine.save_to_file(voice_cl5, "voice_cl5.mp3")
        engine.runAndWait()
        pyttsx3.init(driverName='sapi5') 
        time.sleep(1)
        bot.send_audio(chat_id=chat_id, audio=open('voice_cl5.mp3', 'rb'))

    elif tmp_avg < 9:
        voice_cl6 = f'기온별 옷차림 추천, {tmp_avg}도에는 패딩점퍼, 코트, 야상, 목도리, 장갑, 히트텍이 적합합니다.'
        bot.send_message(chat_id, voice_cl6)
        engine.setProperty('rate', 150)
        engine.save_to_file(voice_cl6, "voice_cl6.mp3")
        engine.runAndWait()
        pyttsx3.init(driverName='sapi5') 
        time.sleep(1)
        bot.send_audio(chat_id=chat_id, audio=open('voice_cl6.mp3', 'rb'))
    driver.quit()

# def morningnews_time(update: Update, _: CallbackContext) -> int:
#     query = update.callback_query
#     query.answer()
#     keyboard =[
#         [
#             InlineKeyboardButton("코로나", callback_data=str(CORONA)),
#             InlineKeyboardButton("주식", callback_data=str(STOCK)),
#             InlineKeyboardButton("부동산", callback_data=str(REALESTATE)),
#             InlineKeyboardButton("암호화폐", callback_data=str(VIRTUALCURRENCY)),
            

#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     bot.send_message(chat_id,"오늘 Topic 뉴스를 전해드릴게요.",reply_markup= reply_markup)
#     return CATEGORY
    
# def breakfast_time():

# def Break_time():
    
# def launch_time():

# def gym_time():

# def dinner_time():
    


# schedule.every().day.at("11:06").do(wakeup_time)
# schedule.every().day.at("16:44").do(morningnews_time)

# def AutoThread1(name):
#     while 1:
#         schedule.run_pending()
#         time.sleep(1)
        


# t1 = threading.Thread(target=AutoThread1, args=('1'))
# t1.start()


if __name__ == '__main__':
    main()