let get_input () = 
  let input = open_in_bin "input.txt" in
  let content = really_input_string input (in_channel_length input) in
  close_in input;
  content
