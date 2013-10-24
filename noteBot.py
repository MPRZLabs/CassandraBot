from fBot_library import fBot
import random

version = 0.8

bot = fBot('Cassandra', 'michcioperz.Users.AfterNET.Org')
bot.debug(0)
bot.init('irc.afternet.org')

bot.debug_msg(1, '%s initialized on %s' % (bot.nick, bot.net))

boys = ['michcioperz', 'antonijn', 'antonjin', 'SuperHawksman', 'iandioch', 'Zanzlanz']
girls = ['Caroline', 'Luna']
orientation = 'gay'
while 1:
    message, parameter, nick, host = bot.react('')

    if bot.get_action('murders'):
        bot.message("%s: Don't be silly, my dear friend" % (nick))

    if bot.get_action('brutally beats'):
        bot.message("%s: Don't be silly, my dear friend" % (nick))
        
    if bot.get_action('kills'):
        bot.message("%s: Don't be silly, my dear friend" % (nick))

    if bot.command('Hi %s' % (bot.nick)):
        bot.message('Hi %s! :*' % (nick))
    
    if bot.command('!!AreYouSure'):
        bot.action('is %s%% sure' % (random.randint(0,100)))
    
    if bot.command('!!IsCool'):
        bot.action('thinks %s is cool indeed' % (parameter))
    
    if bot.command('!!IsAwesome'):
        bot.action('thinks %s is awesome indeed' % (parameter))

    if bot.command('!!Dance'):
        bot.action('dances %s' % (parameter))
        
    if bot.command('!!Bosozoku', 1):
        bot.kill('Cassandra says bye! <3')
    
    if bot.command('!!Talk', 1):
        bot.message(parameter)

    if bot.command('!!Act', 1):
        bot.action(parameter)

    if bot.command('!!Name', 1):
        bot.rename(parameter)
    
    if bot.command('!!Ident'):
        bot.privmsg(nick, 'You are %s. - Your host is \'%s\'.' % (nick, host))

    if bot.command('!!Version'):
        bot.message('I am %s v%.1f running on top of the fBot framework v%.1f by Folis.' % (bot.nick, version, bot.version))
        
    if bot.get_action('hugs %s' % (bot.nick)):
        actionType = 'tightly', 'lightly', 'for a long time', 'quickly', 'softly', 'firmly'
        bot.action('hugs %s %s.' % (nick, random.choice(actionType)))
        
    if bot.get_action('!!orientation'):
        if orientation == 'gay':
            bot.message("I'm into girls!")
        elif orientation == 'straight':
            bot.message("I'm into boys!")
        
    if bot.get_action('!!gay'):
        orientation = 'gay'
        bot.message("I'm into girls now!")
    
    if bot.get_action('!!straight'):
        orientation = 'straight'
        bot.message("I'm into boys now!")

    if bot.get_action('kisses %s' % (bot.nick)):
        if orientation == 'straight'
            if nick in boys:
                bot.action('kisses %s' % (nick))
            elif nick in girls:
                bot.action('feels confused, but kisses %s like a friend' % (nick))
            else:
                bot.message('%s: Do I even know you? :/' % (nick))
        elif orientation == 'gay'
            if nick in boys:
                bot.action('feels confused, but kisses %s like a friend' % (nick))
            elif nick in girls:
                bot.action('kisses %s' % (nick))
            else:
                bot.message('%s: Do I even know you? :/' % (nick))

    if bot.get_action('kicks %s' % (bot.nick)):
        actionType = 'roundhouse-kicks', 'punches', 'kicks', 'headbutts', 'wrestles'
        bot.action('%s %s.' % (random.choice(actionType), nick))

    if bot.get_action('punches %s' % (bot.nick)):
        actionType = 'roundhouse-kicks', 'punches', 'kicks', 'headbutts', 'wrestles'
        bot.action('%s %s.' % (random.choice(actionType), nick))
