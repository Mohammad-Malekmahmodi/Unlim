def encrypt(text):
    encrypted_text = ""

    for char in text:
        # چک کنید که حرف انگلیسی باشد
        if 'a' <= char <= 'z':
            # رمزگذاری حرف انگلیسی
            encrypted_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            # اگر حرف انگلیسی نیست، بدون تغییر اضافه کنید
            encrypted_char = char

        encrypted_text += encrypted_char

    return encrypted_text

if __name__ == "__main__":
    input_text = input()
    result = encrypt(input_text)
    print(result)
