pub fn series(digits: &str, len: usize) -> Vec<String> {
    let mut sub:  Vec<String> = vec![];
    let digit_count: usize = digits.len();

    for i in 0..digit_count + 1 {
        if i + len > digit_count {
            break;
        }

        if len == 0 {
            sub.push(String::new());

            continue;
        }

        sub.push(digits[i..(i + len)].to_string());
    }

    sub
}
