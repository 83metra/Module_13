import asyncio

async def start_strongman(name, power):
    print('Силач %s начал соревнования.'%(name))
    for ball in range(1,6):
        await asyncio.sleep(1/power)
        print('Силач {0} поднял {1}-й шар.'.format(name, ball))
    print(f'Силач {name} закончил соревнования!')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Илья Муромец', 10))
    task2 = asyncio.create_task(start_strongman('Добрыня Никитич', 9))
    task3 = asyncio.create_task(start_strongman('Алёша Попович', 7))
    await task1
    await task2
    await task3
    print('Турнир "Асинхронные силачи" по поднятию шаров Атласа окончен!')

asyncio.run(start_tournament())
