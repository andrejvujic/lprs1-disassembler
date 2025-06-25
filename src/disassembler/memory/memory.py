import os
import re

from ..constants import DATA_ENTRIES_LOCATION_INDICATOR
from .memory_entry import MemoryEntry


class Memory:
    def __init__(self, data_ram_file_name):
        if data_ram_file_name:
            self.data_ram_file_name = data_ram_file_name
            self.data_ram_file_path = os.path.join(
                os.getcwd(),
                data_ram_file_name,
            )

        self.memory_entries = self.load_memory_entries() if data_ram_file_name else []

    def load_memory_entries(self):
        raw_content = self.load_data_ram_content()

        start_index = raw_content.index(DATA_ENTRIES_LOCATION_INDICATOR)

        memory_entries = []

        for index in range(start_index + 1, len(raw_content)):
            if raw_content[index] == DATA_ENTRIES_LOCATION_INDICATOR:
                break

            matches = re.findall(r'"(.*?)"', raw_content[index])
            if not matches:
                raise Exception("Error while parsing instruction rom!")

            memory_entries.append(MemoryEntry.from_raw_value(matches[0]))

        return memory_entries

    def load_data_ram_content(self):
        with open(self.data_ram_file_path, "r") as f:
            raw_content = f.readlines()
            return raw_content

    def __repr__(self):
        if not self.memory_entries or not len(self.memory_entries):
            return "// You don't have any memory entries!"

        formatted_memory_entries = ""
        for memory_entry in self.memory_entries:
            formatted_memory_entries += f"{memory_entry}\n"
        return formatted_memory_entries
