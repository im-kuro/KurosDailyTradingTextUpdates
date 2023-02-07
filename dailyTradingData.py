import datetime, json, creds, time
from colorama import Fore, init
from tradingview_ta import TA_Handler
from twilio.rest import Client

init()

def __init__():
    printUtils.printData("Code started... Waiting to start text loop.")
    time.sleep(creds.waitLoopTime)
    runScript()
    

class printUtils:
    def printError(Error: str): print(Fore.RED + f"[X] ERROR => {Error} ")
    def printSuccess(Data: str): print(Fore.GREEN + f"[!] SUCCESS => {Data} ")
    def printData(Data: str): print(Fore.BLUE + f"[!] DATA => {Data} ")


class UtilFuncs:
    
    def getDailyData(symbol: str, exchange: str, screener: str):
        handler = TA_Handler(
        symbol,
        exchange,
        screener,
        interval="1d",
        timeout=None
        
    )
        
        getHanldeAnalysis = handler.get_analysis()
        return {"symbol": getHanldeAnalysis.symbol, "summary": getHanldeAnalysis.summary, "oscillators": getHanldeAnalysis.oscillators, "indicators": getHanldeAnalysis.indicators,"moving_averages": getHanldeAnalysis.moving_averages}

    def getFourHourData(symbol: str, exchange: str, screener: str):
        handler = TA_Handler(
        symbol,
        exchange,
        screener,
        interval="4h",
        timeout=None
        
    )
        getHanldeAnalysis = handler.get_analysis()
        return {"symbol": getHanldeAnalysis.symbol, "summary": getHanldeAnalysis.summary, "oscillators": getHanldeAnalysis.oscillators, "indicators": getHanldeAnalysis.indicators, "moving_averages": getHanldeAnalysis.moving_averages}



def runScript():
    # sleep for a day (24 hours)
    while True:
        printUtils.printSuccess(f"Running Script! {datetime.datetime.now()}")

        try: 
            jsonChoices = open("choices.json", "r+").read()
        except FileNotFoundError: printUtils.printError("FileNotFoundError - The choices file was not found. Please look at the docs to learn more.")
        except: printUtils.printError("Error getting file.")

        loadedJSONData = json.loads(jsonChoices)
        
        for x in loadedJSONData:
            Screener = loadedJSONData[x]["Screener"]
            Exchange = loadedJSONData[x]["Exchange"]
            Symbol = loadedJSONData[x]["Symbol"]
            
            try:
                getDailyData = UtilFuncs.getDailyData(Screener, Exchange, Symbol)
            except: printUtils.printError("Error getting daily data.")
            try:
                getFourHourData = UtilFuncs.getFourHourData(Screener, Exchange, Symbol)
            except: printUtils.printError("Error getting 4 hour data.")
            
        # define all data to send

        # 1 Day
        
        DaySymbol = getDailyData["symbol"]
        Daysummary = getDailyData["summary"]
        Dayoscillators = getDailyData["oscillators"]
        DaymovingAvrage = getDailyData["moving_averages"]
        
        # 4 hour
        fourHourSymbol = getFourHourData["symbol"]
        fourHoursummary = getFourHourData["summary"]
        fourHouroscillators = getFourHourData["oscillators"]
        fourHourmovingAvrage = getFourHourData["moving_averages"]

        formattedTextMessage = f"""
        
        * 1 Day data
        Symbol => {DaySymbol}
        
        \/ summary \/ 
        Reccomend => {Daysummary["RECOMMENDATION"]}
        
        \/ oscillators \/ 
        Reccomend => {Dayoscillators["RECOMMENDATION"]}
        RSI => {Dayoscillators["COMPUTE"]["RSI"]}
        STOCH.K => {Dayoscillators["COMPUTE"]["STOCH.K"]}
        CCI => {Dayoscillators["COMPUTE"]["CCI"]}
        MACD => {Dayoscillators["COMPUTE"]["MACD"]}
        
        \/ moving Avrage \/ 
        Reccomend => {DaymovingAvrage["RECOMMENDATION"]}
        EMA10 => {DaymovingAvrage["COMPUTE"]["EMA10"]}
        EMA20 => {DaymovingAvrage["COMPUTE"]["EMA20"]}
        EMA30 => {DaymovingAvrage["COMPUTE"]["EMA30"]}
        HullMA => {DaymovingAvrage["COMPUTE"]["HullMA"]}
        
        +===================+
        
        * 4 Hour Data
        Symbol => {fourHourSymbol}
        
        \/ summary \/ 
        Reccomend => {fourHoursummary["RECOMMENDATION"]}
        
        \/ oscillators \/  
        Reccomend => {fourHouroscillators["RECOMMENDATION"]}
        RSI => {fourHouroscillators["COMPUTE"]["RSI"]}
        STOCH.K => {fourHouroscillators["COMPUTE"]["STOCH.K"]}
        CCI => {fourHouroscillators["COMPUTE"]["CCI"]}
        MACD => {fourHouroscillators["COMPUTE"]["MACD"]}
        
        \/ moving Avrage \/ 
        Reccomend => {fourHourmovingAvrage["RECOMMENDATION"]}
        EMA10 => {fourHourmovingAvrage["COMPUTE"]["EMA10"]}
        EMA20 => {fourHourmovingAvrage["COMPUTE"]["EMA20"]}
        EMA30 => {fourHourmovingAvrage["COMPUTE"]["EMA30"]}
        HullMA => {fourHourmovingAvrage["COMPUTE"]["HullMA"]}
        
        """
        sendText(creds.phonefrom, creds.phoneNumber, formattedTextMessage)
        time.sleep(86000)


def sendText(phoneFrom: str, phoneTo: str, message: str):
    client = Client(creds.account_sid, creds.auth_token)
    try:
        messageRes = client.messages.create(
            to=phoneTo, 
            from_=phoneFrom,
            body=message)
        printUtils.printSuccess(messageRes.Status.DELIVERED)
    except: printUtils.printError("Error sending message.")


__init__()