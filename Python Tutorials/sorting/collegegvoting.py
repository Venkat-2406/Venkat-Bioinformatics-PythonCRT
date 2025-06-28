from collections import deque
import matplotlib.pyplot as plt

class OpenMic:
    def __init__(self):  # ✅ Fixed constructor
        self.performers = []
        self.audience = set()
        self.queue = deque()
        self.votes = {}
        self.voted = {}

    def register(self, name, role):
        if role == "performer" and name not in self.performers:
            self.performers.append(name)
            self.queue.append(name)
            self.votes[name] = 0
        elif role == "audience" and name not in self.audience:
            self.audience.add(name)
            self.voted[name] = set()

    def start(self):
        while self.queue:
            p = self.queue.popleft()
            for a in self.audience:
                if p not in self.voted[a]:
                    vote = input(f"{a}, vote for {p}? (y/n): ").strip().lower()  # ✅ Fixed
                    if vote == "y":
                        self.votes[p] += 1
                        self.voted[a].add(p)

    def winner(self):
        if not self.votes:
            print("No votes cast.")
            return
        max_v = max(self.votes.values())
        winners = [p for p in self.votes if self.votes[p] == max_v]
        for w in winners:
            print(f"🏆 Winner: {w} with {max_v} votes")

    def save(self, file="results.txt"):
        with open(file, "w") as f:
            for p in self.performers:
                f.write(f"{p} - {self.votes[p]} votes\n")
        print(f"Results saved to {file}")

    def chart(self):
        if not self.votes:
            print("No votes to display.")
            return
        names, counts = zip(*self.votes.items())
        plt.bar(names, counts, color='skyblue')
        plt.title("🎤 OpenMic Vote Count")
        plt.ylabel("Votes")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# ✅ Usage
o = OpenMic()
o.register("Alice", "performer")
o.register("Bob", "performer")
o.register("Tom", "performer")
o.register("Jerry", "performer")
o.register("Anu", "audience")
o.register("Ravi", "audience")

o.start()
o.winner()
o.save()
o.chart()
