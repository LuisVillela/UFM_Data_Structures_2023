from Doubly_Linked_List import Node, LinkedList

# insrtion node song-----------------------------------------------------------------------------
song_1 = Node('Song inf:', 1, 'Enter Sandman', 'Metallica', 'Metallica')
song_2 = Node('Song inf:', 2, 'Paranoid', 'Black Sabbath', 'Paranoid')
song_3 = Node('Song inf:', 3, 'Master of Puppets', 'Metallica', 'Master of Puppets')
song_4 = Node('Song inf:', 4, 'Ace of Spades', 'Motörhead', 'Ace of Spades')
song_5 = Node('Song inf:', 5, 'Back in Black', 'AC/DC', 'Back in Black')
song_6 = Node('Song inf:', 6, 'Iron Man', 'Black Sabbath', 'Paranoid')

# Create PLay list ll
ll = LinkedList()
print(ll)

# Insert at beginning----------------------------------------------------------------------------
ll.insert_at_beginning(song_1)
print(ll)
ll.insert_at_beginning(song_2)
print(ll)
ll.insert_at_beginning(song_3)
print(ll)
ll.insert_at_beginning(song_4)
print(ll)

# Insert at end----------------------------------------------------------------------------------
ll.insert_at_end(song_5)
print(ll)

# Insert before----------------------------------------------------------------------------------
ll.insert_before(('Song inf:', 1, 'Enter Sandman', 'Metallica', 'Metallica'), song_6)
print(ll)

song_7 = Node('Song inf:', 7, 'Sweet Child O Mine', 'Guns N Roses', 'Appetite for Destruction')
ll.insert_before(('Song inf:', 4, 'Numb', 'Linkin Park', 'Meteora'), song_7)
print(ll)

# Delete------------------------------------------------------------------------------------------
ll.delete(('Song inf:', 1, 'Enter Sandman', 'Metallica', 'Metallica'))
print(ll)

#FUNCTIONS ---------------------------------------------------------------------------------------

print("Output:")


ll.Play()  

ll.Show_Details()

ll.Next()

ll.Previous()

ll.PlaylistLen()

ll.PlayShuffle()

ll.SearchByName("Iron Man")

ll.SearchByName("Santeria")

ll.SearchByArtist("Guns and Roses")# not in play list

ll.SearchByArtist("Bad bunny")# not in play list

print("Ending PLaylist...")
#Finalizando Play list...........