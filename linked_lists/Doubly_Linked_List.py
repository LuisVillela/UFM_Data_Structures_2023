import random
class Node:
    '''
    Node object.

    Args:
        data (str): string value to store in node

    Attributes:
        data (str): value stored in node
        next (Node): pointer to next node in list
    '''
    
    def __init__(self, data: str, id: int, name: str, artist: str, album: str):
        self.data = data
        self.id = id
        self.name = name
        self.artist = artist
        self.album = album
        self.next = None
        
    def __repr__(self):
            return '| Song ID: {} | Song Name: {} | Artist: {} | Album: {} |'.format(
                self.id, self.name, self.artist, self.album)


class LinkedList:
    '''
    Linked List object.

    Args:
        None

    Attributes:
        start (Node): pointer to first node in list
    '''

    def __init__(self):
        self.start = None


    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next


    def __repr__(self):
        nodes = ["START"]

        for node in self:
            nodes.append(f"ID: {node.id} | Name: {node.name} | Artist: {node.artist} | Album: {node.album}")

        nodes.append("NIL")
        return " --> ".join(nodes)


    def traverse(self, key):
        '''
        Navigates every node in the list.

        Args:
            None

        Returns:
            None
        '''
        
        current_node = self.start

        while current_node is not None:
            print(current_node)
            current_node = current_node.next


    def traverse_iter(self):
        '''
        Iterates trough the list using the __iter__ method.

        Args:
            None

        Returns:
            None
        '''

        for current_node in self:
            print(current_node)


    def insert_at_beginning(self, new_node: Node):
        '''
        Inserts a node at the start of the linked list.

        Args:
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        new_node.next = self.start
        self.start = new_node


    def insert_at_end(self, new_node: Node):
        '''
        Inserts a node at the end of the linked list.

        Args:
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        if self.start is None:
            self.start = new_node

        else:
            for current_node in self:
                pass

            current_node.next = new_node


    def insert_before(self, reference_node: str, new_node: Node):
        '''
        Inserts a node before the position of the reference node given.

        Args:
            reference_node (str): value of node used as reference
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return

        if self.start.data == reference_node:
            return self.insert_at_beginning(new_node)

        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = new_node
                new_node.next = current_node
                return
            
            previous_node = current_node

        print('Reference node {} not found in Play list...'.format(reference_node))


    def delete(self, reference_node: str):
        '''
        Deletes a node given a value reference.

        Args:
            reference_node (str): value of node used as reference
            
        Returns:
            None
        '''

        if self.start is None:
            print('Empty Play list...')
            return   

        if self.start.data == reference_node:
            self.start = self.start.next
            return
        
        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = current_node.next
                return

            previous_node = current_node

        print('Reference node {} not found in Play list...'.format(reference_node))

    def Play(self):
        
        if self.start is None:
            print('Play list vacía')
            return
        
        print("Starting PLay list: ", self.start.name, " by ", self.start.artist)
        self.current_node = self.start
        
        print("-------------------------------------------------------------------")

    def Show_Details(self):
        
        if self.current_node is None:
            print('Play list vacia, not playing any song')
            return

        print('Song Information: \nID: {}\nNombre: {}\nArtista: {}\nÁlbum: {}'.format(
            self.current_node.id, self.current_node.name, self.current_node.artist, self.current_node.album))
        
        print("-----------------------------------------------------------------")

    def Next(self):
        if self.current_node is None:
            print("No song playig")
            return

        next_node = self.current_node.next

        if next_node is not None:
            print("Reproducing next song:", next_node.name, "by", next_node.artist)
            self.current_node = next_node
        else:
            print("Ending playlist...")
            
        print("\n")
   
    def Previous(self):
        
        if self.current_node is None:
            print("No song playing")
            return
        
        previous_node = None
        for node in self:
            if node == self.current_node:
                break
            previous_node = node

        if previous_node is not None:
            print("Reproduciendo canción previa", previous_node.name, "by", previous_node.artist)
            self.current_node = previous_node
            print("\n")

        else:
            print("Song not found")
            print("\n")
 
    def PlaylistLen(self):

        count = 0
        for node in self:
            count += 1

        return print("Your Play list songs: ", count), print("\n")

    def PlayShuffle(self):
        
        count = 0
        for node in self:
            count += 1
            
        if count == 0:
            print("La playlist está vacia")
            return
        
        random_i= random.randint(0,count  -1 )
        
        node = self.start
        for i in range (random_i):
            node=node.next
            
        self.current_node = node
        print("Shuffled mode: ", self.current_node.name, "by", self.current_node.artist )
        
        print("\n")

    def SearchByName(self, song_name):
        current_node = self.start
        
        while current_node is not None:
            if song_name == current_node.name:
                print("Song", song_name, "found in Play list") 
                print("\n")
                return current_node
            current_node = current_node.next
        
        print("Song: ", song_name, "not found in Play list")
        print("\n")
        return None
            
    def SearchByArtist(self, song_artist):
        current_node = self.start
        
        while current_node is not None:
            if song_artist == current_node.name:
                print("Artista: ", song_artist, " en la Play list") 
                print("\n-")
                return current_node
            current_node = current_node.next
        
        print("Artista: ", song_artist, "no encontrado en la Playl ist")
        print("\n")
        return None
            