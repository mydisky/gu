from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BATCH_MESSAGE = BATCH = """
This command is used to short or convert links from first to last posts

Make the bot as an admin in your channel

Command usage: `/batch [channel id or username]`

Ex: `/batch -100xxx`
"""

START_MESSAGE = '''Hello, {}

I'm a nanolinks.in Shortener Bot short Using your API. 

Just Send me Any Post with Mdisk or Other Links. I will Convert Those Links Using Your API and Send them Back To You. I work in Channels too. 

Hit /help for more information about this Bot

Current Method Selected: **{}**

'''


HELP_MESSAGE = '''
Hey! My name is {firstname}. I am a DTGLINKS.IN Shortner bot make your Work Easy and Help you to Earn more 💰.

I have a ton of handy features to help you out, such as:

- [Hyperlink](https://t.me/{username}) support 🔗
- Button conversion support 🔘
- Domain inclusion and exclusion options 🌐
- Header and footer text support 📝
- Replace username function 📎
- Banner image support 🖼️
- Batch conversion for channel admins only 📊
- Channel support for admins only 📢

Helpful commands:

- /start: Starts me! You've probably already used this.
- /help: Sends this message; I'll tell you more about myself!
- /batch -100xxx: To short or convert all posts of your channel
- /shortener_api : add your nanolinks api
- /mdisk_api : add mdisk api
- /base_site : Change bast site
- /header : add header
- /footer : add footer
- /include_domain
- /exclude_domain
- /info
- /username
- /banner_image
- /me

Use the commands to know more about the same

Below are some features I provide'''


ABOUT_TEXT = """
**My Details:**

`🤖 Name:` ** {} **
`✏️ LANGUAGE` : [Python 3](https://www.python.org)
`🧰 FRAMEWORK` : [Pyrogram](https://github.com/pyrogram/pyrogram)
`💾 DATABASE` : [MongoDB](https://cloud.mongodb.com)
`🌀 𝚂𝙴𝚁𝚅𝙴𝚁` : VPS
`📢 Support` : [TGNVS](https:/t.me/tgnvs)

I have lots of features, such as 

- Include domains 
- Exclude domains
- Header and Footer Text support
- Replace Username
- Banner Image
- Buttons convert support
- Batch convert (Admin Only Use)
- Channel Support (Admin Only Use)
- Convert forwarded posts (Admin Only Use)

"""


METHOD_MESSAGE = """
Current Method: {method}
    
Methods Available:

~ `mdlink` - Change all the links of the post to your MDisk account first and then short to DTGLINKS.IN link.

~ `shortener` - Short all the links of the post to nanolinks.in link directly.

To change method, choose it from the following options:
"""

CUSTOM_ALIAS_MESSAGE = """For custom alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/example | Example"""


ADMINS_MESSAGE = """
Sorry only work for admin
"""


CHANNELS_LIST_MESSAGE = """
Sorry only work for admin"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Methods', callback_data=f'method_command'),
        InlineKeyboardButton('Batch', callback_data=f'cbatch_command'),
        
    ],

    [
        InlineKeyboardButton('Custom Alias', callback_data=f'alias_conf'),
        InlineKeyboardButton('Admins', callback_data=f'admins_list'),    
    ],

    [
        
        InlineKeyboardButton('Channels', callback_data=f'channels_list'),
        InlineKeyboardButton('Home', callback_data='start_command')
        
    ],


])


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Home', callback_data=f'start_command'),
        InlineKeyboardButton('Help', callback_data=f'help_command')
    ],
    [
        InlineKeyboardButton('Close', callback_data='delete')
    ]
])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Help', callback_data=f'help_command'),
        InlineKeyboardButton('About', callback_data='about_command')
    ],
        [
        InlineKeyboardButton('Method', callback_data=f'method_command'),
        InlineKeyboardButton('Close', callback_data='delete')
    ],

])

METHOD_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('MDLINK', callback_data=f'change_method#mdlink'),
        InlineKeyboardButton('Shortener', callback_data='change_method#shortener'),
        InlineKeyboardButton("Mdisk", callback_data="change_method#mdisk"),
    ],
        [
        InlineKeyboardButton('Back', callback_data=f'help_command'),
        InlineKeyboardButton('Close', callback_data='delete')
    ],

])

BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'help_command')
    ],

])

USER_ABOUT_MESSAGE = """
🔧 Here are the current settings for this bot:

- 🌐 Shortener website: {base_site}

- 🧰 Method: {method}

- 🔌 {base_site} API: {shortener_api}

- 💾 Mdisk API: {mdisk_api}

- 📎 Username: @{username}

- 📝 Header text:
{header_text}

- 📝 Footer text:
{footer_text}

🖼️ Banner image: {banner_image}
"""


MDISK_API_MESSAGE = """To add or update your Mdisk API, \n`/mdisk_api mdisk_api`
            
Ex: `/mdisk_api 6jZqf51sXoPtugiKQq`
            
Others Mdisk Links will be automatically changed to the API of this Mdisk account

Get your Mdisk API from @VideoToolMoneyTreebot

Current Mdisk API: `{}`"""

SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/shortener_api [api]`
            
Ex: `/shortener_api 9e6082cd45fg37f01bh6631e8j3c60a1bab73a73`

Current Website: {base_site}

Current Shortener API: `{shortener_api}`"""

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

For adding line break use \\n

To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """Reply to the Footer Text You Want

This Text will be added to the bottom of every message caption or text

For adding line break use \\n

To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """Current Username: {username}

Usage: `/username your_username` (without @)

This username will be automatically replaced with other usernames in the post

To remove this username, `/username remove`"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""

INCLUDE_DOMAIN_TEXT = """
Use this option if you want to short only links from the following domains list.

Current Include Domain:
{}
Usage: /include_domain domain
Ex: `/include_domain t.me, stack.com`

To remove a domain,
Ex: `/include_domain remove t.me`

To remove all domains,
Ex: `/include_domain remove_all`
"""

EXCLUDE_DOMAIN_TEXT = """
Use this option if you wish to short every link on your channel but exclude only the links from the following domains list

Current Exclude Domains:
{}
Usage: /exclude_domain domain
Ex: `/exclude_domain t.me, google.com`

To remove a domain, 
Ex: `/exclude_domain remove t.me`

To remove all domains,
Ex: `/exclude_domain remove_all`
"""

BANNED_USER_TXT = """
Usage: `/ban [User ID]`
Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
