use std::fs::File;
use std::io::{prelude::*, BufReader};

fn part1() -> i32 {
    let file = File::open("data.txt").expect("Unable to open the file");
    let reader = BufReader::new(file);

    let mut count = 0;
    for line in reader.lines() {
        match line {
            Ok(val) => {
                let p: Vec<&str> = val.split(",").collect();
                let a: Vec<&str> = p[0].split("-").collect();
                let b: Vec<&str> = p[1].split("-").collect();
                if a[0].parse::<i32>().unwrap() <= b[0].parse::<i32>().unwrap() && a[1].parse::<i32>().unwrap() >= b[1].parse::<i32>().unwrap() 
                    || b[0].parse::<i32>().unwrap() <= a[0].parse::<i32>().unwrap() && a[1].parse::<i32>().unwrap() <= b[1].parse::<i32>().unwrap() {
                    count+=1;
                }

            },
            Err(_e) => {}
        };


    }
    return count;
}

fn part2() -> i32 {
    let file = File::open("data.txt").expect("Unable to open the file");
    let reader = BufReader::new(file);

    let mut count = 0;
    for line in reader.lines() {
        match line {
            Ok(val) => {
                let p: Vec<&str> = val.split(",").collect();
                let a: Vec<&str> = p[0].split("-").collect();
                let b: Vec<&str> = p[1].split("-").collect();
                if a[1].parse::<i32>().unwrap() >= b[0].parse::<i32>().unwrap() && a[0].parse::<i32>().unwrap() <= b[1].parse::<i32>().unwrap() {
                    count+=1;
                }

            },
            Err(_e) => {}
        };


    }
    return count;
}

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}
