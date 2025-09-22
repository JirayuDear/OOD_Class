def leader_board(data):
    answer = []
    for i in data:
        i.append(calculator_point(i[1], i[2], i[3]))
        i.append(goal_diff(i[4], i[5]))

    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j][-2] < data[j+1][-2]:
                data[j], data[j+1] = data[j+1], data[j]
            elif data[j][-2] == data[j+1][-2]:
                if data[j][-1] < data[j+1][-1]:
                    data[j], data[j+1] = data[j+1], data[j]
    for i in data:
        print(f"['{i[0]}', {{'points': {i[-2]}}}, {{'gd': {i[-1]}}}]")

def calculator_point(win, loss, draw):
    return 3*int(win) + 0*int(loss) + 1*int(draw)

def goal_diff(scored, conceded):
    return int(scored)-int(conceded)


inp = input("Enter Input : ").split("/")
print("== results ==")
data = []
for i in inp:
    data.append(i.split(","))
leader_board(data)
