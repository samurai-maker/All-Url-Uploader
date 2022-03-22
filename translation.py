class Translation(object):
    START_TEXT = """<b>Hi {},
I'm <a href="https://telegra.ph/file/e4a22cfe44b6135bc1ecb.jpg">WWM URL DOWNLOADER</a> !
You can upload </b><i> File or Video </i> <b> to Telegram with direct link, Using me 😊!
/help for more details!</b>"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = "📥Downloading..."
    UPLOAD_START = "📤Uploading..."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using me \n\n<b>Join @world_wide_movies  </b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds.\n\n@world_wide_movies"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    ABOUT_MSG = """ Something About Me :
 ☞Language : Python3
 ☞Library  : <a href="https://docs.pyrogram.org/">Pyrogram 1.0.7</a>"""
    HELP_USER = """<b>Please Follow These steps!</b>
 <i>   
1. Send url (example.domain).
2. Send Image As Custom Thumbnail (Optional).
3. Select the button.
   
 SVideo - Give File as video with Screenshots
 DFile  - Give File (video) as file with Screenshots
 Video  - Give File as video without Screenshots
 File   - Give File without Screenshots </i>

<b>Works with youtube,zee5, sony.live, voot and much more 😋..Try it noW!

@wolrd_wide_movies</b>
"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
You can use /rename command after receiving file to rename it with custom thumbnail support.
"""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
