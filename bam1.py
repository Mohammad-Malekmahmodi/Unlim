def find_higher_tower(towers, a):
  """
  این تابع ارتفاع اولین برج در سمت راست برج aام را که ارتفاع آن از این برج بلند تر است را پیدا می کند.

  Args:
    towers: یک لیست از ارتفاعات برج ها
    a: شماره برج مورد نظر

  Returns:
    ارتفاع اولین برج در سمت راست برج aام که ارتفاع آن از این برج بلند تر است
  """

  higher_tower = -1
  for i in range(a + 1, len(towers)):
    if towers[i] > towers[a]:
      higher_tower = towers[i]
      break
  return higher_tower


def main():
  # ورودی را از کاربر دریافت کنید
  n = int(input())
  towers = list(map(int, input().split()))

  # برای هر برج، ارتفاع اولین برج در سمت راست آن را که ارتفاع آن از این برج بلند تر است را پیدا کنید
  results = [find_higher_tower(towers, i) for i in range(n)]

  # خروجی را چاپ کنید
  print(*results)


if __name__ == "__main__":
  main()
