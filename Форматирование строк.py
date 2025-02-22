
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 10717.6
team2_time = 18015.2
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

# Использование %:

print('В команде "Мастера кода" участников: %d!' % team1_num)
print('В команде "Волшебники данных" участников: %d!' % team2_num)
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))

# Использование format():

print('Команда "Мастера кода" решила задач: {}!'.format(score_1))
print('"Мастера кода" решили задачи за {:.1f} с!'.format(team1_time))
print('Команда "Волшебники данных" решила задач: {}!'.format(score_2))
print('"Волшебники данных" решили задачи за {:.1f} с!'.format(team2_time))

# Использование f-строк:

if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды "Мастера кода"!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды "Волшебники данных!"'
else:
    challenge_result = 'Ничья!'

print(f'Команды решили {score_1} и {score_2} задач.')
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!")
