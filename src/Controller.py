# noqa: E402
# -*- coding: utf-8 -*-
import logging
from abc import ABC, abstractmethod


class AbstractController(ABC):
    def __init__(self, domain, tcp_enabled, reader_thread, port,
                 terminated):
        self.domain = domain
        self.tcp_enabled = tcp_enabled
        self.reader_function = reader_thread
        self.port = port
        self.terminated = terminated
        self.logger = logging.getLogger('ControllerLogger')

    @abstractmethod
    def initialize(self):
        if self.tcp_enabled is True:
            self.logger.info('Start Thread reader')
            self.threading.start()

    @abstractmethod
    def cleanup(self):
        if self.tcp_enabled:
            self.logger.info('Terminate')

    @abstractmethod
    def toString(self):
        pass


class MonitoringController:

    def __init__(self, writer_controller, time_source_controller):
        self.writer_controller = writer_controller
        self.time_source_controller = time_source_controller

    def new_monitoring_record(self, record):
        return self.writer_controller.new_monitoring_record(record)


class TimeSourceController(AbstractController):

    def __init__(self, time_source):
        # super().__init__()
        self.time_source = time_source

    def initialize(self):
        pass

    def cleanup(self):
        self.debug("shuttig down")

    def toString(self):
        pass



from src.Writer import FileWriter


class WriterController:

    def __init__(self, path):
        self.monitoring_writer = FileWriter(path, [])

    def initialize(self):
        pass

    def cleanup(self):
        return 'foo'

    def new_monitoring_record(self, record):
        self.monitoring_writer.writeMonitoringRecord(record)
