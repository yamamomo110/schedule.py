schedules = []

while True:

    if schedules:
        print("\n登録済みの予定")
        for i, schedule in enumerate(schedules, start=1):
            print(f"{i}. {schedule['time']} - {schedule['plan']}")
    else:
        print("\n現在登録されている予定はありません")

    plan = input("予定を入力して下さい(終了はexit、削除はdelete):")

    if plan == "exit":
        break

    elif plan == "delete":

        if not schedules:
            print("予定がありません")
            continue
        print("\n登録済みの予定")

        for i, schedule in enumerate(schedules, start=1):
            print(f"{i}. {schedule['time']} - {schedule['plan']}")

        while True:
            delete = input("削除する番号を入力してください: ")
            if not delete.isdigit( ):
                print("数字を入力してください")
                continue

            delete = int(delete)

            if 1 <= delete <= len(schedules):
                schedules.pop(delete -1)
                print(" 削除しました")
                break
    
            else:
                 print("その番号はありません")

        continue
    
    time = input("時間を入力して下さい(例:8:00):")

    time = time.translate(str.maketrans("０１２３４５６７８９：",
                                        "0123456789:"
                                        ))

    schedules.append({
        "plan": plan,
        "time": time 
        })

    schedules.sort(
        key=lambda x: (
        int(x["time"].split(":")[0]),
        int(x["time"].split(":")[1])
        )
        )

print("\n登録した予定")

for schedule in schedules:
        print(schedule["time"], "-", schedule["plan"])
