pub fn collatz(n: u64) -> Option<u64> {
    let mut steps: Option<u64> = Some(0);
    let mut current: u64 = n.clone();

    if current == 0 {
        return None;
    }

    while current != 1 {
        if current % 2 == 0 {
            let quotient: Option<u64> = current.checked_div(2);

            if quotient.is_some() {
                current = quotient.unwrap();
            } else {
                return None;
            }
        } else {
            let product: Option<u64> = current.checked_mul(3);

            if product.is_some() {
                let sum: Option<u64> = product.unwrap().checked_add(1);

                if sum.is_some() {
                    current = sum.unwrap();
                } else {
                    return None;
                }
            } else {
                return None;
            }
        }

        steps = Some(steps.unwrap() + 1);
    }

    steps
}
