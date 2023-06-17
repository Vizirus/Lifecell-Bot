import logging
import Sorting as s
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import  KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, Message
#Змінні бота
i = 0
Price = 0
Internet = ""
Minute = ""
MinuteForAll = ""
Token = "6225653555:AAE3-YTelOGWLk9ys74oq2YVDvZle6vRBuM"
log = logging.basicConfig(filename="Botlogs.log", level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p %Z")
bot = Bot(token=Token)
Disp = Dispatcher(bot)
#Кнопки для реп кейбоард
YesButton = KeyboardButton(text="Так")
NoButton = KeyboardButton(text="Ні")
replyMarkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(YesButton, NoButton)
#Кнопки для інлайн кейбоард
AllTarif = InlineKeyboardButton(text="Усі тарифи", callback_data="AllTarifOP")
ChooseTarif = InlineKeyboardButton(text="Підібрати тариф", callback_data="ChooseTarifOP")
previousButton = InlineKeyboardButton(text="⏮", callback_data="PreviousClick")
nextButton = InlineKeyboardButton(text="⏭", callback_data="NextClick")
#Функції
sortClass = s.SortingClass()
@Disp.callback_query_handler(text = ["PreviousClick", "NextClick"])
async def handler(call: types.CallbackQuery):
  global i
  if call.data == "NextClick":
    i += 1 
    if i > len(result):
      i = 0
    if i < len(result):
      await  bot.edit_message_text(text=f"Назва тарифу: {result[i][0]} \n Ціна тарифу: {result[i][1]} \n Кількість Інтернету {result[i][2]} \n Кількість хвилин на дзвінки: {result[i][3]} \n Опис тарифу: {result[i][4]} \n Кількість хвилин на інші оператори: {result[i][5]} \n Посилання на сайт для активації: {result[i][6]}",chat_id=call.message.chat.id , message_id=call.message.message_id,  reply_markup=allMarkup)
   
  elif call.data=="PreviousClick":
    i -= 1
    if i < 0:
      i = len(result)
    if i >= 0:
      await bot.edit_message_text(text=f" Назва тарифу: {result[i][0]} \n Ціна тарифу: {result[i][1]} \n Кількість Інтернету {result[i][2]} \n Кількість хвилин на дзвінки: {result[i][3]} \n Опис тарифу: {result[i][4]} \n Кількість хвилин на інші оператори: {result[i][5]} \n Посилання на сайт для активації: {result[i][6]}",chat_id=call.message.chat.id , message_id=call.message.message_id,  reply_markup=allMarkup)
    
@Disp.message_handler(commands=["start"])
async def echo_test(message: types.Message):
  keyboardLine = InlineKeyboardMarkup().add(AllTarif, ChooseTarif)
  await message.answer("Добрий день! Ласкаво просимо до чат боту Lifecell! Оберіть, яку операцію ви хочете провести...", reply_markup=keyboardLine)
@Disp.callback_query_handler(text = ["AllTarifOP", "ChooseTarifOP"])
async def callBack(call: types.CallbackQuery):
  global allMarkup
  global result
  allMarkup = InlineKeyboardMarkup().add(previousButton, nextButton)
  if call.data == "AllTarifOP":
    await call.message.answer("Ось усі наші тарифи")
    result = sortClass.GetAll()
    await call.message.answer(f"Назва тарифу: {result[i][0]} \n Ціна тарифу: {result[i][1]} \n Кількість Інтернету {result[i][2]} \n Кількість хвилин на дзвінки: {result[i][3]} \n Опис тарифу: {result[i][4]} \n Кількість хвилин на інші оператори: {result[i][5]} \n Посилання на сайт для активації: {result[i][6]}", reply_markup=allMarkup)
  elif call.data == "ChooseTarifOP":
    await call.message.answer("І так, давайте оберемо для вас тариф, але перед цим давайте я вам покажу тарифи, які відсортовані за деякими критеріями, може ви зможте підібрати щось для себе...\n Почнемо з відсортованих об'єму Інтернета")
    result = sortClass.SortByInternet()
    await call.message.answer(f"Назва тарифу: {result[i][0]} \n Ціна тарифу: {result[i][1]} \n Кількість Інтернету {result[i][2]} \n Кількість хвилин на дзвінки: {result[i][3]} \n Опис тарифу: {result[i][4]} \n Кількість хвилин на інші оператори: {result[i][5]} \n Посилання на сайт для активації: {result[i][6]}", reply_markup=allMarkup)
    await call.message.answer("Тепер відсортовані по хвилинам...")
    result = sortClass.SortByMinute()
    await call.message.answer(f"Назва тарифу: {result[i][0]} \n Ціна тарифу: {result[i][1]} \n Кількість Інтернету {result[i][2]} \n Кількість хвилин на дзвінки: {result[i][3]} \n Опис тарифу: {result[i][4]} \n Кількість хвилин на інші оператори: {result[i][5]} \n Посилання на сайт для активації: {result[i][6]}", reply_markup=allMarkup)
    await call.message.answer("І на останок, відсортовані за ціною")
    result = sortClass.SortByPrice()
    await call.message.answer(f"Назва тарифу: {result[i][0]} \n Ціна тарифу: {result[i][1]} \n Кількість Інтернету {result[i][2]} \n Кількість хвилин на дзвінки: {result[i][3]} \n Опис тарифу: {result[i][4]} \n Кількість хвилин на інші оператори: {result[i][5]} \n Посилання на сайт для активації: {result[i][6]}", reply_markup=allMarkup)
    await call.message.answer("Вам щось сподобалось?", reply_markup=replyMarkup)
@Disp.message_handler()
async def YesNo(message: types.Message):
  global allMarkup
  global result
  if message.text=="Так":
    await message.answer("Сподіваюсь, вам спободобалось користуватись мною!")
  elif message.text == "Ні":
    await message.answer("Сподіваюсь, я зможу вам допомогти наступного разу!")
    

if __name__ == "__main__":
  executor.start_polling(Disp)
