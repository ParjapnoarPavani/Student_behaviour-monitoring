import csv

# read flash.dat to a list of lists
data = open("shape_predictor_68_face_landmarks.dat",encoding="utf8")

datContent = [i.strip().split() for i in open("shape_predictor_68_face_landmarks.dat",encoding="utf8").readlines()]

# write it as a new CSV file
with open("flash.csv", "wb",encoding="utf8") as f:
    writer = csv.writer(f)
    writer.writerows(datContent)