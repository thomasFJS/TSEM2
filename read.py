from smartcard.CardRequest import CardRequest
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.CardType import AnyCardType
from smartcard import util
from accesslinkTools import PolarAccessLink
import time
import json
import mysql.connector
# INSERT 
#sql = "INSERT INTO CLIENTS (name, cardID) VALUES (%s, %s)"
#val = ("Thomas", "[139, 28, 63, 172]")
#mydb.commit()
#print(mycursor.rowcount, "record inserted")

#Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mermailmegalo1",
    database="db_rfid"

)

mycursor = mydb.cursor()


if __name__ == '__main__':
    # respond to the insertion of any type of smart card
    card_type = AnyCardType()

    # create the request. Wait for up to x seconds for a card to be attached
    request = CardRequest(timeout=None, cardType=card_type)

    #clients = json.load(c)
    while True:
            time.sleep(0.1)
            # listen for the card
            service = None
            try:
                service = request.waitforcard()
            except CardRequestTimeoutException:
                print("ERROR: No card detected")
                exit(-1)

            # when a card is attached, open a connection
            conn = service.connection
            conn.connect()

            # get and print the ATR and UID of the card
            get_uid = util.toBytes("FF CA 00 00 00")
            print("ATR = {}".format(util.toHexString(conn.getATR())))
            data, sw1, sw2 = conn.transmit(get_uid)
            uid = util.toHexString(data)
            status = util.toHexString([sw1, sw2])
            print("UID = {}\tstatus = {}".format(uid, status))
            #print(uid)
            #print(data)
            sql = "SELECT cardID FROM CLIENTS WHERE cardID = %s"
            adr = (uid,)
            mycursor.execute(sql,adr)
            result = mycursor.fetchall()
            

            if mycursor.rowcount==1 :
                print("Success")
                PolarAccessLink()
            else:
                print("Refused")

            time.sleep(2)
       