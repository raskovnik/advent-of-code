use std::fs::File;
use std::io::{prelude::*,BufReader};

fn part1() -> i32 {
    let file = File::open("data.txt").expect("Unable to open file");
    let mut m: i32 = 0;
    let mut s: i32 = 0;

    let reader = BufReader::new(file);
    for line in reader.lines() {
        let num = match line {
            Ok(num) => num,
            Err(_e) => return -1,
        };
        if num == "" {
            if s > m {
                m = s;
           }
           s = 0;
        } else {
            s += num.to_string().parse::<i32>().unwrap();
        }
    }
    return m;
}

fn get_min_index(array: [i32; 3]) -> usize {
    return array.iter()
    .position(|&x| x == match array.iter().min() {
        Some(x) =>*x,
        None => -1,
    }).unwrap();
}

fn part2() -> i32 {
    let file = File::open("data.txt").expect("Unable to open file");
    let mut m: usize = 0;
    let mut s: i32 = 0;
    let mut carry: [i32; 3] = [0, 0, 0];

    let reader = BufReader::new(file);
    for line in reader.lines() {
        let num = match line {
            Ok(num) => num,
            Err(_e) => return -1,
        };
        if num == "" {
            if s > carry[m] {
                carry[m] = s;
                m = get_min_index(carry);
           }
           s = 0;
        } else {
            s += num.to_string().parse::<i32>().unwrap();
        }
    }
    if s > carry[m] {
        carry[m] = s;
    }

    return IntoIterator::into_iter(carry).sum();
}

fn main() {
    println!("{}", part1());
    println!("{}",part2());
}
