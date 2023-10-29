import csv
import sys

def scourging(file1, file2):
    try:
        data = []
        with open(file1, 'r', newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name'].split(',')
                data.append({"first": name[1].strip(), "last": name[0].strip(), "house": row['house']})
        with open(file2,'w', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except FileNotFoundError:
        sys.exit('File not found')

def main():
    if len(sys.argv) != 3:
        sys.exit('Invalid number of arguments')
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    if not file1.endswith('csv') or not file2.endswith('csv'):
        sys.exit('Invalid file type')

    scourging(file1, file2)

if __name__ == '__main__':
    main()