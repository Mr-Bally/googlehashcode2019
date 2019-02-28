
class Photo(object):

    def __init__(self, photo_id, orientation, tags):
        self.id = photo_id
        self.orientation = orientation
        self.tags = tags

    @property
    def number_of_tags(self):
        return len(self.tags)

    def __str__(self):
        return str(self.id)
