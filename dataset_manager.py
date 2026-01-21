class DataSet:
    def __init__(self, numeric_file, category_file, threshold=50):
        self.numeric_file = numeric_file
        self.category_file = category_file
        self.threshold = threshold
        self.data = []
        self.categories = set()

    def load_data(self):
        try:
            with open(self.numeric_file, "r") as f:
                content = f.read().strip()
                if content == "":
                    print("Numeric file is empty!")
                    return False

                values = content.replace(",", " ").split()
                for v in values:
                    try:
                        self.data.append(float(v))
                    except:
                        print("Invalid value skipped:", v)

                if len(self.data) == 0:
                    print("No valid numbers found!")
                    return False

        except FileNotFoundError:
            print("Number file not found.")
            return False

        try:
            with open(self.category_file, "r") as f:
                content = f.read().strip()
                if content != "":
                    values = content.replace(",", " ").split()
                    for v in values:
                        self.categories.add(v)
        except FileNotFoundError:
            print("Category file not found.")

        return True

    def calculate_total(self):
        total = 0
        for n in self.data:
            total += n
        return total

    def calculate_average(self):
        return self.calculate_total() / len(self.data)

    def calculate_minimum(self):
        min_val = self.data[0]
        for n in self.data:
            if n < min_val:
                min_val = n
        return min_val

    def calculate_maximum(self):
        max_val = self.data[0]
        for n in self.data:
            if n > max_val:
                max_val = n
        return max_val

    def display_results(self):
        total = self.calculate_total()
        average = self.calculate_average()
        minimum = self.calculate_minimum()
        maximum = self.calculate_maximum()

        print("\n--- REPORT ---")
        print("Total:", total)
        print("Average:", average)
        print("Minimum:", minimum)
        print("Maximum:", maximum)

        if average >= self.threshold:
            print("Performance: High Performance")
        else:
            print("Performance: Needs Improvement")

        print("Unique categories:", len(self.categories))

        with open("report.txt", "w") as f:
            f.write("--- REPORT ---\n")
            f.write(f"Total: {total}\n")
            f.write(f"Average: {average}\n")
            f.write(f"Minimum: {minimum}\n")
            f.write(f"Maximum: {maximum}\n")
            f.write(f"Unique categories: {len(self.categories)}\n")

        print("\nSaved as report.txt")


dataset = DataSet("numbers.txt", "categories.txt", 50)

if dataset.load_data():
    dataset.display_results()