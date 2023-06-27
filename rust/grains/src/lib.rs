pub fn square(s: u32) -> u64 {
    if s < 1 || s > 64 {
        panic!("Square must be between 1 and 64");
    }

    if s == 1 {
        return 1;
    }

    u64::pow(2, s - 1)
}

pub fn total() -> u64 {
    let mut sum: u64 = 1;

    for i in 1..64 {
        sum += u64::pow(2, i);
    }

    sum
}