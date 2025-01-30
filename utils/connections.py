import re
import asyncpg
import asyncio

# Константы для подключения к базе данных
DB_LINK = "postgresql://smartfridgedb_owner:kRe0Hf1josyS@ep-young-dust-a5pvzx3t.us-east-2.aws.neon.tech/smartfridgedb?sslmode=require"
PARAMETER_LIST = re.split(r"[:/\@\?]+", DB_LINK)

DB_PARAMS = {
    "user": PARAMETER_LIST[1],
    "password": PARAMETER_LIST[2],
    "host": PARAMETER_LIST[3],
    "database": PARAMETER_LIST[4],
    "port": PARAMETER_LIST[5] if len(PARAMETER_LIST) > 5 else "5432",  # Порт по умолчанию
    "ssl": "require",  # Указываем SSL
}

async def async_execute_query(query, *parameters):
    connection = None
    try:
        connection = await asyncpg.connect(**DB_PARAMS)
        results = await connection.fetch(query, *parameters)
        return [dict(row) for row in results]
    except Exception as e:
        print(f"Error executing query: {e}")
        raise  # Пробрасываем исключение для дальнейшей обработки
    finally:
        if connection:
            await connection.close()

def execute_query(query, *parameters):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop:
        return loop.run_until_complete(async_execute_query(query, *parameters))
    else:
        return asyncio.run(async_execute_query(query, *parameters))
