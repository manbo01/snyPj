import json

def print_log():
    # new empty list
    entries = [] 
    try:
        with open("Mars_Base_Inventory_List.csv", "r", encoding="utf-8") as file:
            # skip first line
            next(file)
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    try:
                        # dager score check
                        parts[4] = str(float(parts[4]))
                        entries.append(parts)
                        # Substance, Weight, Specific Gravity, Strength, Flammability
                        print(f'{parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]}')
                    except ValueError:
                        print('형식 오류:', line.strip())
                else:
                    print('형식 오류:', line.strip())
    except Exception as e:
        print('오류 발생:', e)
        return

    # Flammability sort
    sorted_entries = sorted(entries, key=lambda x: float(x[4]), reverse=True)

    # Flammability higher than 0.7 sort
    dangerous_items = [item for item in sorted_entries if float(item[4]) >= 0.7]

    # danger item print
    print("\n[인화성 지수 위험]")
    for item in dangerous_items:
        print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}")

    # danger item list to csv
    with open("Mars_Base_Inventory_danger.csv", "w", encoding="utf-8") as danger_file:
        for item in dangerous_items:
            danger_file.write(",".join(item) + "\n")

    # bonus quest
    # save sorted_entries to binary file
    with open("Mars_Base_Inventory_List.bin", "wb") as bin_file:
        for item in sorted_entries:
            line = " | ".join(item) + "\n"
            bin_file.write(line.encode("utf-8"))

    # read and print from binary file
    print("\n[이진 파일]")
    try:
        with open("Mars_Base_Inventory_List.bin", "rb") as bin_file:
            for line in bin_file:
                print(line.decode("utf-8").strip())
    except Exception as e:
        print("이진 파일 읽기 오류:", e)

if __name__ == "__main__":
    print_log()