#!/usr/bin/env ocaml
let () = 
  Sys.readdir "."
  |> Array.to_seq
  |> Seq.filter Sys.is_directory
  |> Seq.map (fun dir -> dir ^ "/input.txt")
  |> Seq.map open_out
  |> Seq.iter close_out
