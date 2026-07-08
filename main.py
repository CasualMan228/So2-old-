import random
import os #работа с файлами
startFile = "D:\\Start\\OrderedCells.txt"
import time
import re #поиск текста по шаблону
import cv2 #подгрузка, коррекция и проверка на сходство фото
rangeValue = 0.75
import pyautogui #взаимодействие с ПК
import pytesseract #детект текста с фото
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import numpy as np #работа с массива (при подгрузке скриншота)
from PIL import Image #открытие фото для дальнейших действий

count = 0
kolvo = 0

########################################################################################################################

print("Версия 0.1 (TEST)🐍")
print("Подгружаю фотографии ячеек...")
start = {
    "aurora": "D:\\Start\\Aurora.png",
    "cold_lead": "D:\\Start\\Cold_Lead.png",
    "dusk": "D:\\Start\\Dusk.png",
    "fiend": "D:\\Start\\Fiend.png",
    "peaceful_dream": "D:\\Start\\Peaceful_Dream.png",
    "pixelV2": "D:\\Start\\PixelV2.png",
    "powergame": "D:\\Start\\Powergame.png",
    "pursuit": "D:\\Start\\Pursuit.png",
    "rhino": "D:\\Start\\Rhino.png",
    "scale": "D:\\Start\\Scale.png",
    "silver_plated": "D:\\Start\\Silver_Plated.png",
    "tropic": "D:\\Start\\Tropic.png",
    "vector": "D:\\Start\\Vector.png",
    "vesper_haze": "D:\\Start\\Vesper_Haze.png",
    "vhs": "D:\\Start\\VHS.png",
    "zap": "D:\\Start\\Zap.png",
    "donate": "D:\\Start\\Donate.png",
    "sell_buy": "D:\\Start\\SellBuy.png",
    "marketplace": "D:\\Start\\MarketPlace.png",
    "prikol_error": "D:\\Start\\PrikolError.png"
}
loadedStart = {name: cv2.imread(path) for name, path in start.items()}
donateFind = loadedStart["donate"]
sellBuyFind = loadedStart["sell_buy"]
marketplaceFind = loadedStart["marketplace"]
prikolError = loadedStart["prikol_error"]
print("Все фотографии ячеек успешно подгружены👍")

########################################################################################################################

def checkPrikolError():
    print(f"Вызвана функция по проверке на уведомление об какой-либо ошибке⚙️")
    screenshot = pyautogui.screenshot()
    screenshot_cv = np.array(screenshot)
    blurred_screenshot = cv2.GaussianBlur(screenshot_cv, (5, 5), 0)
    loadedScreenshot = cv2.cvtColor(np.array(blurred_screenshot), cv2.COLOR_RGB2BGR)
    similarity = cv2.matchTemplate(loadedScreenshot, prikolError, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(similarity)
    if max_val >= rangeValue:
        print("Увидел уведомление об ошибке = Возвращаюсь назад в инвентарь...")
        time.sleep(1)

        pyautogui.click(200, 80) #все назад
        pyautogui.click(200, 80)
        pyautogui.click(200, 80)
        pyautogui.click(200, 80)
        pyautogui.click(200, 80)

def checkMessageSellBuy(): #нижний левый угол по ширине 8 см, по высоте 2,5 см, справа заслоняет чуть серебро
    print(f"Вызвана функция по проверке на уведомление о покупке/продажи (сверху)⚙️")
    screenshot = pyautogui.screenshot()
    screenshot_cv = np.array(screenshot)
    blurred_screenshot = cv2.GaussianBlur(screenshot_cv, (5, 5), 0)
    loadedScreenshot = cv2.cvtColor(np.array(blurred_screenshot), cv2.COLOR_RGB2BGR)
    similarity = cv2.matchTemplate(loadedScreenshot, sellBuyFind, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(similarity)
    if max_val >= rangeValue:
        print("Увидел уведомление sellBye = Ждем...")
        time.sleep(3)

def find_best_match(template, screenshot):
    screenshot_cv = np.array(screenshot)
    loadedScreenshot = screenshot_cv.copy()
    if template.size == 0 or loadedScreenshot.size == 0: #проверка на ненулевые размеры изображений
        return None, None
    if template.shape[0] > loadedScreenshot.shape[0] or template.shape[1] > loadedScreenshot.shape[1]: #проверка на то, что габариты шаблона не превышают габариты скриншота
        return None, None
    similarity = cv2.matchTemplate(loadedScreenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(similarity)
    cv2.imwrite("D:\\Start\\SellTEST.png", loadedScreenshot)
    if max_val >= rangeValue:  #если хорошее совпадение, то возвращаем результат
        return max_val, max_loc
    return None, None  #если недостаточно совпадений вернуть None

def order(cellName):
    print(f"Вызвана функция по заказу ячейки {cellName}⚙️")
    global count
    global kolvo
    global startFile
    global donateFind
    time.sleep(1)

    print("Перейдите в свой инвентарь в Bluestacks 5 -> Standoff 2 -> f11 (для полноэкранного режима). У вас 10 секунд!")
    print('Вы преждевременно не должны были ничего не ставить на продажу и на закупку, убрать лишние "NEW" скины и экипировать нужные предметы в своем инвентаре')
    print("УБЕРИТЕ ВСЕ ВСПЛЫВАЮШИЕ ПРИЛОЖЕНИЯ И УВЕДОМЛЕНИЯ!")
    print("Ваша раскладка клавиатуры должна быть на ЛАТИНИЦЕ!")
    print("В Standoff 2 необходимо, чтобы никто вам ничего НЕ ПИСАЛ и НЕ ПРИГЛАШАЛ в лобби!")
    print("Не трогайте и не взаимодействуйте (если нет необходимости) мышь и клавиатуру!")
    time.sleep(10)

    if cellName not in start:
        print(f"Ячейка '{cellName}' не существует!❌")
        return
    checkMessageSellBuy()
    checkPrikolError()
    print("Перехожу на рынок...")
    pyautogui.click(1000, 40) #рынок
    time.sleep(1)

    checkPrikolError()
    print("Сортирую с самых нищих скинов...")
    pyautogui.click(333, 333) #сортировка по редкости (для сброса ненужных сортировок)
    pyautogui.click(300, 400) #сортировка по цене (сначала самые богатые)
    pyautogui.click(300, 400) #сортировка по цене (сначала самые нищие)
    pyautogui.moveTo(1000, 500) #тащим курсор к скинам для дальнейшей прокрутки поиска нужной ячейки
    time.sleep(1)

    imageToFind = loadedStart[cellName]
    print(f"Ищу ячейку {cellName}...")
    screenshot = pyautogui.screenshot()
    loadedScreenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    similarity = cv2.matchTemplate(loadedScreenshot, imageToFind, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(similarity)
    while max_val < rangeValue:
        print(f"Не нашел ячейку {cellName}, продолжаю искать...")
        if count == 20:
            print(f"Заново начинаю искать ячейку {cellName}...")
            checkMessageSellBuy()
            pyautogui.click(600, 70) #магазин
            time.sleep(1)

            checkMessageSellBuy()
            pyautogui.click(1000, 40) #рынок
            time.sleep(1)

            checkPrikolError()
            pyautogui.click(333, 333) #сортировка по редкости (для сброса ненужных сортировок)
            pyautogui.click(300, 400) #сортировка по цене (сначала самые богатые)
            pyautogui.click(300, 400) #сортировка по цене (сначала самые нищие)
            count = 0
            time.sleep(1)

        pyautogui.moveTo(1000, 500)
        pyautogui.scroll(-150)
        time.sleep(2)

        screenshot = pyautogui.screenshot()
        loadedScreenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        similarity = cv2.matchTemplate(loadedScreenshot, imageToFind, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(similarity)
        count += 1
    if max_val >= rangeValue:
        print(f"Нашел ячейку {cellName}! Узнаю стоимость...")
        top_left = max_loc
        height, width, _ = imageToFind.shape
        center_x = top_left[0] + width // 2
        center_y = top_left[1] + height // 2
        checkMessageSellBuy()
        pyautogui.click(center_x, center_y) #мы переносимся уже в ячейку
        time.sleep(5)

        checkPrikolError()
        screenshot = pyautogui.screenshot()
        screenshot_cv = np.array(screenshot)
        blurred_screenshot = cv2.GaussianBlur(screenshot_cv, (5, 5), 0)
        loadedScreenshot = cv2.cvtColor(np.array(blurred_screenshot), cv2.COLOR_RGB2BGR)
        region_x = 1230
        region_y = 737
        region_width = 270
        region_height = 150
        region = loadedScreenshot[region_y:region_y + region_height, region_x:region_x + region_width] #region фулл цены
        cv2.imwrite("D:\\Start\\Price.png", region)
        text = pytesseract.image_to_string(Image.open("D:\\Start\\Price.png"), lang="eng")
        price = re.search(r"\d+.\d{2}", text)
        if price:
            price = price.group()
            price = float(price)
            price = float(f"{price:.2f}") #снимаем лишнюю разрядность, т.е. делаем стоимость в виде x.xx
            print(f"Стоимость: {price} голды")
            priceRemove = 0.5 * price
            newPrice = price - priceRemove
            newPrice = float(f"{newPrice:.2f}") #снимаем лишнюю разрядность, т.е. делаем стоимость в виде x.xx
            print(f"Стоимость с 50% комиссией: {newPrice} голды")
            time.sleep(1)

            print("Узнаю стоимость первого слота продажи...")
            screenshot = pyautogui.screenshot()
            screenshot_cv = np.array(screenshot)
            blurred_screenshot = cv2.GaussianBlur(screenshot_cv, (5, 5), 0)
            loadedScreenshot = cv2.cvtColor(np.array(blurred_screenshot), cv2.COLOR_RGB2BGR)
            region_x = 1300
            region_y = 400
            region_width = 200
            region_height = 100
            region = loadedScreenshot[region_y:region_y + region_height, region_x:region_x + region_width] #region первой цены
            cv2.imwrite("D:\\Start\\FirstPrice.png", region)
            text = pytesseract.image_to_string(Image.open("D:\\Start\\FirstPrice.png"), lang="eng")
            firstPrice = re.search(r"\d+.\d{2}", text)
            firstPrice = firstPrice.group()
            firstPrice = float(firstPrice)
            firstPrice = float(f"{firstPrice:.2f}") #снимаем лишнюю разрядность, т.е. делаем стоимость в виде x.xx
            if firstPrice:
                if firstPrice <= newPrice:
                    print("Цена первого слота продажи такая же как и цена с 20% комиссией = НЕВЫГОДНО = Отмена🚫")
                    time.sleep(1)

                    checkMessageSellBuy()
                    pyautogui.click(190, 45) #стрелка назад
                    pyautogui.click(190, 45) #стрелка назад
                    pyautogui.click(190, 45) #стрелка назад
                elif firstPrice > newPrice:
                    print(f"Начинаю анализ закупки {cellName}...")
                    time.sleep(1)

                    pyautogui.click(1600, 250) #сбросить, если совершали старую закупку этой же ячейки
                    time.sleep(1)

                    checkPrikolError()
                    pyautogui.click(1650, 150) #заказать начальное
                    time.sleep(1)

                    checkPrikolError()
                    pyautogui.click(1000, 440) #ввод числа голды на закупку
                    for _ in range(30):
                        pyautogui.press("backspace")
                    pyautogui.write(str(newPrice))
                    time.sleep(1)

                    checkPrikolError()
                    pyautogui.click(1000, 515) #ввод количества на закупку
                    for _ in range(30):
                        pyautogui.press("backspace")
                    time.sleep(1)

                    checkPrikolError()
                    rand_choice = random.random()
                    if rand_choice < 1 / 6:
                        pyautogui.write("10")
                        kolvo = 10
                    elif rand_choice < 1 / 2:
                        pyautogui.write("5")
                        kolvo = 5
                    elif rand_choice < 5 / 6:
                        pyautogui.write("2")
                        kolvo = 2
                    else:
                        pyautogui.write("1")
                        kolvo = 1
                    print(f"Данные для закупки заполнены: цена -> {newPrice} голды и количество -> {kolvo} штук")
                    print("Все расчеты успешно выполнены -> Выполняю закупку...")
                    checkPrikolError()
                    pyautogui.click(952, 700) #заказать финальное
                    time.sleep(1)

                    checkPrikolError()
                    screenshot = pyautogui.screenshot()
                    loadedScreenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
                    similarity = cv2.matchTemplate(loadedScreenshot, donateFind, cv2.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(similarity)
                    if max_val >= rangeValue:
                        print("У вас недостаток средств для данной ячейки!❌")
                        time.sleep(1)

                        pyautogui.click(240, 980) #все назад
                        pyautogui.click(200, 80)
                        pyautogui.click(200, 80)
                        pyautogui.click(200, 80)
                        pyautogui.click(200, 80)
                        return
                    if os.path.exists(startFile):
                        with open(startFile, "r") as file:
                            lines = file.readlines()
                    else:
                        lines = []
                    new_line = f"{cellName} {price}\n"
                    found = False
                    for i, line in enumerate(lines):
                        if line.startswith(cellName):
                            print("Открываю OrderedCells.txt... Вижу, что данная ячейка уже была в файле -> Перезаписываю")
                            lines[i] = new_line
                            found = True
                            break
                    if not found:
                        print("Открываю OrderedCells.txt... Вижу, что данной ячейки еще не было в файле -> Добавляю")
                        lines.append(new_line)
                    with open(startFile, "w") as file:
                        file.writelines(lines)
                    time.sleep(5)

                    print("Закупка по идее должна была выполниться и мы возвращаемся обратно в инвентарь")
                    pyautogui.click(200, 80) #все назад
                    pyautogui.click(200, 80)
                    pyautogui.click(200, 80)
                    pyautogui.click(200, 80)
            else:
                print("Не удалось узнать цену на первый слот продажи!❌")
                time.sleep(1)

                pyautogui.click(200, 80) #все назад
                pyautogui.click(200, 80)
                pyautogui.click(200, 80)
                pyautogui.click(200, 80)
                return
        else:
            print("Не удалось узнать цену на ячейку!❌")
            time.sleep(1)

            pyautogui.click(200, 80) #все назад
            pyautogui.click(200, 80)
            pyautogui.click(200, 80)
            pyautogui.click(200, 80)
            return

def sell():
    print(f"Вызвана функция по продаже ячеек из инвентаря⚙️")
    time.sleep(1)

    print("Перейдите в свой инвентарь в Bluestacks 5 -> Standoff 2 -> f11 (для полноэкранного режима). У вас 10 секунд!")
    print('Вы преждевременно не должны были ничего не ставить на продажу и на закупку, убрать лишние "NEW" скины и экипировать нужные предметы в своем инвентаре')
    print("УБЕРИТЕ ВСЕ ВСПЛЫВАЮШИЕ ПРИЛОЖЕНИЯ И УВЕДОМЛЕНИЯ!")
    print("Ваша раскладка клавиатуры должна быть на ЛАТИНИЦЕ!")
    print("В Standoff 2 необходимо, чтобы никто вам ничего НЕ ПИСАЛ и НЕ ПРИГЛАШАЛ в лобби!")
    print("Не трогайте и не взаимодействуйте (если нет необходимости) мышь и клавиатуру!")
    time.sleep(10)

    pyautogui.moveTo(1000, 500)  #тащим курсор к скинам для дальнейшей прокрутки для сортировки ячеек в инвентаре
    time.sleep(1)

    pyautogui.scroll(150)
    time.sleep(1)

    checkMessageSellBuy()
    pyautogui.click(518, 148) #здесь просто сортировка предметов в инвентаре на удобный для sell()
    pyautogui.click(1000, 150)
    pyautogui.click(1000, 150)
    time.sleep(1)

    checkMessageSellBuy()
    pyautogui.click(612, 47) #сброс верхнего меню сортировки предметов(ячеек) в инвентаре
    pyautogui.click(276, 50)
    time.sleep(1)

    while True:
        pyautogui.click(205, 199)  #клик по ячейке в инвентаре
        pyautogui.click(180, 43)  #клик по инвентарю, чтобы сбросить вспомогательное меню
        time.sleep(1)

        screenshot = pyautogui.screenshot()
        loadedScreenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        region_x = 129
        region_y = 114
        region_width = 345
        region_height = 230
        region = loadedScreenshot[region_y:region_y + region_height, region_x:region_x + region_width]  #region ячейки со скином в инвентаре
        cv2.imwrite("D:\\Start\\SellCellInventar.png", region)
        best_match = None
        max_val = 0
        for name, image in loadedStart.items():
            value, loc = find_best_match(image, region)
            if value is not None and value > max_val:
                max_val = value
                max_loc = loc
                best_match = name
        if max_val >= rangeValue:
            print(f"Нашел нужную ячейку в инвентаре - {best_match}👍")
            pyautogui.click(205, 199)  #клик по этой ячейке
            time.sleep(1)

            screenshot = pyautogui.screenshot()
            loadedScreenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            similarity = cv2.matchTemplate(loadedScreenshot, marketplaceFind, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(similarity)
            if max_val >= rangeValue:
                top_left = max_loc
                height, width, _ = marketplaceFind.shape
                center_x = top_left[0] + width // 2
                center_y = top_left[1] + height // 2
                checkMessageSellBuy()
                pyautogui.click(center_x, center_y)  #найти на рынке
                time.sleep(3)

                checkPrikolError()
            else:
                print("Не нашел кнопку -> Найти на рынке!❌")
                break

            pyautogui.click(372, 844) #продать
            time.sleep(3)

            checkPrikolError()
            pyautogui.click(257, 277) #выбор самой ячейки для продажи
            pyautogui.click(1466,980) #кнопка выбрать
            time.sleep(3)

            checkPrikolError()
            pyautogui.click(1296, 441) #ввод цены
            with open(startFile, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith(best_match):
                        sellPrice = float(line.split()[1])
                        sellPrice = sellPrice - 0.01 #чтобы продавалось хоть как-нибудь :0
                        print(f"Ячейка {best_match} должна продаваться за {sellPrice:.2f} голды")
                        break
            pyautogui.write(f"{sellPrice:.2f}")
            time.sleep(1)

            checkPrikolError()
            pyautogui.click(695, 705) #убрать кликом от ввода цены
            time.sleep(1)

            checkPrikolError()
            pyautogui.click(953, 727) #финальная кнопка продажи ячейки
            time.sleep(3)

            checkPrikolError()
            pyautogui.click(200, 80)  #все назад
            pyautogui.click(200, 80)
            pyautogui.click(200, 80)
            pyautogui.click(200, 80)
            time.sleep(3)

        else:
            print("Нужная ячейка в инвентаре не найдена!❌")
            time.sleep(1)

            pyautogui.click(200, 80)  #все назад
            pyautogui.click(200, 80)
            pyautogui.click(200, 80)
            pyautogui.click(200, 80)
            break

# def resell(): ДОБАВИТЬ ПРОВЕРКУ НА PRIKOL ERROR! ОТКОММЕНТИРОВАТЬ КЛИКИ И ОТШЛИФОВАТЬ КОД!
#     print(f"Вызвана функция по перепродаже ячеек из инвентаря⚙️")
#     time.sleep(1)
#
#     print("Перейдите в свой инвентарь в Bluestacks 5 -> Standoff 2 -> f11 (для полноэкранного режима). У вас 10 секунд!")
#     print('Вы преждевременно не должны были ничего не ставить на продажу и на закупку, убрать лишние "NEW" скины и экипировать нужные предметы в своем инвентаре')
#     print("УБЕРИТЕ ВСЕ ВСПЛЫВАЮШИЕ ПРИЛОЖЕНИЯ И УВЕДОМЛЕНИЯ!")
#     print("Ваша раскладка клавиатуры должна быть на ЛАТИНИЦЕ!")
#     print("В Standoff 2 необходимо, чтобы никто вам ничего НЕ ПИСАЛ и НЕ ПРИГЛАШАЛ в лобби!")
#     print("Не трогайте и не взаимодействуйте (если нет необходимости) мышь и клавиатуру!")
#     time.sleep(10)
#
#     checkMessageSellBuy()
#     pyautogui.click(1000, 40)  #рынок
#     time.sleep(1)
#
#     checkMessageSellBuy()
#     pyautogui.click(670, 140)  #мои запросы
#     time.sleep(1)
#
#     while True:
#         screenshot = pyautogui.screenshot()
#         loadedScreenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
#         region_x = 515
#         region_y = 204
#         region_width = 345
#         region_height = 230
#         region = loadedScreenshot[region_y:region_y + region_height, region_x:region_x + region_width]  #region ячейки со скином
#         cv2.imwrite("D:\\Start\\SellCell.png", region)
#         best_match = None
#         max_val = 0
#         for name, image in loadedStart.items():
#             value, loc = find_best_match(image, region)
#             if value > max_val:
#                 max_val = value
#                 best_match = name
#         if max_val >= rangeValue:
#             print(f"Нашел нужную ячейку - {best_match}👍")
#             pyautogui.click(686, 313)  #клик по этой ячейке
#             pyautogui.click(794, 224)  #отменить запрос
#             pyautogui.moveTo(1000, 500) #перетащим курсор подальше от нужной области
#             time.sleep(3)
#
#         else:
#             print("Нужная ячейка не найдена!❌")
#             time.sleep(1)
#
#             pyautogui.click(200, 80) #все назад
#             pyautogui.click(200, 80)
#             pyautogui.click(200, 80)
#             pyautogui.click(200, 80)
#             time.sleep(3)
#
#             pyautogui.moveTo(1000,500) #тащим курсор к скинам для дальнейшей прокрутки для сортировки ячеек в инвентаре
#             time.sleep(1)
#
#             pyautogui.scroll(150)
#             time.sleep(1)
#
#             checkMessageSellBuy()
#             pyautogui.click(518, 148)
#             pyautogui.click(1000, 150)
#             pyautogui.click(1000, 150)
#             time.sleep(1)
#
#             checkMessageSellBuy()
#             pyautogui.click(612, 47)
#             pyautogui.click(276, 50)
#             time.sleep(1)
#             break
#     while True:
#         pyautogui.click(205, 199)  #клик по ячейке в инвентаре
#         pyautogui.click(180, 43)  #клик по инвентарю, чтобы сбросить вспомогательное меню
#         time.sleep(1)
#
#         screenshot = pyautogui.screenshot()
#         loadedScreenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
#         region_x = 129
#         region_y = 114
#         region_width = 345
#         region_height = 230
#         region = loadedScreenshot[region_y:region_y + region_height, region_x:region_x + region_width]  #region ячейки со скином в инвентаре
#         cv2.imwrite("D:\\Start\\SellCellInventar.png", region)
#         best_match = None
#         max_val = 0
#         for name, image in loadedStart.items():
#             value, loc = find_best_match(image, region)
#             if value > max_val:
#                 max_val = value
#                 max_loc = loc
#                 best_match = name
#         if max_val >= rangeValue:
#             print(f"Нашел нужную ячейку в инвентаре - {best_match}👍")
#             pyautogui.click(205, 199)  #клик по этой ячейке
#             time.sleep(1)
#
#             screenshot = pyautogui.screenshot()
#             loadedScreenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
#             similarity = cv2.matchTemplate(loadedScreenshot, marketplaceFind, cv2.TM_CCOEFF_NORMED)
#             min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(similarity)
#             if max_val >= rangeValue:
#                 top_left = max_loc
#                 height, width, _ = marketplaceFind.shape
#                 center_x = top_left[0] + width // 2
#                 center_y = top_left[1] + height // 2
#                 checkMessageSellBuy()
#                 pyautogui.click(center_x, center_y)  #найти на рынке
#                 time.sleep(3)
#             else:
#                 print("Не нашел кнопку - Найти на рынке!❌")
#
#             pyautogui.click(372, 844) #продать
#             time.sleep(3)
#
#             pyautogui.click(257, 277) #выбор самой ячейки для продажи
#             pyautogui.click(1466,980) #кнопка выбрать
#             time.sleep(3)
#
#             pyautogui.click(1296, 441) #ввод цены
#             with open(startFile, "r") as file:
#                 lines = file.readlines()
#                 for line in lines:
#                     if line.startswith(best_match):
#                         sellPrice = line.split()[1]
#                         print(f"Ячейка {best_match} должна продаваться за {sellPrice} голды")
#                         break
#             pyautogui.write(str(sellPrice))
#             time.sleep(1)
#             pyautogui.click(695, 705) #убрать кликом от ввода цены
#             time.sleep(1)
#
#             pyautogui.click(953, 727) #финальная кнопка продажи ячейки
#             time.sleep(3)
#
#             pyautogui.click(200, 80)  #все назад
#             pyautogui.click(200, 80)
#             pyautogui.click(200, 80)
#             pyautogui.click(200, 80)
#             time.sleep(3)
#
#         else:
#             print("Нужная ячейка в инвентаре не найдена!❌")
#             time.sleep(1)
#
#             pyautogui.click(200, 80)  #все назад
#             pyautogui.click(200, 80)
#             pyautogui.click(200, 80)
#             pyautogui.click(200, 80)
#             break

def switchFirst():
    print(f"Вызвана функция по смене аккаунта на первый⚙️")
    time.sleep(1)

    print("Перейдите в свой инвентарь в Bluestacks 5 -> Standoff 2 -> f11 (для полноэкранного режима). У вас 10 секунд!")
    print('Вы преждевременно не должны были ничего не ставить на продажу и на закупку, убрать лишние "NEW" скины и экипировать нужные предметы в своем инвентаре')
    print("УБЕРИТЕ ВСЕ ВСПЛЫВАЮШИЕ ПРИЛОЖЕНИЯ И УВЕДОМЛЕНИЯ!")
    print("Ваша раскладка клавиатуры должна быть на ЛАТИНИЦЕ!")
    print("В Standoff 2 необходимо, чтобы никто вам ничего НЕ ПИСАЛ и НЕ ПРИГЛАШАЛ в лобби!")
    print("Не трогайте и не взаимодействуйте (если нет необходимости) мышь и клавиатуру!")
    time.sleep(10)

    pyautogui.click(53, 840)  #настройки
    checkMessageSellBuy()
    pyautogui.click(1098, 125)  #авторизация
    pyautogui.moveTo(1000, 500)  #тащим курсор на безопасное место для скроллинга
    pyautogui.scroll(-150)
    time.sleep(1)

    pyautogui.click(1700, 900)  #выйти из аккаунта
    time.sleep(15)

    pyautogui.click(717, 940) #выбор какой акк Google или Facebook
    time.sleep(3)

    pyautogui.click(751, 560)  #первый акк
    time.sleep(20)

    pyautogui.click(49, 379)  #в инвентарь

def switchSecond():
    print(f"Вызвана функция по смене аккаунта на второй⚙️")
    time.sleep(1)

    print("Перейдите в свой инвентарь в Bluestacks 5 -> Standoff 2 -> f11 (для полноэкранного режима). У вас 10 секунд!")
    print('Вы преждевременно не должны были ничего не ставить на продажу и на закупку, убрать лишние "NEW" скины и экипировать нужные предметы в своем инвентаре')
    print("УБЕРИТЕ ВСЕ ВСПЛЫВАЮШИЕ ПРИЛОЖЕНИЯ И УВЕДОМЛЕНИЯ!")
    print("Ваша раскладка клавиатуры должна быть на ЛАТИНИЦЕ!")
    print("В Standoff 2 необходимо, чтобы никто вам ничего НЕ ПИСАЛ и НЕ ПРИГЛАШАЛ в лобби!")
    print("Не трогайте и не взаимодействуйте (если нет необходимости) мышь и клавиатуру!")
    time.sleep(10)

    pyautogui.click(53, 840)  #настройки
    checkMessageSellBuy()
    pyautogui.click(1098, 125)  #авторизация
    pyautogui.moveTo(1000, 500)  #тащим курсор на безопасное место для скроллинга
    pyautogui.scroll(-150)
    time.sleep(1)

    pyautogui.click(1700, 900)  #выйти из аккаунта
    time.sleep(15)

    pyautogui.click(717, 940)  #выбор какой акк Google или Facebook
    time.sleep(3)

    pyautogui.click(751, 670) #второй акк
    time.sleep(20)

    pyautogui.click(49, 379)  #в инвентарь

########################################################################################################################

sell()
# while True:
#     switchSecond()
#     sell()
#     switchFirst()
#     sell()
#     order("dusk")
#     order("fiend")
#     order("cold_lead")
#     order("aurora")
#     order("peaceful_dream")
#     order("pixelV2")
#     order("powergame")
#     order("pursuit")
#     order("rhino")
#     order("scale")
#     order("silver_plated")
#     order("tropic")
#     order("vector")
#     order("vesper_haze")
#     order("vhs")
#     order("zap")
#     switchSecond()
#     order("dusk")
#     order("fiend")
#     order("cold_lead")
#     order("aurora")
#     order("peaceful_dream")
#     order("pixelV2")
#     order("powergame")
#     order("pursuit")
#     order("rhino")
#     order("scale")
#     order("silver_plated")
#     order("tropic")
#     order("vector")
#     order("vesper_haze")
#     order("vhs")
#     order("zap")
#     time.sleep(900)
