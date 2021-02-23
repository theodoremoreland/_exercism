class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        card_num = self.card_num
        card_num_without_spaces = card_num.replace(" ", "")
        does_contain_only_digits = card_num_without_spaces.isnumeric()
        sum_of_all_digits = 0

        if not does_contain_only_digits:
            return False
        elif card_num_without_spaces == "0":
            return False

        card_num_has_even_number_of_digits = len(card_num_without_spaces) % 2 == 0

        for index, digit in enumerate(card_num_without_spaces):
            current_index_is_even = index % 2 == 0
            should_skip_current_index = (card_num_has_even_number_of_digits and not current_index_is_even) or (not card_num_has_even_number_of_digits and current_index_is_even)
            
            if should_skip_current_index:
                sum_of_all_digits += int(digit)
                continue
            else:
                doubled_num = int(digit) * 2
                luhn_num = doubled_num if doubled_num < 9 else doubled_num - 9
                sum_of_all_digits += luhn_num

        if sum_of_all_digits % 10 == 0:
            return True
        else:
            return False