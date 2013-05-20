#!/usr/bin/env python
# -*- coding: utf-8 -*-

import obfsproxy.common.log as logging
import obfsproxy.common.serialize as serialize

import struct
import mycrypto
import const

log = logging.get_obfslogger()


def createDataMessages( data ):

        messages = []

        log.debug("Creating protocol messages.")

        while len(data) >= const.MPU:
                messages.append(ProtocolMessage(data[:const.MPU]))
                data = data[const.MPU:]

        messages.append(ProtocolMessage(data))

        return messages


def saneHeader( totalLen, payloadLen, flags ):

        def ok( length ):
                return True if (0 <= length <= const.MPU) else False

        validFlags = [
                const.FLAG_PAYLOAD,
                const.FLAG_NEW_TICKET,
                const.FLAG_CONFIRM_TICKET,
                const.FLAG_PAYLOAD + const.FLAG_CONFIRM_TICKET
        ]

        return ok(totalLen) and ok(payloadLen) and (ord(flags) in validFlags)


class ProtocolMessage( object ):
        """Provides an abstraction of ScrambleSuit protocol messages. The class
        provides methods to build, encrypt and pad protocol messages."""

        def __init__( self, payload="", paddingLen=0, flags=const.FLAG_PAYLOAD ):

                payloadLen = len(payload)
                assert((payloadLen + paddingLen) <= (const.MPU))

                self.hmac = ""
                self.totalLen = payloadLen + paddingLen
                self.payloadLen = payloadLen
                self.payload = payload
                self.flags = chr(flags)


        def encryptAndHMAC( self, crypter, HMACKey ):

                encrypted = crypter.encrypt(serialize.htons(self.totalLen) + \
                                serialize.htons(self.payloadLen) + self.flags + \
                                self.payload + (self.totalLen - self.payloadLen) * '\0')

                hmac = mycrypto.HMAC_SHA256_128(HMACKey, encrypted)

                return hmac + encrypted


        def addPadding( self, paddingLen ):

                # The padding must not exceed the message size.
                assert ((self.totalLen + paddingLen) <= const.MPU)

                if paddingLen == 0:
                        return

                log.debug("Adding %d bytes of padding to %d-byte message." % \
                                (paddingLen, const.HDR_LENGTH + self.totalLen))
                self.totalLen += paddingLen


        def __len__( self ):
                return const.HDR_LENGTH + self.totalLen
