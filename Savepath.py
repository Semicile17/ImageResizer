import csv
def SaveImagePathToCsv(imagePath):
    with open("ImagePaths.csv",  "a") as f:
        writer = csv.writer(f)
        writer.writerow([imagePath])