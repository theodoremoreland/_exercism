pub fn raindrops(n: u32) -> String {
    let mut sound: String = String::new();
    
    if n % 3 == 0 {
        sound += &"Pling";
    }

    if n % 5 == 0 {
        sound += &"Plang";
    }

    if n % 7 == 0 {
        sound += &"Plong";
    }

    if sound == "" {
        return n.to_string()
    }

    return sound;
}
