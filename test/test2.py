#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use say Method"""

import qi
import argparse
import sys


def main(session):
    """
    Say a text with a local configuration.
    """
    # Get the service ALAnimatedSpeech.
    asr = session.service("ALTextToSpeech")
    asr_service = session.service("ALAnimatedSpeech")

    # set the local configuration
    configuration = {"bodyLanguageMode":"contextual"}

    # say the text with the local configuration
    asr.setLanguage("Japanese")
    asr.setParameter("pitchShift",1.1)
    asr.setParameter("speed",90)
    asr_service.say("コチさんが^start(animations/Stand/Gestures/Give_5)見つけてくれたよね^wait(animations/Stand/Gestures/Give_5)",configuration)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.142.30",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
