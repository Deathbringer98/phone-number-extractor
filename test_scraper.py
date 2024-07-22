import scraper
import data

def test():
    for test_str, expected_nums in zip(data.test_phone_strs, data.test_expected_strs):
        extracted_nums = scraper.get_all_nums(test_str)
        print(f'Line: {test_str}')
        print(f'\tPhones:\t\t{extracted_nums}')
        print(f'\tExpected:\t{expected_nums}')
        assert extracted_nums == expected_nums

# Run the test
test()
