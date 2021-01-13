import random
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        # USE ADD_USER NUM_USERS TIMES

        # Create friendships
        for i in range(0, num_users):
            self.add_user(f'User {i + 1}')

        # GENERATE ALL FRIENDSHIP COMBINATIONS
        possible_friendships = []

        # AVOID DUPLICATES BY MAKING SURE FIRST NUMBER IS SMALLER THAN SECOND
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # SHUFFLE ALL POSSIBLE FRIENDSHIPS
        random.shuffle(possible_friendships)

        # CREATE FOR FIRST X PAIRS X TOTAL // 2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # * Hint 1: To create N random friendships, you could create a list with all possible friendship combinations, shuffle the list, then grab the first N elements from the list. You will need to `import random` to get shuffle.
        # * Hint 2: `add_friendship(1, 2)` is the same as `add_friendship(2, 1)`. You should avoid calling one after the other since it will do nothing but print a warning. You can avoid this by only creating friendships where user1 < user2.

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # CREATE A QUEUE
        qq = Queue()
        # ENQUEUE USER_ID
        qq.enqueue([user_id])
        # WHILE QUEUE IS NOT EMPTY:
        while qq.size() > 0:
            # DEQUEUE THE FIRST ELEMENT
            print('CURRENT QUEUE', qq.queue)
            connection = qq.dequeue()
            # IF NEWLY APPENDED ELEMENT FROM LINE IS NOT IN VISITED:
            print('CONNECTION', connection)
            if connection[-1] not in visited:
                print('CONNECTION[-1]', connection[-1])
                # ADD IT TO VISITED
                visited[connection[-1]] = connection
                # ENQUEUE CONNECTIIONS
                for friend in self.friendships[connection[-1]]:
                    new_connection = list(connection)
                    new_connection.append(friend)
                    qq.enqueue(new_connection)
        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    # // {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
    connections = sg.get_all_social_paths(1)
    print(connections)
    # // {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}

# 1 CONNECTION TO 2
# 1 -> 8 -> 5 -> 2
# 1 -> 10 -> 2
# 1 -> 5 -> 2

# ______________
#              1
# ______________  

# Visited: 

# _______________________
# [1, 5]  [1, 10]  [1, 8]  
# _______________________  [1]

# Visited: 1:[ 5, 10, 8]

# _____________________________________
# [1, 5]  [1, 10] 
# _____________________________________  [1, 8]

# Visited: 1:[ 5, 10, 8], 8:[]
# ***DON'T ADD [1, 8, 5] BECAUSE 5 IS ALREADY IN VISITED; SAME WITH [1, 8, 1]

# _____________________________________________________________________
# [1, 10, 2]  [1, 10, 6] [1, 5]   
# _____________________________________________________________________  [1, 10]

# Visited: 1, 5, 10, 8, 6, 2
# ***STOPS BECAUSE IT FINDS SHORTEST PATH TO 2 WHICH IS [1, 10, 2]***



# 1 CONNECTION TO 9
# 1 -> 8 -> 5 -> 2
# 1 -> 10 -> 2
# 1 -> 5 -> 2

# ______________
#              1
# ______________  

# Visited: 

# _______________________
# [1, 5]  [1, 10]  [1, 8]  
# _______________________  [1]

# Visited: 1, 5, 10, 8

# _____________________________________
# [1, 5]  [1, 10] 
# _____________________________________  [1, 8]

# Visited: 1, 5, 10, 8

# _____________________________________________________________________
# [1, 10, 2]  [1, 10, 6]  [1, 5]   
# _____________________________________________________________________  [1, 10]

# Visited: 1, 5, 10, 8, 6, 2

# _______________________________________________________________________________________________
# [1, 10, 2]  [1, 10, 6]    
# _______________________________________________________________________________________________  [1, 5]

# Visited: 1, 5, 10, 8, 6, 2

# _______________________________________________________________________________________________
# [1, 10, 2]     
# _______________________________________________________________________________________________  [1, 10, 6]

# Visited: 1, 5, 10, 8, 6, 2

# _______________________________________________________________________________________________
#      
# _______________________________________________________________________________________________  [1, 10, 2]

# Visited: 1, 5, 10, 8, 6, 2

# NO CONNECTIONS: QUEUE BECOMES EMPTY, RETURN NONE