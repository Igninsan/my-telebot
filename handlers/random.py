from aiogram import Router, types
from aiogram.filters import Command
from random import randint


random_router = Router()

salad_ezhik_recipe = 'Салат Ёжик. Яйца сварить вкрутую и остудить в холодной воде. Колбасу и яйца нарезать кубиками. Сыр натереть на тёрке. Соединить колбасу, сыр, яйца и кукурузу (без жидкости). Чеснок очистить и выдавить через чеснокодавилку. Заправить салат майонезом и перемешать все ингредиенты.'
borsch_recipe = 'Борщ. Сварить бульон и процедить его. В готовый бульон отправить нарезанный картофель и варить его минут 15. Выкладываем в сковороду с растительным маслом нарезанную свеклу, морковь и измельченный чеснок, сладкий перец, лук и помидор. В томатную пасту добавляем немного воды, размешиваем. Добавляем сахар и немного соли, выливаем к овощам. Накрываем крышкой и тушим 10 минут. Поджарку отправляем в кастрюлю, добавляем специи. В самом конце приготовления отправляем в кастрюлю капусту, лавровый лист и зелень.'
omelette_recipe = 'Омлет. Разбейте в глубокую чашку яйца и добавьте молока. Взбейте вилкой или венчиком. Посолите. Разогрейте на сковороде растительное или сливочное масло и вылейте полученную массу. Обжаривайте омлет с обеих сторон. '

recipe_list = [salad_ezhik_recipe, borsch_recipe, omelette_recipe]

salad_ezhik_image = types.FSInputFile("images/ёжик.jpg")
borsch_image = types.FSInputFile("images/борщ.jpg")
omelette_image = types.FSInputFile("images/омлет.jpg")

image_list = [salad_ezhik_image, borsch_image, omelette_image]

@random_router.message(Command('random'))
async def random_handler(message: types.Message):
    random_recipe = randint(0, len(recipe_list) - 1)
    await message.answer_photo(photo=image_list[random_recipe], caption=recipe_list[random_recipe])

