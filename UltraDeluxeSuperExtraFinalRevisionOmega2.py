
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


def create_data_structure(string_input):
    network = {}
    trigger = True
    friends = []
    sentences = string_input.split('.')
    game_sentences = []
    connection_sentences = []
    usernames = []
    if string_input in(' ', ''):
        return {}
    
    for e in sentences:
        if trigger:
            connection_sentences.append(e)
            trigger = False
        else:
            game_sentences.append(e)
            trigger = True
     
    trigger = True
    ############ Get list of users ###############
    for each in connection_sentences:
        whitespace = each.find(' ',0)
        username = each[0:whitespace]
        usernames.append(username)
        
  #############create network###################3     
    for user in usernames:
        if user:
            network[user] = {'Friends':[],'Games':[]}
    
##############fill network with friends#################
    for sentence in connection_sentences:
        sentence = sentence.translate(None,',')
        for word in sentence.split():
            currentuser = sentence.split()[0] 
            if word not in(currentuser,'is','connected','to'):
                network[currentuser]['Friends'].append(word)
    ###################### fill network with games ###################
    for phrase in game_sentences:
        trigger = True
        whitespace = phrase.find(' ',0)
        user = phrase[0:whitespace]
        start = phrase.find('play',0) + 5
        phrase = phrase[start:]
        gamelist = []
        for game in phrase.split(','):
            if game.find(' ') is 0:
                gamelist.append(game[1:])
            else:
                gamelist.append(game)
                
        network[user]['Games'] = gamelist
    return network
                
                
        
        
            
                              
                             
                
        
        




def get_connections(network, user):
    if user in network:
        return network[user]['Friends']
    else:
        return None
      

def get_games_liked(network,user):
    if user in network.keys():
        return network[user]['Games']
    else:
        return None


def add_connection(network, user_A, user_B):
    if user_A in network:
        if user_B in network:
            if user_B not in get_connections(network,user_A):
                get_connections(network,user_A).append(user_B)
            return network
        else:
            return False
    else:
        return False

def add_new_user(network, user, games):
    if user in network:
        print 'UNCHANGED'
        return network
    else:
        network[user] = {'Friends':[],'Games':games}
        return network
    
 def get_secondary_connections(network, user):
    secondary_connections = []
    secondary_connections_final = []
    if user in network:
        network[user]['Friends of Friends'] = []
        connections = get_connections(network,user)
        for connection in connections:
            secondary_connections.append(network[connection]['Friends'])
        for each in secondary_connections:
            for username in each:
                if username not in secondary_connections_final:
                    secondary_connections_final.append(username)
                    network[user]['Friends of Friends']= secondary_connections_final
        return network[user]['Friends of Friends']
    else:
        return None
                                                   
                
            
    
def connections_in_common(network, user_A, user_B):
    counter = 0
    if (user_A not in network) or (user_B not in network):
        return False
    else:
        A_friends = get_connections(network,user_A)
        B_friends = get_connections(network,user_B)
        for friend in A_friends:
            if friend in B_friends:
                counter += 1
        return counter
        
def path_to_friend(network,user_A,user_B,path = None):
    if (user_A not in network) or (user_B not in network) or (user_A is user_B):
        return None

    if path is None:
        path = []
    path = path + [user_A]

    if user_B in get_connections(network,user_A):
        return path + [user_B]

    for node in get_connections(network,user_A):
        if node not in path:
            newpath = path_to_friend(network, node, user_B, path)
            if newpath:
                return newpath
    return None


def games_in_common(network,user_A,user_B):
    if user_A not in network or user_B not in network or user_A is user_B:
        return None
    gamelist = []
    Agames = get_games_liked(network,user_A) 
    Bgames = get_games_liked(network,user_B)
    for game in Agames:
        if game in Bgames:
            gamelist.append(game)
    if gamelist:
        return gamelist
    else:
        return None
