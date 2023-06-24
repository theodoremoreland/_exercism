
fn get_student_position(student: &str) -> u8 {
    match student {
        "Alice" => return 0,
        "Bob" => return 2,
        "Charlie" => return 4,
        "David" => return 6,
        "Eve" => return 8,
        "Fred" => return 10,
        "Ginny" => return 12,
        "Harriet" => return 14,
        "Ileana" => return 16,
        "Joseph" => return 18,
        "Kincaid" => return 20,
        "Larry" => return 22,
        _ => panic!("Well, that ain't right.")
    }
}

fn get_plant_name(letter: char) -> &'static str {
    match letter {
        'R' => "radishes",
        'C' => "clover",
        'G' => "grass",
        'V' => "violets",
        _ => panic!("Well, that ain't right.")
    }
}

pub fn plants(_diagram: &str, _student: &str) -> Vec<&'static str> {
    let mut student_plants: Vec<&'static str> = vec![];
    // Splits diagram into two rows on the newline.
    let rows: Vec<&str> = _diagram
        .split('\n')
        .collect();
    let _first_row: Vec<char> = rows[0]
        .chars()
        .collect();
    let _second_row: Vec<char> = rows[1]
        .chars()
        .collect();
    let student_position: u8 = get_student_position(_student);

    let first_plant = get_plant_name(_first_row[student_position as usize]);
    let second_plant = get_plant_name(_first_row[(student_position + 1) as usize]);
    let third_plant = get_plant_name(_second_row[student_position as usize]);
    let fourth_plant = get_plant_name(_second_row[(student_position + 1) as usize]);

    student_plants.push(first_plant);
    student_plants.push(second_plant);
    student_plants.push(third_plant);
    student_plants.push(fourth_plant);

    return student_plants;
}
