use std::fs;
use std::collections::HashMap;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Unable to read the file");
    let mut days = Vec::<i64>::new();
    for c in contents.split(",") {
        days.push(c.trim().parse().expect(""));
    }
    let mut fish = HashMap::new();
    for i in 0..9 {
         let _ = *fish.entry(i).or_insert(0);
    }
    for day in &days {
        *fish.entry(*day).or_insert(0) += 1;
    }
    
    for _ in 1..=256{
        let temp = fish[&0];
        for c in 0..8 {
            let count = fish[&(&c + 1)];
            fish.insert(c, count);
        }
        *fish.get_mut(&8).unwrap() = temp;
        *fish.get_mut(&6).unwrap() += temp;
    }
    println!("{}", fish.values().sum::<i64>());


}
