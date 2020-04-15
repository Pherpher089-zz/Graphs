import random


class User:
    def __init__(self, name):
        self.name = name


class Stack:
    def __init__(self):
        self.storage = []

    def push(self, item):
        self.storage.append(item)

    def pop(self):
        if(len(self.storage) > 0):
            return self.storage.pop()
        else:
            return []

    def size(self):
        return len(self.storage)


class Queue():
    def __init__(self):
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            return []

    def size(self):
        return len(self.storage)


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def get_average_friendships(self):
        total_friendships = 0
        for i in range(1, len(self.friendships)):
            total_friendships += len(self.friendships[i])
        average_friendships = total_friendships / len(self.friendships)
        return average_friendships

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
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(1, num_users):
            self.add_user(user)

        # Create friendships
        friends = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, self.last_id + 1):
                friends.append((user, friend))
        # shuffle list of all possible friendships
        random.shuffle(friends)

        # figure number of random friendships for average
        total_friendships = num_users * avg_friendships
        pairs_needed = total_friendships // 2

        random_friendships = friends[:pairs_needed]
        for i in random_friendships:
            self.add_friendship(i[0], i[1])

    def get_friends(self, user_id):
        return self.friendships[user_id]

    def bfs(self, starting_node, target_node):
        q = Queue()
        visited = []
        path = [starting_node]
        q.enqueue((starting_node, path))
        while q.size() > 0:
            current_pair = q.dequeue()
            if current_pair[0] not in visited:
                visited.append(current_pair[0])
                neighbors = self.get_friends(current_pair[0])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        new_path = current_pair[1]
                        new_path.append(neighbor)
                        if neighbor == target_node:
                            return new_path
                        q.enqueue((neighbor, new_path))
        print(f"user: {starting_node} is not connected to user:{target_node}")

    def dft(self, starting_node, visited):
        s = Stack()
        s.push(starting_node)

        while s.size() > 0:
            current_node = s.pop()
            if current_node not in visited:
                visited[current_node] = self.bfs(starting_node, current_node)
                neighbors = self.get_friends(current_node)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        s.push(neighbor)
        return visited

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        self.dft(user_id, visited)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships, sep='\n')
    average_friendships = sg.get_average_friendships()
    print(f"Average number of friends: {average_friendships}")
    connections = sg.get_all_social_paths(1)
    print(connections, sep="\n\n")
