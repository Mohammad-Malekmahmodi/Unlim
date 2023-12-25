def count_button_presses(n, m):
  """
  این تابع تعداد دفعات فشار دادن دکمه را محاسبه می کند.

  Args:
    n: عدد اولیه
    m: عدد دلخواه

  Returns:
    تعداد دفعات فشار دادن دکمه
  """

  n_len = len(n)
  m_len = len(m)

  if n_len != m_len:
    raise ValueError("طول دو عدد باینری باید برابر باشد.")

  count = 0
  for i in range(n_len):
    if n[i] != m[i]:
      count += 1
    else:
      if i == n_len - 1:
        if n[i] == '0':
          count = n_len

  return count


def main():
  """
  این تابع تابع اصلی برنامه است.
  """

  n = input("عدد اولیه را وارد کنید: ")
  m = input("عدد دلخواه را وارد کنید: ")

  count = count_button_presses(n, m)

  print(f"برای تبدیل {n} به {m} باید {count} بار دکمه را فشار دهید.")


if __name__ == "__main__":
  main()
