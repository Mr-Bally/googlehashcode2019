import sys
from photo import Photo
import networkx as nx

def main(input_file):
    horizontal_photos = []
    vertical_photos = []

    with open(input_file) as file:
        numberOfPhotos = int(file.readline().strip('\n'))

        index = 0
        while index < numberOfPhotos:
            currentPhoto = file.readline().strip('\n').split(" ")

            orientation = currentPhoto[0]

            numberOfTags = int(currentPhoto[1])
            tags = []
            for i in range(numberOfTags):
                tags.append(currentPhoto[i + 2])

            if orientation == "H":
                horizontal_photos.append(Photo(index, orientation, tags))
            else:
                vertical_photos.append(Photo(index, orientation, tags))

            index += 1

    vertical_graph = nx.Graph()



    for vertical_photo in vertical_photos:
        # print(vertical_photo.id)
        vertical_graph.add_node(vertical_photo.id)
    i = 0
    for index in range (len(vertical_photos)):
        best_weight = 0
        best_index = 0
        print(i)
        i = i +1
        for index2 in range (index+1, len(vertical_photos)):
            weight = resolve_score(vertical_photos[index].tags, vertical_photos[index2].tags)
            if weight > best_weight:
                best_weight = weight
                best_index = index2

        vertical_graph.add_weighted_edges_from([(vertical_photos[index].id, vertical_photos[best_index].id, best_weight)])

    print(vertical_graph.edges(data=True))




def resolve_score(a,b):
    a = set(a)
    b = set(b)
    return min([len(a.intersection(b)), len(a.difference(b)), len(b.difference(a))])



if __name__ == "__main__":
    main(sys.argv[1])
