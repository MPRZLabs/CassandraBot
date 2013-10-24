#This is the main library file.
#Check out the comments to see what everything does!

#Import, duh.
import socket, string, time

#Create the fBot class
class fBot(object):

    #This is what happens when the class is first called.
    #You may pass 2 values: The name of the bot, and it's boss.
    def __init__(self, Nickname, BossHost=''):
        self.version = 1.2
        
        #Putting the values into variables.
        self.nick = Nickname
        self.boss = BossHost

        #The read buffer.
        self.read = ''

        #Creating a socket.
        self.s = socket.socket()

        #Displaying a message to notify
        #the user that *something* is happening.
        print 'Loading. Please be patient.\n'

    #My self written initialization. Normally, you only
    #need to pass 1 value: The network. You can also
    #specify a different port, though.
    def init(self, Network, Port=6667):
        #Putting the network in a variable.
        self.net = Network        

        #Connect to the network, via the socket we created.
        self.s.connect((Network, Port))

        #User registration:
        #First you send the nick command with the nick you want the bot to have.
        #Then you send user details in this order: USER, IDENT, HOST :Description.
        self.s.send('NICK %s\r\n' % (self.nick))
        self.s.send('USER %s %s bla :%s\r\n' % (self.nick, self.nick, self.nick))      

    #Setting up the debug functionality.
    #You may pass one of three debug output levels,
    #or 'PARAM' which gives back a possible parameter
    #value the he cuts out of each message. (Useful for
    #functions like bot.rename()
    def debug(self, Rating):
        if Rating == 1:
            self.print_debug = 1
        elif Rating == 2:
            self.print_debug = 2
        elif Rating == 3:
            self.print_debug = 3
        elif Rating == 'PARAM':
            self.print_debug = 4
        else:
            self.print_debug = 0

    #The debug_msg function, which allows you to send debug
    #messages to the console. Sends out messages if the print_debug
    #value is equal or greater than it's rating.
    #If you pass PARAM, you only get the parameters, though!
    def debug_msg(self, Rating, Message):
        if not self.print_debug == 4:
            if self.print_debug >= Rating:
                print "DEBUG (Rating: %s) - %s" % (Rating, Message)
        else:
            if self.print_debug == Rating:
                print "DEBUG (Rating: %s) - %s" % (Rating, Message)

    #Makes the bot quit the channel with a certain message. Looks like this:
    # "fBot has left the channel (Quit: ExitMessage)"
    def kill(self, ExitMessage=''):
        self.s.send('QUIT :%s\r\n' % (ExitMessage))
        exit()

    #Joins the specified channel.
    def join(self, Channel):

        #Saves the channel name in a variable.
        self.chan = Channel

        #Joining and showing the chat log header.
        self.s.send('JOIN :%s\r\n' % (self.chan))
        print '\r\n############ CHAT LOG ############\r\n'

    #Send a raw command to the socket.
    def query(self, Query):
        self.s.send(Query)

    #Sends a message to the channel the bot is in.
    def message(self, Message):
        self.query('PRIVMSG %s :%s\r\n' % (self.chan, Message))

    #Sends a private message to the specified user.
    def privmsg(self, Nick, Message):
        self.query('PRIVMSG %s :%s\r\n' % (Nick, Message))

    #Renames the bot to a certain name.
    #The command works like this: fNick <NewNickname>
    def rename(self, Nick):
        self.query('NICK :%s\r\n' % (Nick))

    #Sends a /me action to the channel.
    def action(self, Action):
        self.message('\x01ACTION %s\x01' % (Action))

    #Reads the chat log line by line, and splits it
    #into pieces. Then returns a list of the parts.
    #You can get those with line[i]. It splits when-
    #ever it finds an "empty character". (Space).
    def parse_messages(self):
        self.read = self.read + self.s.recv(1024) 
        temp = string.split(self.read, '\n')
        self.read = temp.pop( )

        for line in temp:
            line = string.rstrip(line)
            line = string.split(line)

        return line

    #The core of the bot. This is where most of the magic happens.
    def react(self,  CommandOperator='.'):
        global host

        #Set the parameter to nothing.
        parameter = ''

        #Setting the Command Operator.
        self.ComOp = CommandOperator

        #Start parsing messages.
        get = self.parse_messages()

        #If debug level 3 is activated, print every line the IRC network sends.
        self.debug_msg(3, string.join(get))

        #If the Message of the Day has been sent by the IRC network,
        #start the joining procedure.
        if get[1] == '005':
            #Join the Team All Hail Noah channel.
            self.join('#GamedevTeam')

            #If debug level 1 is activated, print out, that the bot is now officially parsing messages.
            self.debug_msg(1, 'Bot - %s - is now parsing messages on %s' % (self.nick, self.chan))

        #Pingback to prevent getting disconnected from the network.
        if get[0] == 'PING':
            self.query('PONG %s\r\n' % (get[1]))

        #Try to split the messages into semantic parts.
        try:

            #First take the split list of input and put it back together.
            chat_line = string.join(get)

            #Extract certain parts out of the last message.
            #Extract the nickname of the sender.
            nick = chat_line.split ('!') [ 0 ].replace (':', '')

            #Extract the host of the sender.
            host = chat_line.split(" ")[ 0 ].split("@")[ 1 ]

            #Extract the message of the sender.
            self.msg = chat_line.split(":", 2)[ 2 ].replace('\r\n', '')

            #Try to get a parameter if possible.
            try:
                parameter = string.join(get[4:])
            except IndexError:
                #If it fails, return an empty value.
                parameter = ''
            
        except IndexError:
            #If the splitting totally fails (System messages), return empty values.
            nick, host, self.msg, parameter = '', '', '', ''
            return self.msg, parameter, nick, host

        else:
            #If it succeeds, print the chat log to console.

            #Getting a copy of the original message.
            print_message = self.msg

            #If you find a /me action, format it into a readable text.
            if '\x01ACTION' in print_message:
                action = print_message.replace('\x01ACTION', '')
                print '* %s%s' % (nick, action)
            #If a nick change happens, put it into readable form.
            elif get[1] == 'NICK':
                print "%s is now called %s!" % (nick, print_message)
            else:
                #Otherwise just print what the person said.
                print "%s: %s" % (nick, print_message)
                
            #If debug is PARAM, show what the possible parameter is.
            self.debug_msg(4, "PARAMETER: %s" % parameter)

            #Return the values, so they can be used.
            return self.msg, parameter, nick, host

    #A function to check for commands.   
    def command(self, Command, Rights=0):
        temp = self.ComOp + Command
        temp = string.lower(temp)
        msg = string.lower(self.msg)

        if Rights == 1:
            if host == self.boss:
                if temp in msg:
                    return True
            else:
                pass
        else:
            if temp in msg:
                return True        

    def get_action(self, Action):
        temp = '\x01ACTION '+Action
        temp = string.lower(temp)
        msg = string.lower(self.msg)

        if temp in msg:
            return True
