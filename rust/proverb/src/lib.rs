pub fn build_proverb(list: &[&str]) -> String {
    let mut proverb: String = String::new();

    for index in 0..list.len() {
        if index == list.len() - 1 {
            break;
        }

        proverb = proverb + &format!("For want of a {} the {} was lost.\n", list[index], list[index + 1]);
    }

    proverb = if list.len() > 0 { proverb + &format!("And all for the want of a {}.", list[0]) } else { proverb };

    return proverb
}
