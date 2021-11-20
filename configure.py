# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 13:35:37 2021

@author: 1 """

import telebot
import cv2 as cv

bot = telebot.TeleBot('2063757848:AAH_a1GZ6L-goFMbVZL9vmgxh_1ySLIWU90')

@bot.message_handler(content_types=['text'])
 
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
       bot.send_message(message.from_user.id, "Какой фильтр наложить на фото? Выберите: erosion, blur, gauss, median, dilation, gray, turn")
    elif message.text == "erosion":
        mesg = bot.send_message(message.from_user.id, "Отправьте изображение")
        bot.register_next_step_handler(mesg, photoErode)
    elif message.text == "blur":
        mesg = bot.send_message(message.from_user.id, "Отправьте изображение")
        bot.register_next_step_handler(mesg, photoBlur)
    elif message.text == "gauss":
        mesg = bot.send_message(message.from_user.id, "Отправьте изображение")
        bot.register_next_step_handler(mesg, photoGauss)
    elif message.text == "median":
        mesg = bot.send_message(message.from_user.id, "Отправьте изображение")
        bot.register_next_step_handler(mesg, photoMedian)
    elif message.text == "dilation":
        mesg = bot.send_message(message.from_user.id, "Отправьте изображение")
        bot.register_next_step_handler(mesg, photoDilation)
    elif message.text == "gray":
        mesg = bot.send_message(message.from_user.id, "Отправьте изображение")
        bot.register_next_step_handler(mesg, photoGray)
    elif message.text == "turn":
        mesg = bot.send_message(message.from_user.id, "Отправьте изображение")
        bot.register_next_step_handler(mesg, photoTurn)
    else:
        bot.send_message(message.from_user.id, "Я вас не понимаю. Напишите /help.")

@bot.message_handler(content_types=["photo"])   
def photoErode(message):
   file_info = bot.get_file(message.photo[0].file_id)
   downloaded_file = bot.download_file(file_info.file_path)
   src = 'C:/Users/1/OneDrive/Desktop/' + message.photo[0].file_id + ".png"
   with open(src, 'wb') as new_file:
       new_file.write(downloaded_file)
   img = cv.imread(src)
   kernel3 = cv.getStructuringElement(cv.MORPH_ELLIPSE, ( 3, 3 ) ) 
   img_erode = cv.erode(img, kernel3)
   cv.imwrite(src, img_erode)
   photo = open(src, 'rb')
   bot.send_photo(message.chat.id, photo )

@bot.message_handler(content_types=["photo"])   
def photoBlur(message):
    file_info = bot.get_file(message.photo[0].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'C:/Users/1/OneDrive/Desktop/' + message.photo[0].file_id + ".png"
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    img = cv.imread(src)
    img_blur = cv.blur(img, (5,5))
    cv.imwrite(src, img_blur)
    photo = open(src, 'rb')
    bot.send_photo(message.chat.id, photo )

@bot.message_handler(content_types=["photo"])   
def photoGauss(message):
    file_info = bot.get_file(message.photo[0].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'C:/Users/1/OneDrive/Desktop/' + message.photo[0].file_id + ".png"
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    img = cv.imread(src)
    img_gauss = cv.GaussianBlur(img, (5, 5), 0)
    cv.imwrite(src, img_gauss)
    photo = open(src, 'rb')
    bot.send_photo(message.chat.id, photo )

@bot.message_handler(content_types=["photo"])   
def photoMedian(message):
    file_info = bot.get_file(message.photo[0].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'C:/Users/1/OneDrive/Desktop/' + message.photo[0].file_id + ".png"
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    img = cv.imread(src)
    img_median = cv.medianBlur(img, 5)
    cv.imwrite(src, img_median)
    photo = open(src, 'rb')
    bot.send_photo(message.chat.id, photo )

@bot.message_handler(content_types=["photo"]) 
def photoDilation(message):
    file_info = bot.get_file(message.photo[0].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'C:/Users/1/OneDrive/Desktop/' + message.photo[0].file_id + ".png"
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    img = cv.imread(src)
    kernel3 = cv.getStructuringElement(cv.MORPH_ELLIPSE, ( 3, 3 ) )
    img_dilation = cv.dilate(img, kernel3)
    cv.imwrite(src, img_dilation)
    photo = open(src, 'rb')
    bot.send_photo(message.chat.id, photo )

@bot.message_handler(content_types=["photo"]) 
def photoGray(message):
    file_info = bot.get_file(message.photo[0].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'C:/Users/1/OneDrive/Desktop/' + message.photo[0].file_id + ".png"
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    img = cv.imread(src)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite(src, img_gray)
    photo = open(src, 'rb')
    bot.send_photo(message.chat.id, photo )

@bot.message_handler(content_types=["photo"]) 
def photoTurn(message):
    file_info = bot.get_file(message.photo[0].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'C:/Users/1/OneDrive/Desktop/' + message.photo[0].file_id + ".png"
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    img = cv.imread(src)
    (h, w, d) = img.shape
    center = (w // 2, h // 2)
    M = cv.getRotationMatrix2D(center, 180, 1.0)
    img_turn = cv.warpAffine(img, M, (w, h))
    cv.imwrite(src, img_turn)
    photo = open(src, 'rb')
    bot.send_photo(message.chat.id, photo )

bot.polling(none_stop=True, interval=0)   


