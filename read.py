#!/usr/bin/python3

import RPi.GPIO as GPIO

import manager.rules_manager as rules_manager
import manager.game_manager as game_manager
import lib.helper as helper
import lib.MFRC522 as MFRC522
import lib.constants as constants

# create the reader object
MIFAREReader = MFRC522.MFRC522()

def read_card():
    """Read RFID card

    Returns:
        Card: card infos
    """
    with open('./json/clients.json') as c:
        cards = json.load(c)
        while True:
            time.sleep(0.1)
            (status, TagType) = MIFAREReader.MFRC522_Request(
                MIFAREReader.PICC_REQIDL)
            (status, uid) = MIFAREReader.MFRC522_Anticoll()
            if status == MIFAREReader.MI_OK:
                card_id = int(str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])) #get the card id of the scanned card
                for card in cards:
                    if card["card_id"] == card_id:
                        print(
                            "Card found")
                        time.sleep(2)
                        return card