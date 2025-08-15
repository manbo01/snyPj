import numpy as np

def load_csv(file):
    try:
        data = np.genfromtxt(file, delimiter=',', skip_header=1, dtype=None, encoding='utf-8')
        return data
    except Exception as e:
        print(f'Error : file load - {file} ({e})')
        return None
    
def main():
    # load file
    arr1 = load_csv('mars_base_main_parts-001.csv')
    arr2 = load_csv('mars_base_main_parts-002.csv')
    arr3 = load_csv('mars_base_main_parts-003.csv')

    if arr1 is None or arr2 is None or arr3 is None:
        print("Error: file load")
        return

    result = []

    try:
        for row1, row2, row3 in zip(arr1, arr2, arr3):
            part_name = row1[0] # same part name
            avg_strength = (row1[1] + row2[1] + row3[1]) / 3
            # average
            if avg_strength < 50:
                result.append((part_name, avg_strength))
    except Exception as e:
        print(f"Error: average ({e})")
        return

    # save
    try:
        with open('parts_to_work_on.csv', 'w', encoding='utf-8') as f:
            f.write('parts, average\n')
            for part, avg in result:
                f.write(f'{part},{avg:.3f}\n')
        print('Success')
    except Exception as e:
        print(f'Error : save ({e})')

main()