from fBot_library import fBot
import random

version = 0.8

bot = fBot('michiBot', 'michcioperz.Users.AfterNET.Org')
bot.debug(0)
bot.init('irc.afternet.org')

bot.debug_msg(1, '%s initialized on %s' % (bot.nick, bot.net))

while 1:
    message, parameter, nick, host = bot.react('m')
    
    if bot.command('AreYouSure'):
        bot.action('is %s%% sure' % (random.randint(0,100)))
    
    if bot.command('IsCool'):
        bot.action('thinks %s is cool indeed' % (parameter))
    
    if bot.command('IsAwesome'):
        bot.action('thinks %s is awesome indeed' % (parameter))

    if bot.command('Dance'):
        bot.action('dances')

    if bot.command('Help'):
        bot.privmsg(nick, '--- Commands ---')
        bot.privmsg(nick, 'mCake - %s quits (Can only be issued by owner.)' % (bot.nick))
        bot.privmsg(nick, 'mTalk <text> - Makes %s say <text> (Can only be issued by owner.)' % (bot.nick))
        bot.privmsg(nick, 'mName - Rename %s. (Can only be issued by owner.)' % (bot.nick))
        bot.privmsg(nick, 'mIdent - Receive a query containing your nick and host.')
        bot.privmsg(nick, 'mVersion - Check the version of %s.' % (bot.nick))
        bot.privmsg(nick, '%s also reacts to /me commands: kick, punch and hug' % (bot.nick))
        
    if bot.command('Cake', 1):
        bot.kill('fBot Framework v%.1f written by Folis' % (bot.version))
    
    if bot.command('Talk', 1):
        bot.message(parameter)

    if bot.command('Act', 1):
        bot.action(parameter)

    if bot.command('Name', 1):
        bot.rename(parameter)
    
    if bot.command('Ident'):
        bot.privmsg(nick, 'You are %s. - Your host is \'%s\'.' % (nick, host))

    if bot.command('Version'):
        bot.message('I am %s v%.1f running on top of the fBot framework v%.1f by Folis.' % (bot.nick, version, bot.version))
        
    if bot.get_action('hugs %s' % (bot.nick)):
        actionType = 'tightly', 'lightly', 'for a long time', 'quickly', 'softly', 'firmly'
        bot.action('hugs %s %s.' % (nick, random.choice(actionType)))

    if bot.get_action('kicks %s' % (bot.nick)):
        actionType = 'roundhouse-kicks', 'punches', 'kicks', 'headbutts', 'wrestles'
        bot.action('%s %s.' % (random.choice(actionType), nick))

    if bot.get_action('punches %s' % (bot.nick)):
        actionType = 'roundhouse-kicks', 'punches', 'kicks', 'headbutts', 'wrestles'
        bot.action('%s %s.' % (random.choice(actionType), nick))
