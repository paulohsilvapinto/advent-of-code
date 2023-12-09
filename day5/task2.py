from commons.utils import read_input


def parse_seed_ranges(almanac):
    seeds_row_numbers = almanac[0].split(": ")[1].split()
    seeds_row_numbers = [int(seed) for seed in seeds_row_numbers]

    seed_ranges = []
    for idx in range(0, len(seeds_row_numbers) - 1, 2):
        seed_ranges.append(range(seeds_row_numbers[idx], seeds_row_numbers[idx] + seeds_row_numbers[idx + 1]))

    return seed_ranges


def parse_reversed_translations(almanac):
    translator = {}
    for line in almanac[1:]:
        if line == "\n":
            pass
        elif "map:" in line:
            line_split = line.split("-to-")
            conversion_source = line_split[1].split()[0]
            conversion_destination = line_split[0]

            translator[conversion_source] = {"target": conversion_destination, "conversions": list()}
        else:
            source_start, destination_start, range_length = tuple([int(val) for val in line.split()])
            translator[conversion_source]["conversions"].append(
                {
                    "destination_range": range(destination_start, destination_start + range_length),
                    "source_range": range(source_start, source_start + range_length),
                },
            )

    return translator


def get_seed_for_location(location, translator):
    convert_from_category = "location"
    convert_from_value = location
    # debug_string = f"{convert_from_category}: {convert_from_value}"

    while convert_from_category != "seed":
        convert_to_category = translator[convert_from_category]["target"]
        converted_value = None

        for conversion in translator[convert_from_category]["conversions"]:
            if convert_from_value in conversion["source_range"]:
                offset = convert_from_value - conversion["source_range"][0]
                converted_value = conversion["destination_range"][0] + offset
                break

        if converted_value is None:
            converted_value = convert_from_value

        # debug_string += f", {convert_to_category}: {converted_value}"
        convert_from_category = convert_to_category
        convert_from_value = converted_value

    # print(debug_string)
    return converted_value


almanac = read_input(day_number=5)
seed_ranges = parse_seed_ranges(almanac)
translator = parse_reversed_translations(almanac)

location = 0
while True:
    potential_seed = get_seed_for_location(location, translator)
    # print(f"Location {location}, potential seed {potential_seed}")
    if any(potential_seed in seed_range for seed_range in seed_ranges):
        print(location)
        break
    location += 1
