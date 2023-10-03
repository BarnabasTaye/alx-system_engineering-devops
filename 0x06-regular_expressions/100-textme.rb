#!/usr/bin/env ruby
# Print from to and flags strings
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
