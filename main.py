import json

def print_log():
    entries = []
    try:
        with open("mission_computer_main.log", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    entries.append(parts)
                    print(f'{parts[0]} | {parts[1]} | {parts[2]}')
                else:
                    print('형식 오류:', line.strip())
    except Exception as e:
        print('오류 발생:', e)
        return

    # reverse
    sorted_entries = sorted(entries, key=lambda x: x[0], reverse=True)
    print('\n[정렬된 로그 출력]')
    for entry in sorted_entries:
        print(f"{entry[0]} | {entry[1]} | {entry[2]}")

    # convert to dict
    keys = ["timestamp", "info", "message"]
    dict_entries = [dict(zip(keys, entry)) for entry in sorted_entries]

    # save as .json
    try:
        with open("parsed_log.json", "w", encoding="utf-8") as json_file:
            json.dump(dict_entries, json_file, ensure_ascii=False, indent=2)
        print('\nJSON 파일로 저장 완료: parsed_log.json')
    except Exception as e:
        print('JSON 저장 오류:', e)

if __name__ == "__main__":
    print_log()