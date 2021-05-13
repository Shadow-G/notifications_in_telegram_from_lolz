#!usr/bin/python
# -*- coding: utf-8 -*-

import telebot
from telebot import types
from bs4 import BeautifulSoup
from selenium import webdriver

bot = telebot.TeleBot('TOKEN')
user_id = 0000000

driver = webdriver.PhantomJS()

print("Parser is start")

def pars():
	import time

	driver.get("https://lolz.guru/forums/86/")

	time.sleep(60)

	soup = BeautifulSoup(driver.page_source, "html.parser")

	quotes = soup.find_all('div', class_='discussionListItem')

	user = quotes[0].find('span', class_='username').get_text()
	title = quotes[0].find('span', class_='spanTitle').get_text()
	time = quotes[0].find('span', class_='startDate').get_text()
	href = quotes[0].find('a', class_='listBlock')

	date = time.split()
	href = "https://lolz.guru/" + href['href']

	return user, title, time, href, date[2]


upname = ''
parsing = True
while parsing:
	par = pars()
	if par[1] != upname and int(par[4]) == int(2021):
		upname = par[1]

		key = types.InlineKeyboardMarkup() # Создаем раздел для кнопок
		but_3 = types.InlineKeyboardButton(text="Клик", url=par[3]) # Создаем кнопку
		key.add(but_3) # Добавляем кнопку

		bot.send_message(user_id, f'''
Тема: {par[1]}
Автор: {par[0]}
Опубликовано: {par[2]}''', reply_markup=key)