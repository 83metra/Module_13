from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()

@dp.message_handler(text= 'Calories')
async def set_age(message):
    await message.answer('Введите свой возраст.')
    await UserState.age.set()

@dp.message_handler(state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    date = await state.get_data()
    await message.answer('Введите свой рост.')
    await UserState.growth.set()


@dp.message_handler(state= UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    date = await state.get_data()

    await message.answer('Введите свой вес')
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def set_sex(message, state):
    await state.update_data(weight = message.text)
    date = await state.get_data()
    await message.answer('Введите свой пол (мужчина/женщина)')
    await UserState.sex.set()



@dp.message_handler(state= UserState.sex)
async def send_calories(message, state):
    await state.update_data(sex= message.text)
    date = await state.get_data()
    if 'му' in str(date['sex']).lower():
        result = (int(date['weight']) * 10) + (6.25 * int(date['growth'])) - (int(date['age']) + 5)
        await message.answer('Ваша норма калорий: %s'%(result))
    elif 'же' in str(date['sex']).lower():
        result = (int(date['weight']) * 10) + (6.25 * int(date['growth'])) - (int(date['age']) - 161)
        await message.answer('Ваша норма калорий: {}'.format(result))
    else:
        await message.answer('В нашей стране только два пола - мужчина и женщина! Начните всё с начала!')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
