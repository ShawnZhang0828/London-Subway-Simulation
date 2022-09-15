class Line():
    '''
        Line class is used to represent a line in the subway system
    '''

    def __init__(self, id, name, color, stripe):
        '''
            Initialize a class instance
        '''
        self.id = id
        self.name = name
        self.color = color
        self.stripe = stripe if stripe != 'NULL' else None

    def display_info(self):
        '''
            Print all information of a line
        '''
        print(f'id: {self.id} - name: {self.name} - color: {self.color} - stripe: {self.stripe}')