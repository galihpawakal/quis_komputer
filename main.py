print("Selamat Datang Di komputer Quis")

playing = input("Kamu akan bermain game?")


if playing.lower() != "iya":
    quit()

print("okay, Kita akan Bermain")
score = 0

answer = input("apa kepanjangan dari cpu? ")
if answer.lower() == "central processing unit":
    print('Benar!')
    score += 1
else:
    print("salah!")

answer = input("apa kepanjangan dari GPU? ")
if answer.lower() == "graphics processing unit":
    print('Benar!')
    score += 1
else:
    print("salah!")

answer = input("apa kamu suka dia? ")
if answer.lower() == "iya":
    print('Benar!')
    score += 1
else:
    print("salah!")

answer = input("dia itu siapa? ")
if answer.lower() == "hanya teman":
    print('Benar!')
    score += 1
else:
    print("salah!")

print("kamu mendapatkan " + str(score) + " pertanyaan Berhasil!")
print("kamu mendapatkan " + str((score / 4) * 100) + "%.")
