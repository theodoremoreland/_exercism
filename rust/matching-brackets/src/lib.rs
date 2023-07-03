pub fn brackets_are_balanced(string: &str) -> bool {
    let open_brackets: Vec<char> = vec!['[', '{', '('];
    let close_brackets: Vec<char> = vec![']', '}', ')'];
    let mut open_brackets_found: Vec<char> = Vec::new();

    for character in string.chars() {
        if open_brackets.contains(&character) {
            open_brackets_found.push(character);

            continue;
        }
        
        if close_brackets.contains(&character) {
            if character == ']' && open_brackets_found.last() == Some(&'[') {
                open_brackets_found.pop();

                continue;
            }

            if character == '}' && open_brackets_found.last() == Some(&'{') {
                open_brackets_found.pop();

                continue;
            }

            if character == ')' && open_brackets_found.last() == Some(&'(') {
                open_brackets_found.pop();

                continue;
            }

            return false;
        }
    }

    open_brackets_found.is_empty()
}
