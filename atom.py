def count_electrons(n, k, x, i):
  """
  این تابع تعداد الکترون‌های یک اتم را محاسبه می‌کند.

  Args:
    n: 0 اگر اتم یون نباشد و 1 اگر اتم یون باشد.
    k: بار یون.
    x: عدد جرمی.
    i: عدد اتمی.

  Returns:
    تعداد الکترون‌ها.
  """

  if n == 0:
    return i
  else:
    if k > 0:
      return i + k
    else:
      return i


def count_protons(i):
  """
  این تابع تعداد پروتون‌های یک اتم را محاسبه می‌کند.

  Args:
    i: عدد اتمی.

  Returns:
    تعداد پروتون‌ها.
  """

  return i


def count_neutrons(x, i):
  """
  این تابع تعداد نوترون‌های یک اتم را محاسبه می‌کند.

  Args:
    x: عدد جرمی.
    i: عدد اتمی.

  Returns:
    تعداد نوترون‌ها.
  """

  return x - i


def count_electron_shells(i):
  """
  این تابع تعداد لایه‌های الکترونی یک اتم را محاسبه می‌کند.

  Args:
    i: عدد اتمی.

  Returns:
    تعداد لایه‌های الکترونی.
  """

  shells = 0
  while i >= 2:
    i //= 2
    shells += 1
  return shells


def main():
  """
  این تابع تابع اصلی برنامه است.
  """

  n = int(input())
  if n == 0:
    k = None
  else:
    k = int(input())
  x = int(input())
  i = int(input())

  protons = count_protons(i)
  electrons = count_electrons(n, k, x, i)
  neutrons = count_neutrons(x, i)
  shells = count_electron_shells(i)

  print("Protons:", protons)
  print("Electrons:", electrons)
  print("Neutrons:", neutrons)
  print("Layers:", shells)


if __name__ == "__main__":
  main()
