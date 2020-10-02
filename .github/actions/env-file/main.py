#!/usr/bin/python3
import sys
import re

if len(sys.argv) == 1:
    sys.exit("Missing input")

envs = sys.argv[1]

print("ENVS", envs)

def parse_escaped_chars(env):
    return re.sub(r"\\(\"|,)",r"\1", env) 
    #return env.replace(r"\",r"")

def parse_input(envs):
    return re.split(r"(?<!\\),", envs)
    #return envs.split(",")

def gen_output(envs):
    return "\n".join(envs)

output = gen_output([parse_escaped_chars(env) for env in parse_input(envs)])
print(output)

