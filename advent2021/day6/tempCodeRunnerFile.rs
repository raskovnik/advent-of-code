        for c in 0..=8 {
            fish[&c] = fish[&(&c + 1)];
        }
        fish.entry(8).unwrap() = temp;
        fish.entry(6).unwrap() += temp;