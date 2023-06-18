pub fn is_armstrong_number(num: u32) -> bool {
    let num_string: String = num.to_string();
    let digit_count: usize = num_string.len();
    let mut sum: u128 = 0;

    for digit_char in num_string.chars() {
        let digit: Option<u32> = digit_char.to_digit(10);

        if let Some(digit) = digit {
            sum += u128::pow(digit.into(), digit_count as u32);
        } else {
            panic!("Could not convert {:?} to u32.", digit_char);
        }
    }

    // Compare numbers as u128 in case sum exceeds u32.
    return num as u128 == sum;
}
