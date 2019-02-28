import sys
from photo import Photo

def main(input_file):
    with open(input_file) as file:
        numberOfPhotos = int(file.readline().strip('\n'))

        photos = []
        index = 0
        while index < numberOfPhotos:
            currentPhoto = file.readline().strip('\n').split(" ")

            orientation = currentPhoto[0]

            numberOfTags = int(currentPhoto[1])
            tags = []
            for i in range(numberOfTags):
                tags.append(currentPhoto[i + 2])

            photos.append(Photo(index, orientation, tags))

            index += 1


if __name__ == "__main__":
    main(sys.argv[1])
