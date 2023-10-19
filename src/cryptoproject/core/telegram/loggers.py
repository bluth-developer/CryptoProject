import asyncio
from logging import StreamHandler
from threading import Thread
import aiogram
from core.misc import loggers
from core.misc.exceptions import SendingProcessNotStartedError


class TelegramLogger:
    def __init__(self, bot_token):
        """
        :param bot_token: Telegram BOT TOKEN
        """
        self._bot = aiogram.Bot(token=bot_token)
        self._loop: asyncio.AbstractEventLoop = None
        self._start_process()

    @staticmethod
    def _run_loop(loop):
        """
        Runs loop forever in the process

        :param loop: - Loop to run
        :return:
        """
        asyncio.set_event_loop(loop)
        loop.run_forever()

    def _start_process(self):
        """
        Starts a new process with an eventloop inside
        Is needed to send logs in parallel
        :return:
        """
        loop = asyncio.new_event_loop()
        self._loop = loop
        process = Thread(target=self._run_loop, args=(loop,), daemon=True)
        process.start()

    async def _send(self, chat_id, log):
        """
        Sends log in chat via Telegram
        :param chat_id:
        :param log:
        :return:
        """
        try:
            await self._bot.send_message(chat_id=chat_id, text=log, parse_mode="HTML")
        except Exception as e:
            loggers.telegram.exception(f"Exception while sending {log} to {chat_id}:\n{e}")

    def send(self, chat_id, log):
        """
        Sends log in chat via Telegram

        :param chat_id:
        :param log:
        :return:
        """
        if not self._loop or not self._loop.is_running():
            raise SendingProcessNotStartedError()
        asyncio.run_coroutine_threadsafe(self._send(chat_id, log), self._loop)


class TelegramLoggerHandler(StreamHandler):
    """Logger handler that send logs to Telegram"""

    def __init__(self, telegram_logger: TelegramLogger, chat_ids: list[int]):
        """
        :param telegram_logger: Telegram Logger
        :param chat_ids: list of chat_id to log to
        """
        super().__init__()
        self._telegram_logger = telegram_logger
        self._chat_ids = chat_ids

    def emit(self, record):
        log = self.format(record)
        for chat_id in self._chat_ids:
            self._telegram_logger.send(chat_id, log)
