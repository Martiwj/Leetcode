impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        
        let a_parsed = match u128::from_str_radix(&a, 2) {
            Ok(num) => num,
            Err(_) => return String::from("Invalid input for a"),
        };

        let b_parsed = match u128::from_str_radix(&b, 2) {
            Ok(num) => num,
            Err(_) => return String::from("Invalid input for b"),
        };

        let sum = a_parsed + b_parsed; 

        let binary_string = format!("{:b}", sum); 
        
        binary_string

    }
}