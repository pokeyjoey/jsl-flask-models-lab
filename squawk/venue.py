class Venue():
    __table__ = 'venues'
    columns = ['id', 'foursquare_id', 'name', 'price',
               'rating', 'likes', 'menu_url']

    def __init__(self, values):
        breakpoint()
        self.__dict__ = dict(zip(columns, values))
