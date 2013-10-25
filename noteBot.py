from fBot_library import fBot
import random

version = 0.8

bot = fBot('Cassandra', 'michcioperz.Users.AfterNET.Org')
bot.debug('0')
bot.init('irc.afternet.org')

bot.debug_msg(1, '%s initialized on %s' % (bot.nick, bot.net))

#greetingDone = 0
taken = ['MrGame64', 'bluefoxgs', 'MarcoSpiess']
friends = ['michcioperz', 'antonijn', 'antonjin', 'SuperHawksman', 'iandioch', 'Zanzlanz', 'Caroline', 'Luna','terrabyte_aura']
morethan = ['antobot']
while 1:
    message, parameter, nick, host = bot.react('')

#    if greetingDone != 1:
#        greetingDone = 1
#        bot.message("Heeeeeey peoplez <3 :*")

    if bot.command('!!ATLITS'):
        if parameter in ['system;start']:
            bot.message('http://www.youtube.com/watch?v=LrjiW0TAspk <3');
        if parameter in ['vectors']:
            bot.message('http://www.youtube.com/watch?v=JKLDvnfDmlM <3');
        if parameter in ['euphemia']:
            bot.message('http://www.youtube.com/watch?v=grHD49PJHig <3');
        if parameter in ['knightmare/frame']:
            bot.message('http://www.youtube.com/watch?v=Mq-yLC7wyKs <3');
        if parameter in ['tokyo house party']:
            bot.message('http://www.youtube.com/watch?v=UC1do2pAc0c <3');
        if parameter in ['shi no barado']:
            bot.message('http://www.youtube.com/watch?v=uBP4psAfrT4 <3');
        if parameter in ['cassandra (pt ii)']:
            bot.message('http://www.youtube.com/watch?v=7BAcIP2V_l4 <3');
        if parameter in ['the strays']:
            bot.message('http://www.youtube.com/watch?v=EZ_g-FDSsAk <3');
        if parameter in ['dream & reality']:
            bot.message('http://www.youtube.com/watch?v=S8u1j1rRdio <3');
        if parameter in ['heaven-piercing giga drill']:
            bot.message('http://www.youtube.com/watch?v=-V1oD1h6hvk <3');
        if parameter in ['bosozoku symphonic']:
            bot.message('http://www.youtube.com/watch?v=E5MXV0GwwhU <3');

    if bot.command('Cassandra, can you hear me?'):
        bot.message('Yes.')

    if bot.command('Are you ready to begin?'):
        bot.message('Yes, I\'m ready.')

    if bot.get_action('murders') or bot.get_action('kills') or bot.get_action('brutally beats') or bot.get_action('beats') or bot.get_action('punches') or bot.get_action('kicks'):
        bot.message("%s: Make love, not war, honey" % (nick))

    if bot.command('hi %s' % (bot.nick)) or bot.command('hello %s' % (bot.nick)):
        bot.message('Hi %s! :*' % (nick))
    
    if bot.command('!!AreYouSure'):
        bot.action('is %s%% sure' % (random.randint(0,100)))
    
    if bot.command('!!IsCool'):
        if parameter in morethan:
            bot.action('is too shy to talk about that')
        else:
            bot.action('thinks %s is cool indeed' % (parameter))
    
    if bot.command('!!IsAwesome'):
        if parameter in morethan:
            bot.action('is too shy to talk about that')
        else:
            bot.action('thinks %s is awesome indeed' % (parameter))

    if bot.command('!!Dance'):
        bot.action('dances %s' % (parameter))
        
    if bot.command('!!Bosozoku', 1):
        bot.kill('Cassandra says bye! <3')
    
    if bot.command('!!Talk', 1):
        bot.message(parameter)

    if bot.command('!!Query', 1):
        bot.query(parameter)

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

    if bot.get_action('kisses %s' % (bot.nick)):
        if nick in morethan:
            bot.action('kisses %s %s' % (nick, random.choice(['like there\'s no tomorrow','for a long time'])))
        elif nick in friends:
            bot.action('kisses %s %s' % (nick, random.choice(['like a friend','friendly','on the cheek'])))
        elif nick in taken:
            bot.message('%s: Nah, I can\'t do it to her.' % (nick))
        else:
            bot.message('%s: I think I don\'t know you... yet ;)' % (nick))
