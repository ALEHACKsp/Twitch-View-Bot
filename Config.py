class config:
    Channel_URL = "https://www.twitch.tv/brucesefis"
    """
    How many Views per proxy: integer 1-10 recommended: 5
    """
    Proxy_Multipler = 1
    """
    Randomness between each view
    """
    Random_Multiplier = 8
    """
    How long it will wait for each ping to get a reply (In milliseconds)
    """
    Ping_Timeout = 350
    """
    Name of the text file with all the proxies
    """
    Proxy_File = "Proxies.txt"



    class extras:
        class Proxy_Joke:
            Proxy_Joke_Extra = True

    # noinspection PyMethodParameters
    @staticmethod
    def start():
        print(f"""
        {bcolors.OKGREEN}-----Settings-----{bcolors.ENDC}
        {bcolors.OKBLUE}Proxy_Multipler {bcolors.Yellow}= {config.Proxy_Multipler}  **How many Views per proxy: integer 1-10 recommended: 5**{bcolors.ENDC}
        
        
        {bcolors.OKBLUE}Random_Multiplier {bcolors.Yellow}= {config.Random_Multiplier} **Randomness between each view**{bcolors.ENDC}
        
        
        {bcolors.OKBLUE}Channel_URL {bcolors.Yellow}= {config.Channel_URL} **URL of the twitch streamer's channel**{bcolors.ENDC}

        
        {bcolors.OKBLUE}Ping_Timeout {bcolors.Yellow}= {config.Ping_Timeout} **How long to wait for a response while testing proxies (In milliseconds)** **Recommended 500**{bcolors.ENDC}
        
        
        {bcolors.OKBLUE}Proxy_File {bcolors.Yellow}= {config.Proxy_File} **Name of the text file with all the proxies**{bcolors.ENDC}
        {bcolors.OKGREEN}------------------{bcolors.ENDC}
        """)


class advancedConfig:

    headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}


class bcolors:
    ResetAll = "\033[0m"

    Bold       = "\033[1m"
    Dim        = "\033[2m"
    Underlined = "\033[4m"
    Blink      = "\033[5m"
    Reverse    = "\033[7m"
    Hidden     = "\033[8m"

    ResetBold       = "\033[21m"
    ResetDim        = "\033[22m"
    ResetUnderlined = "\033[24m"
    ResetBlink      = "\033[25m"
    ResetReverse    = "\033[27m"
    ResetHidden     = "\033[28m"

    Default      = "\033[39m"
    Black        = "\033[30m"
    Red          = "\033[31m"
    Green        = "\033[32m"
    Yellow       = "\033[33m"
    Blue         = "\033[34m"
    Magenta      = "\033[35m"
    Cyan         = "\033[36m"
    LightGray    = "\033[37m"
    DarkGray     = "\033[90m"
    LightRed     = "\033[91m"
    LightGreen   = "\033[92m"
    LightYellow  = "\033[93m"
    LightBlue    = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan    = "\033[96m"
    White        = "\033[97m"

    BackgroundDefault      = "\033[49m"
    BackgroundBlack        = "\033[40m"
    BackgroundRed          = "\033[41m"
    BackgroundGreen        = "\033[42m"
    BackgroundYellow       = "\033[43m"
    BackgroundBlue         = "\033[44m"
    BackgroundMagenta      = "\033[45m"
    BackgroundCyan         = "\033[46m"
    BackgroundLightGray    = "\033[47m"
    BackgroundDarkGray     = "\033[100m"
    BackgroundLightRed     = "\033[101m"
    BackgroundLightGreen   = "\033[102m"
    BackgroundLightYellow  = "\033[103m"
    BackgroundLightBlue    = "\033[104m"
    BackgroundLightMagenta = "\033[105m"
    BackgroundLightCyan    = "\033[106m"
    BackgroundWhite        = "\033[107m"




    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'
