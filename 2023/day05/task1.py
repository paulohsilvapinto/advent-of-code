from commons.utils import read_input


def parse_seeds(almanac):
    seeds = almanac[0].split(": ")[1].split()
    seeds = [int(seed) for seed in seeds]

    return seeds


def parse_translations(almanac):
    translator = {}
    for line in almanac[1:]:
        if line == "":
            pass
        elif "map:" in line:
            line_split = line.split("-to-")
            conversion_source = line_split[0]
            conversion_destination = line_split[1].split()[0]

            translator[conversion_source] = {"target": conversion_destination, "conversions": list()}
        else:
            destination_start, source_start, range_length = tuple([int(val) for val in line.split()])
            translator[conversion_source]["conversions"].append(
                {
                    "source_start": source_start,
                    "source_end": source_start + range_length - 1,
                    "destination_start": destination_start,
                },
            )

    return translator


def get_min_location(seeds, translator):
    min_location = None

    for seed in seeds:
        convert_from_category = "seed"
        convert_from_value = seed
        # debug_string = f"{convert_from_category}: {convert_from_value}"

        while convert_from_category != "location":
            convert_to_category = translator[convert_from_category]["target"]
            converted_value = None

            for conversion in translator[convert_from_category]["conversions"]:
                if conversion["source_start"] <= convert_from_value <= conversion["source_end"]:
                    offset = convert_from_value - conversion["source_start"]
                    converted_value = conversion["destination_start"] + offset
                    break

            if converted_value is None:
                converted_value = convert_from_value

            # debug_string += f", {convert_to_category}: {converted_value}"
            convert_from_category = convert_to_category
            convert_from_value = converted_value

        # print(debug_string)
        if not min_location:
            min_location = converted_value
        else:
            min_location = min(min_location, converted_value)

    return min_location


def solve(input_data):
    almanac = input_data
    seeds = parse_seeds(almanac)
    translator = parse_translations(almanac)
    return get_min_location(seeds, translator)


if __name__ == "__main__":
    input_data = read_input(year=2023, day_number=5)
    print(solve(input_data))
