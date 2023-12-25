def distance(speed, time):
  """
  این تابع مسافت پیموده شده را با توجه به سرعت و زمان محاسبه می کند.

  Args:
    speed: سرعت بر حسب کیلومتر بر ساعت
    time: زمان بر حسب دقیقه

  Returns:
    مسافت پیموده شده بر حسب کیلومتر
  """

  return round(speed * time / 60, 1)


def speed(distance, time):
  """
  این تابع سرعت ماشین را با توجه به مسافت و زمان محاسبه می کند.

  Args:
    distance: مسافت بر حسب متر
    time: زمان بر حسب دقیقه

  Returns:
    سرعت ماشین بر حسب کیلومتر بر ساعت
  """

  return round(distance * 60 / time, 1)


def time(distance, speed):
  """
  این تابع مدت زمانی که طول می کشد تا ماشین به مقصد برسد را با توجه به مسافت و سرعت محاسبه می کند.

  Args:
    distance: مسافت بر حسب متر
    speed: سرعت ماشین بر حسب کیلومتر بر ساعت

  Returns:
    مدت زمان بر حسب ساعت
  """

  return round(distance / speed * 60 / 60, 1)


def fuel(distance, fuel_per_100km):
  """
  این تابع مقدار سوخت مصرفی را با توجه به مسافت و مصرف سوخت در هر ۱۰۰ کیلومتر محاسبه می کند.

  Args:
    distance: مسافت بر حسب متر
    fuel_per_100km: مصرف سوخت خودرو در هر ۱۰۰ کیلومتر بر حسب لیتر

  Returns:
    مقدار سوخت مصرفی بر حسب لیتر
  """

  return round(distance / 1000 / fuel_per_100km, 1)


def main():
  # ورودی را از کاربر دریافت کنید
  n = int(input())
  commands = []
  for _ in range(n):
    commands.append(input().split())

  # خروجی را چاپ کنید
  for command in commands:
    if command[0] == "distance":
      print(f"{distance(*command):.1f}km")
    elif command[0] == "speed":
      print(f"{speed(*command):.1f}km/h")
    elif command[0] == "time":
      print(f"{time(*command):.1f}h")
    elif command[0] == "fuel":
      print(f"{fuel(*command):.1f}L")


if __name__ == "__main__":
  main()
