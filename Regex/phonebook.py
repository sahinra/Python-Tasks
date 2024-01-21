import re

# Do not modify this list
phone_list = ["98-777-653", "98-742-644", "34-855-326", "34-25-629", "34-489-115", "72-999-563", "9-321-459",
              "72-654-121", "72-4-694", "72-255-313", "98-111-323", "98-433-14", "34-577-342", "98-323-000",
              "98-202-666", "34-5435-454", "34-515-633"]

ugly_phone_list = ["98-333-111", "12--323-566", "123-34-221", "99-948-321", "-12-123-346",
                     "894-58438-543", "85-234-222",
                     "12-333-444-", "99-888--433", "15-465-876", "98-555-22", "-3-355-333", "3--344-53", "--2--45---",
                     "11-111-222", "12#22$34$222", "98 223 555"]


# "These are the valid phone numbers in your phonebook:"
def check_length(lists):
    valid_numbers = []
    invalid_numbers = []
    for p in lists:
        if len(p) != 10:
            invalid_numbers.append(p)
        else:
            valid_numbers.append(p)
    return valid_numbers, invalid_numbers


# "and these are the wrong ones:"


# "The area codes:"
# "and the numbers without the area codes:"
def area_codes_finder(lists):
    area_codes =[]
    numbers = []
    for e in lists:
        area_code, number = e.split("-", 1)
        area_codes.append(area_code)
        numbers.append(number)

    return area_codes, numbers


# "The unique area codes:"
def unique_area_codes(area_codes):
    unique = set()
    for ac in area_codes:
        unique.add(ac)
    return unique


# "You have X numbers from area 98, Y numbers from area 34, and Z numbers from area 72."
def count_area_codes(area_codes):
    count_dict = {}
    for ac in area_codes:
        count_dict[ac] = count_dict.get(ac, 0) + 1
    return count_dict


# "These are the pretty phone numbers:"
# "and these are the ugly ones:"
def valid_pattern(lists):
    valid_numbers = []
    invalid_numbers = []

    for p in lists:
        pattern = re.compile(r'^\d{2}-\d{3}-\d{3}$')
        match = pattern.match(p)

        if match:
            valid_numbers.append(p)
        else:
            invalid_numbers.append(p)

    return valid_numbers, invalid_numbers


def main():
    print("###################  Check the length  ##########################")
    valid_len, invalid_len = check_length(phone_list)
    print(valid_len)
    print(invalid_len)

    print("###################  Area codes  ##########################")
    area_codes, numbers = area_codes_finder(valid_len)
    print(area_codes)
    print(numbers)

    print("###################  Unique area codes  ##########################")
    unique_codes = unique_area_codes(area_codes)
    print(unique_codes)

    print("###################  Count area codes  ##########################")
    area_code_counts = count_area_codes(area_codes)
    for ac, count in area_code_counts.items():
        print(f"You have {count} numbers from area {ac}.")

    print("###################  Valid pattern  ##########################")
    valid_numbers, invalid_numbers = valid_pattern(ugly_phone_list)
    print("Pretty Phone Numbers:", valid_numbers)
    print("Ugly Phone Numbers:", invalid_numbers)


if __name__ == "__main__":
    main()