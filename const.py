#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines constant values for the ScrambleSuit protocol.
The values below are not supposed to be changed. If you don't obey, be at least
careful because things could break easily.
"""

# Key size for the AES session key and its IV in bytes.
SESSION_KEY_SIZE = IV_SIZE = 32

# Key size for the master key in bytes.
MASTER_KEY_SIZE = 32

# The maximum padding length to be appended to the puzzle in bytes.
MAX_PADDING_LENGTH = 4096

# Length of the raw time-lock puzzle (consisting of `n' and `Ck') in bytes.
PUZZLE_LENGTH = 128

# The length of the puzzle's modulus `n' in bits.
PUZZLE_MODULUS_LENGTH = 512

# Approximate CPU time in seconds necessary to solve the puzzle.
PUZZLE_UNLOCK_TIME = 120

# Size of random key used to obfuscate a puzzle in bits.
PUZZLE_OBFUSCATION_KEYSPACE = 7

# Nonce size prepended to encrypted puzzle in bytes.
PUZZLE_NONCE_LENGTH = 8

# Length of the magic values in bytes.
MAGIC_LENGTH = 32

# States which are used for the protocol state machine.
ST_WAIT_FOR_AUTH = 0
ST_WAIT_FOR_PUZZLE = 1
ST_SOLVING_PUZZLE = 2
ST_WAIT_FOR_MAGIC = 3
ST_CONNECTED = 4
ST_WAIT_FOR_PK = 5

# FIXME - Directory where long-lived information is stored.
DATA_DIRECTORY = "/tmp/"

# Divisor (in seconds) for the UNIX epoch used to defend against replay
# attacks.
EPOCH_GRANULARITY = 3600

# Key rotation time for session ticket keys in seconds.
KEY_ROTATION_TIME = 60 * 60 * 24 * 7

# File where session ticket keys are stored.
KEY_STORE = "ticket_keys.bin"

# File which holds our session ticket.
# FIXME - multiple session tickets for multiple servers must be supported.
TICKET_FILE = "session_ticket.bin"

# Length of ScrambleSuit's header in bytes.
HDR_LENGTH = 16 + 2 + 2 + 1

# Length of the HMAC-SHA256-128 in bytes.
HMAC_LENGTH = 16

# Length of ScrambleSuit's MTU in bytes.
MTU = 1460

# Maximum payload unit of a ScrambleSuit message in bytes.
MPU = MTU - HDR_LENGTH

PUBLIC_KEY_LENGTH = 192

# The smallest 16-byte value (used to encrypt puzzles).
MIN_16BYTE_VALUE = (1 << (8 * 15))

FLAG_PAYLOAD = 1
FLAG_NEW_TICKET = 2
FLAG_CONFIRM_TICKET = 4

# Length of a session ticket in bytes.
TICKET_LENGTH = 112

# Life time of session tickets in seconds.
SESSION_TICKET_LIFETIME = 60 * 60 * 24 * 7

# The prefix prepended to the master key which is locked inside the time-lock
# puzzle. The client looks for this prefix to verify that the puzzle was
# unlocked successfully.
MASTER_KEY_PREFIX = "MasterKey="

# The protocol name which is used in log messages.
TRANSPORT_NAME = "ScrambleSuit"

# SHA256's digest size in bytes.
SHA256_DIGEST_SIZE = 32
