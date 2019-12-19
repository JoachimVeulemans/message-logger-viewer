import json
import os
from flask import jsonify
from shutil import copyfile
from datetime import datetime


class FileManager:
    def __init__(self, save_file: str, deleted_location):
        self.save_file = save_file
        self.deleted_location = deleted_location

    def get_json(self):
        f = open(self.save_file, 'r')
        lines = str(f.readlines())
        f.close()
        lines = lines.replace("\\n", "")
        lines = lines.replace("\"", "")
        lines = lines.replace("'", '"')
        print(lines)
        return json.loads(lines)

    def write_lines(self, lines: []):
        for line in lines:
            self.write_line(line)

    def write_line(self, line: str):
        f = open(self.save_file, "a+")
        f.write(str(line) + "\n")
        f.close()

    def clear(self):
        dt_string = datetime.now().strftime("-%d-%m-%Y-%H-%M-%S")
        copyfile(self.save_file, self.deleted_location + "logs" + dt_string + ".txt")
        f = open(self.save_file, "w")
        f.close()
