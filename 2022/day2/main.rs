use std::collections::HashMap;
use std::fs::File;
use std::io::{prelude::*, BufReader};

fn score(value: &str) -> String {
    match value {
        "X" => return "1".to_string(),
        "Y" => return "2".to_string(),
        "Z" => return "3".to_string(),
        "A" => return "X".to_string(),
        "B" => return "Y".to_string(),
        "C" => return "Z".to_string(),
        _ => return "".to_string()
    }
}

fn get_score(p1: &str, p2: &str, rules: &HashMap<&str, &str>) -> i32 {
    if score(p2) == p1 {return score(p1).parse::<i32>().unwrap() + 3}
    else if rules.get(p1) == Some(&p2) {return score(p1).parse::<i32>().unwrap() + 6}
    else {return score(p1).parse::<i32>().unwrap()}
}

fn get_choice(p1: &str, game: &str, rules2: &HashMap<&str, &str>) -> String {
    let rules: HashMap<&str, &str> = HashMap::from([
        ("Z", "X"),
        ("X", "Y"),
        ("Y", "Z")
    ]);
    if game == "Y" {return score(p1);}
    else if game == "X" {
        return match rules2.get(p1) {
            Some(x) => x.to_string(),
            _ => "".to_string(),
        };
    }
    else {
        let c = score(p1);
        return match rules.get(c.as_str()) {
            Some(x) => x.to_string(),
            _ => "Error".to_string(),
    };}
}

fn part1(rules: &HashMap<&str, &str>) -> i32 {
    let mut m = 0;
    let file = File::open("test.txt").expect("Unable to open file");
    let reader = BufReader::new(file);
    for line in reader.lines() {
        match line {
            Ok(val) => {
                let p: Vec<&str> = val.split(" ").collect();
                m += get_score(p[1], p[0], rules);
            },
            _ => {}
        };
    }
    return m;
}

fn part2(rules1: &HashMap<&str, &str>, rules2: &HashMap<&str, &str>) -> i32 {
    let mut m = 0;
    let file = File::open("data.txt").expect("Unable to open file");
    let reader = BufReader::new(file);
    for line in reader.lines() {
        match line {
            Ok(val) => {
                let p: Vec<&str> = val.split(" ").collect();
                m += get_score(get_choice(p[0], p[1], rules2).as_str(), p[0], rules1);
            },
            _ => {}
        };
    }
    return m;
}

fn main() {
    let rules1: HashMap<&str, &str> = HashMap::from([
        ("X", "C"),
        ("Z", "B"),
        ("Y", "A"),
    ]);
    
    let rules2: HashMap<&str, &str> = HashMap::from([
        ("A", "Z"),
        ("B", "X"),
        ("C", "Y")
    ]);
    println!("{}",part1(&rules1));
    println!("{}", part2(&rules1, &rules2))
}