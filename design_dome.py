def get_pi():
    return 3.141592

# ^
def power(x, y):
    result = 1
    for n in range(y):
        result *= x
    return result

# default setting
def sphere_area(diameter, material='유리', thickness = 1.0):
    radius = diameter / 2
    pi = get_pi()

    area = 2 * pi * power(radius, 2)

    density_dict = {'유리': 2.4,
                    '알루미늄': 2.7,
                    '탄소강': 7.85
                    }
    
    volume = area * thickness
    density = density_dict.get(material, 2.4)
    weight = volume * density / 1000

    # round 3
    area = round(area, 3)
    weight = round(weight, 3)

    # in mars
    mars_gravity_ratio = 3.71 / 9.81
    weight = round(weight * mars_gravity_ratio, 3)

    return material, diameter, thickness, area, weight

# user input
def main():
    material = input('material : ')
    diameter = float(input('diameter : '))
    thickness = float(input('thickness : '))

    material, diameter, thickness, area, weight = sphere_area(diameter, material, thickness)

    # round 3
    print(f'\n재질 => {material}, 지름 => {diameter:.3f}, 두께 => {thickness:.3f}, 면적 => {area:.3f}, 무게 => {weight:.3f}kg')

if __name__ == "__main__":
    main()