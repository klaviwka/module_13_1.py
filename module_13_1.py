import asyncio


async def start_strongman(name: str, power: int) -> None:
    """
    Асинхронная функция, представляющая соревнование силача.

    :param name: Имя силача (строка).
    :param power: Мощность силача (целое число), количество шаров, которые он может поднять.
    """
    print(f'Силач {name} начал соревнования.')

    for i in range(1, power + 1):  # Поднимаем количество шаров в соответствии с мощностью
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна силе
        print(f'Силач {name} поднял {i} шар.')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament() -> None:
    """
    Асинхронная функция, запускающая турнир среди силачей.
    """
    # Создаем задачи для трех силачей
    tasks = [
        start_strongman('Pasha', 3),
        start_strongman('Denis', 4),
        start_strongman('Apollon', 5),
    ]

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)


# Запуск асинхронной функции start_tournament
if __name__ == '__main__':
    asyncio.run(start_tournament())
