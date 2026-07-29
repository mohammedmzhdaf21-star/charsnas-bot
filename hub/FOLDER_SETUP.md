# Put channel + bots in one Telegram folder

Telegram **cannot** include bot private chats inside a *shareable* folder invite (`t.me/addlist/...`). That is a Telegram rule, not a bot bug.

## Working setup (this is how communities do it)

### A) Campus group = bots live “in” the folder
1. Create a group: **CharaNas Campus**
2. Add these bots as **admins** (or members):
   - `@Charanaseducenter_bot` (hub)
   - `@CharanasMedicine_bot`
   - `@Charanasdentistry_bot`
   - `@Charanaspharmacy_bot`
   - `@CharanasMLS_bot`
   - `@Charanasnursing_bot`
3. Create invite link for the group → `CAMPUS_GROUP_INVITE` in `hub/.env`
4. Optional: note group id (`-100...`) → `CAMPUS_GROUP_CHAT_ID` then run `/post_campus_menu` in the hub bot

### B) Shared folder = Channel + Campus group
1. Telegram → **Settings → Chat Folders → Create folder** → name `CharaNas`
2. Include: your **channel** + **CharaNas Campus** group
3. **Share folder** → copy `https://t.me/addlist/...`
4. Put in `hub/.env`:
   ```bash
   FOLDER_INVITE_LINK=https://t.me/addlist/XXXX
   CAMPUS_GROUP_INVITE=https://t.me/+YYYY
   FOLDER_NAME=CharaNas
   ```
5. Restart hub

Students tap **Add CharaNas folder** → get channel + campus group (bots are inside the group).

### C) Bot chats in the folder tab (per student)
After opening a department bot once:
**Settings → Chat Folders → CharaNas → Included chats → add that bot**

Then the bot appears as its own chat inside the folder on their phone.
