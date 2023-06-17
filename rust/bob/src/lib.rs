fn is_silence(message: &str) -> bool {
    if message.len() == 0 {
        return true;
    } else {
        let message_without_whitespace: String = message
            .chars()
            .filter(|c| !c.is_whitespace())
            .collect();

        message_without_whitespace.len() == 0
    }
}

fn is_yelling(message: &str) -> bool {
    if is_silence(message) {
        return false;
    }

    let lowercase_version: String = message.to_lowercase();
    let capital_version: String = message.to_uppercase();
    let has_letters: bool = lowercase_version != capital_version;

    has_letters && message == capital_version
}

fn is_asking_question(message: &str) -> bool {
    // Returns either char or None, so return type is Option<char>.
    let last_char_option: Option<char> = message.chars().rev().nth(0);

    // Need to check to see if value is not None before executing boolean expression.
    if let Some(last_char) = last_char_option {
        last_char == '?'
    } else {
        false
    }
}

pub fn reply(message: &str) -> &str {
    let message_without_whitespace: String = message.chars().filter(|c| !c.is_whitespace()).collect();

    if is_yelling(&message_without_whitespace) && is_asking_question(&message_without_whitespace) {
        return "Calm down, I know what I'm doing!";
    }

    if is_yelling(&message_without_whitespace) {
        return "Whoa, chill out!";
    }

    if is_asking_question(&message_without_whitespace) {
        return "Sure.";
    }

    if is_silence(&message_without_whitespace) {
        return "Fine. Be that way!";
    }

    return "Whatever."
}
