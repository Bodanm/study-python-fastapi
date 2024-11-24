class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count} {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

j = Journal()
j.add_entry("I ate today")
j.add_entry("I slept yesterday")
j.add_entry("I slept today")
j.remove_entry(0)
print(f"Count of enries:\n{j}")