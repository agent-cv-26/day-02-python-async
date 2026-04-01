import asyncio
import time


async def brew_coffee_async(id):
    print(f"Task {id}: Starting to brew coffee...")
    await asyncio.sleep(3)  # محاكاة انتظار عملية I/O
    print(f"Task {id}: Coffee is ready! (Async)")


async def main():
    start_time = time.perf_counter()

    print("--- Running 5 Async Tasks Simultaneously ---")

    # تحدي اليوم: تشغيل 5 مهام معاً
    await asyncio.gather(
        brew_coffee_async(1),
        brew_coffee_async(2),
        brew_coffee_async(3),
        brew_coffee_async(4),
        brew_coffee_async(5),
    )

    end_time = time.perf_counter()
    print(f"Total time taken for 5 cups: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
