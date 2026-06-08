import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# The hosting service will securely pass your token here
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# REPLURALIZE THESE WITH YOUR ACTUAL LINKS IN PHASE 3
LINKS = {
    "medicine": os.environ.get('MED_LINK', 'https://t.me/'),
    "dentistry": os.environ.get('DENT_LINK', 'https://t.me/'),
    "pharmacy": os.environ.get('PHARM_LINK', 'https://t.me/'),
    "mls": os.environ.get('MLS_LINK', 'https://t.me/'),
    "nursing": os.environ.get('NURSE_LINK', 'https://t.me/'),
    "none": "https://t.me/charsnas" 
}

@bot.chat_join_request_handler()
def handle_join_request(update: telebot.types.ChatJoinRequest):
    user_id = update.from_user.id
    chat_id = update.chat.id
    
    try:
        # Automatically approve them into the main channel
        bot.approve_chat_join_request(chat_id, user_id)
        
        # Build the 6-button grid menu
        markup = InlineKeyboardMarkup(row_width=2)
        markup.add(
            InlineKeyboardButton("Medicine 💊", url=LINKS["medicine"]),
            InlineKeyboardButton("Dentistry 🦷", url=LINKS["dentistry"]),
            InlineKeyboardButton("Pharmacy 🧪", url=LINKS["pharmacy"]),
            InlineKeyboardButton("MLS 🔬", url=LINKS["mls"]),
            InlineKeyboardButton("Nursing 🩺", url=LINKS["nursing"]),
            InlineKeyboardButton("None ❌", url=LINKS["none"])
        )
        
        # Send the DM menu to the user
        bot.send_message(
            user_id, 
            "Welcome to CharaNas! 🎉\n\nPlease select your specific department channel below to join your community:", 
            reply_markup=markup
        )
    except Exception as e:
        print(f"Error handling request: {e}")

if __name__ == "__main__":
    print("Bot is up and running smoothly...")
    bot.infinity_polling()
