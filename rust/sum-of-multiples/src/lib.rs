use std::collections::HashSet;

pub fn sum_of_multiples(limit: u32, factors: &[u32]) -> u32 {
    let mut set: HashSet<u32> = HashSet::new();

    for factor in factors {
        let mut multiplier: u32 = 1;

        while (factor > &0) && (factor * multiplier) < limit {
            
            set.insert(factor * multiplier);

            multiplier = multiplier + 1;
        }
    }

    set.iter().sum()
}
