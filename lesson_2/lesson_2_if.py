# Как-то получить от пользователя оценку
rate = input(" Оцените работу оператора от 1 до 5: ") # str
rate_as_number = int (rate) # int

# Проверить, что оценка от 1 до 5
if (rate_as_number<1):
    rate_as_number = 1

if (rate_as_number > 5):
    rate_as_number = 5

print (rate_as_number)
# В зависимости от оценки, предложить дать обратную связь
feedback = " "
if rate_as_number == 1:
    feedback = input (" Расскажите, что нам улучшить ?: ")

elif rate_as_number == 2:

    feedback = input (" Расскажите, что вас смутило ?: ")

elif rate_as_number == 3:
        feedback = input (" Расскажите, что нам  улучшить ?: ")

elif rate_as_number ==4:
    feedback = input(" Расскажите, почему не 5 ?: ")

else:
    feedback = input(" Спасибо за отзыв)) ")


print (feedback)
