# -*- coding: utf-8 -*-
from sys import exc_info, stdout
import logging
import os
from enum import IntEnum
import requests
import re


class AttackErrorBase(Exception):
    pass


class GenericError(AttackErrorBase):
    pass


class InvalidIdentityError(AttackErrorBase):
    pass


class ContestNotStartedError(AttackErrorBase):
    pass


class ContestPausedError(AttackErrorBase):
    pass


class ContestCompletedError(AttackErrorBase):
    pass


class InvalidFormatError(AttackErrorBase):
    pass


class Result(IntEnum):
    SUCCESS_FLAG_ACCEPTED = 0  # submitted flag has been accepted
    ERR_GENERIC = 1  # generic error
    ERR_INVALID_IDENTITY = 2  # the attacker does not appear to be a team
    ERR_CONTEST_NOT_STARTED = 3  # contest has not been started yet
    ERR_CONTEST_PAUSED = 4  # contest has been paused
    ERR_CONTEST_COMPLETED = 5  # contest has been completed
    ERR_INVALID_FORMAT = 6  # submitted data has invalid format
    ERR_ATTEMPTS_LIMIT = 7  # attack attempts limit exceeded
    ERR_FLAG_EXPIRED = 8  # submitted flag has expired
    ERR_FLAG_YOURS = 9  # submitted flag belongs to the attacking team
    ERR_FLAG_SUBMITTED = 10  # submitted flag has been accepted already
    ERR_FLAG_NOT_FOUND = 11  # submitted flag has not been found
    ERR_SERVICE_NOT_UP = 12  # the attacking team service is not up


class Carrier(object):
    def __init__(self, host, port=80, url='api/submit'):
        self._logger = self.get_logger()
        self._host = host
        self._port = port
        self._url = url

    def get_logger(self):
        console_handler = logging.StreamHandler(stdout)
        log_format = '[%(asctime)s] - %(levelname)s - %(message)s'
        formatter = logging.Formatter(log_format)
        console_handler.setFormatter(formatter)
        logger = logging.Logger(__name__)
        level_str = os.getenv('LOG_LEVEL', 'INFO')
        if level_str == 'CRITICAL':
            level = logging.CRITICAL
        elif level_str == 'ERROR':
            level = logging.ERROR
        elif level_str == 'WARNING':
            level = logging.WARNING
        elif level_str == 'INFO':
            level = logging.INFO
        elif level_str == 'DEBUG':
            level = logging.DEBUG
        elif level_str == 'NOTSET':
            level = logging.NOTSET
        else:
            level = logging.INFO
        logger.setLevel(level)
        logger.addHandler(console_handler)
        return logger

    @property
    def logger(self):
        return self._logger

    @property
    def submit_url(self):
        return 'http://{0}:{1}/{2}'.format(self._host, self._port, self._url)

    def attack(self, *flags):
        payload = []
        for flag in flags:
            if re.match('^[\da-f]{32}=$', flag) is None:
                raise InvalidFormatError()
            else:
                payload.append(flag)

        try:
            r = requests.post(self.submit_url, json=payload)
            if r.status_code == 200:
                return r.json()

            if r.status_code == 400:
                code = r.json()
                if code == Result.ERR_INVALID_IDENTITY:
                    raise InvalidIdentityError()
                elif code == Result.ERR_CONTEST_NOT_STARTED:
                    raise ContestNotStartedError()
                elif code == Result.ERR_CONTEST_PAUSED:
                    raise ContestPausedError()
                elif code == Result.ERR_CONTEST_COMPLETED:
                    raise ContestCompletedError()
                elif code == Result.ERR_INVALID_FORMAT:
                    raise InvalidFormatError()
                else:
                    raise GenericError()
            else:
                raise GenericError()
        except Exception:
            self.logger.error('An exception occured', exc_info=exc_info())
            raise
