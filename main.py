# Bu proje Pomodoro'nun ikinci deneyi. Bir şifre oluşturma servisi inşa edeceğim.

from hashlib import sha256, sha512

print("Enter the value you want to hash. (sha256)")
A = input("First Value: ")

print(sha256(A.encode('utf-8')).hexdigest())

print("Enter the value you want to hash. (sha512)")
B = input("Second Value: ")

print(sha512(B.encode('utf-8')).hexdigest())

# Çıkarımlar;
# Sanırım sha'nın yanındaki sayılar bir boyutu işaret ediyor çünkü 256.2 512 ediyor ve tam-
# iki katı uzunluğunda. Byte ile ilgili şeyler okudum internette çok düşmedim ve SHA işinde çok yeni-
# olduğum için internetten birinin stackoverflow'da yazdığı şeyi kendi çapımda denedim.

# Öğrenimler;
# "encode", "('utf-8')", print içinde modifikasyon belirtme (sha256 gibi komutları verme), "hexdigest".
