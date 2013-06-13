##-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
##    Py-Arduino-Proxy - Access your Arduino from Python
##    Copyright (C) 2011 - Horacio Guillermo de Oro <hgdeoro@gmail.com>
##
##    This file is part of Py-Arduino-Proxy.
##
##    Py-Arduino-Proxy is free software; you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation version 2.
##
##    Py-Arduino-Proxy is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License version 2 for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with Py-Arduino-Proxy; see the file LICENSE.txt.
##-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import cherrypy
import jinja2
import logging
import os
import sys
import subprocess
import time

from cherrypy.process.plugins import BackgroundTask
from cherrypy.process.wspbus import Bus

from arduino_proxy import ArduinoProxy

logger = logging.getLogger(__name__)


class Root(object):
    
    def __init__(self, jinja2_env, proxy=None, on_error_handler=None):
        self.proxy = proxy
        self.jinja2_env = jinja2_env
        self.on_error_handler = on_error_handler

    @cherrypy.expose
    def connect_emulator(self):
        logger.info("Creating EMULATOR...")
        self.proxy = ArduinoProxy.create_emulator()
        raise cherrypy.HTTPRedirect("/") # Connect OK -> redirect to '/'

    @cherrypy.expose
    def connect(self, serial_port=None, speed=None):
        # Render the connect page
        if serial_port is None:
            error_message = cherrypy.session.get('error_message')  #@UndefinedVariable
            cherrypy.session['error_message'] = None  #@UndefinedVariable
            template = self.jinja2_env.get_template('web-ui-select-serial-port.html')
            return template.render(error_message=error_message)
        
        # Try to conect
        error_message = None # holds the error messages, and used as a flag too.
        serial_port = serial_port.strip()
        if serial_port: # != None
            try:
                logger.info("Trying to connect to %s", serial_port)
                proxy = ArduinoProxy(tty=serial_port, speed=int(speed))
                logger.info("Connected OK")
                self.proxy = proxy
                raise cherrypy.HTTPRedirect("/") # Connect OK -> redirect to '/'
            except cherrypy.HTTPRedirect, cherrypy_redirect:
                raise cherrypy_redirect
            except ArduinoProxy, ap_exception:
                error_message = str(ap_exception)
                logger.exception("Couldn't create instance of ArduinoProxy")
            except Exception, exception:
                error_message = str(exception)
                logger.exception("Couldn't create instance of ArduinoProxy")
        else:
            error_message = "Must specify a serial port."
        
        assert error_message
        template = self.jinja2_env.get_template('web-ui-select-serial-port.html')
        return template.render(error_message=error_message)
    
    @cherrypy.expose
    def index(self):
        return self.generate_ui()

    @cherrypy.expose
    def js_prototyper(self):
        return self.generate_ui(template_name="web-ui-js-prototyper.html")

    def generate_ui(self, template_name="web-ui-main.html"):
        """
        Generates the UI pages (main, JS Prototyper, etc.).
        If no proxy is defined or validation fails, a redirect is generated.
        """
        if self.proxy is None:
            raise cherrypy.HTTPRedirect("/connect")

        try:
            self.proxy.validateConnection()
        except Exception, e:
            if self.on_error_handler:
                self.on_error_handler()
            else:
                self.proxy = None
                cherrypy.session['error_message'] = str(e)  #@UndefinedVariable
                raise cherrypy.HTTPRedirect("/connect")

        arduino_type = self.proxy.getArduinoTypeStruct()
        avr_cpu_type = self.proxy.getAvrCpuType()
        template = self.jinja2_env.get_template(template_name)

        return template.render(arduino_type=arduino_type, avr_cpu_type=avr_cpu_type)

    ## ~~~~~~ Here start AJAX methods

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def ping(self):
        try:
            self.proxy.ping()
            return {'ok': True, }
        except Exception, e:
            # FIXME: return error details and log
            logging.exception("Exception raised by proxy.ping()")
            return {'ok': False, 'exception': str(e), }

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def validate_connection(self):
        try:
            random_value = self.proxy.validateConnection()
            return {'ok': True, 'random_value': random_value, }
        except Exception, e:
            # FIXME: return error details and log
            logging.exception("Exception raised by proxy.validateConnection()")
            return {'ok': False, 'exception': str(e), }

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def pin_mode(self, pin=None, mode=None):
        try:
            if mode == 'output':
                self.proxy.pinMode(int(pin), ArduinoProxy.OUTPUT)
                return {'ok': True, }
            elif mode == 'input':
                self.proxy.pinMode(int(pin), ArduinoProxy.INPUT)
                return {'ok': True, }
            else:
                # FIXME: return error details and log
                return {'ok': False, 'error': 'Invalid mode: ' + mode}
        except Exception, e:
            # FIXME: return error details and log
            logging.exception("Exception raised by proxy.pinMode()")
            return {'ok': False, 'exception': str(e), }

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def digital_write(self, pin=None, value=None):
        try:
            if value == 'low':
                self.proxy.digitalWrite(int(pin), ArduinoProxy.LOW)
                return {'ok': True, }
            elif value == 'high':
                self.proxy.digitalWrite(int(pin), ArduinoProxy.HIGH)
                return {'ok': True, }
            else:
                # FIXME: return error details and log
                return {'ok': False, 'error': 'ArduinoProxy returned an invalid value: ' + value}
        except Exception, e:
            # FIXME: return error details and log
            logging.exception("Exception raised by proxy.digitalWrite()")
            return {'ok': False, 'exception': str(e), }

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def analog_write(self, pin=None, value=None):
        try:
            self.proxy.analogWrite(int(pin), int(value))
            return {'ok': True, }
        except Exception, e:
            # FIXME: return error details and log
            logging.exception("Exception raised by proxy.analogWrite()")
            return {'ok': False, 'exception': str(e), }
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def analog_read(self, pin=None):
        try:
            value = self.proxy.analogRead(int(pin))
            return {'ok': True, 'value': value, }
        except Exception, e:
            # FIXME: return error details and log
            logging.exception("Exception raised by proxy.analogRead()")
            return {'ok': False, 'exception': str(e), }
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def digital_read(self, pin=None):
        try:
            value = self.proxy.digitalRead(int(pin))
            if value == ArduinoProxy.HIGH:
                return {'ok': True, 'value': 1, }
            elif value == ArduinoProxy.LOW:
                return {'ok': True, 'value': 0, }
            else:
                # FIXME: return error details and log
                return {'ok': False, 'error': 'ArduinoProxy returned an invalid value: ' + value}
        except Exception, e:
            # FIXME: return error details and log
            logging.exception("Exception raised by proxy.analogWrite()")
            return {'ok': False, 'exception': str(e), }

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def delay(self, value=None):
        try:
            self.proxy.delay(int(value))
            return {'ok': True, }
        except Exception, e:
            # FIXME: return error details and log
            logging.exception("Exception raised by proxy.delay()")
            return {'ok': False, 'exception': str(e), }

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_free_memory(self):
        try:
            return {
                'ok': True,
                'freeMemory': self.proxy.getFreeMemory(),
            }
        except Exception, e:
            # FIXME: return error details and log
            logging.exception("Exception raised by proxy.getAvrCpuType()")
            return {'ok': False, 'exception': str(e), }

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_avr_cpu_type(self):
        try:
            return {
                'ok': True,
                'avrCpuType': self.proxy.getAvrCpuType(),
            }
        except Exception, e:
            # FIXME: return error details and log
            logging.exception("Exception raised by proxy.getAvrCpuType()")
            return {'ok': False, 'exception': str(e), }

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_arduino_type_struct(self):
        try:
            return {
                'ok': True,
                'arduinoTypeStruct': self.proxy.getArduinoTypeStruct(),
            }
        except Exception, e:
            # FIXME: return error details and log
            logging.exception("Exception raised by proxy.getArduinoTypeStruct()")
            return {'ok': False, 'exception': str(e), }

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def close(self):
        try:
            self.proxy.close()
            self.proxy = None
            return {'ok': True, }
        except Exception, e:
            # FIXME: return error details and log
            logging.exception("Exception raised by proxy.close()")
            return {'ok': False, 'exception': str(e), }


def background_check_ping(proxy):
    """
    Tarea en BACKGROUND.
    
    Sirve para que, si el ping no responde, cerremos el servidor, y así
    el script de inicio lo volverá a iniciar, y de esta manera nos aseguramos
    de reinicair todo el sistema (servidor y Arduino)
    """
    logging.info("Iniciando background_check_ping()")
    try:
        # res = 0
        res = proxy.ping()
        logging.info("proxy.ping(): %s", res)
    except:
        logging.exception("ERROR in background_check_ping()... "
            "Haremos 'os._exit(1)' para forzar el reinicio del servidor y de Arduino")
        os._exit(1)


def check_pin0_digital(proxy):
    """
    Tarea en BACKGROUND
    """
    PIN_ALARMA_PATIO = 11
    logging.info("Iniciando check_pin0_digital() - PIN_ALARMA_PATIO: %s",
        PIN_ALARMA_PATIO)
    try:
        proxy.pinMode(PIN_ALARMA_PATIO, ArduinoProxy.INPUT)
        proxy.digitalWrite(PIN_ALARMA_PATIO, ArduinoProxy.HIGH)

        ultimo_valor = ArduinoProxy.HIGH
        while True:
            value = proxy.digitalRead(PIN_ALARMA_PATIO)
            if value != ultimo_valor:
                print "ALARMA  1 (Conectada) / 0 (Desconectada). Nuevo valor:", value
                logging.info("ALARMA  1 (Conectada) / 0 (Desconectada). Nuevo valor: %s", value)
                ultimo_valor = value
        if value == ArduinoProxy.HIGH:
            subprocess.call('/home/scripts/alarma/alarma_desactivada.txt', shell=True)
        else:
            subprocess.call('/home/scripts/alarma/alarma_activada.txt', shell=True)
            time.sleep(0.1)
    except:
        logging.exception("ERROR in check_pin0_digital()... "
            "Haremos 'os._exit(1)' para forzar el reinicio del servidor y de Arduino")
        os._exit(1)


def background_check_ds18x20_temperatura_pileta(proxy):
    """
    Tarea en BACKGROUND
    """
    PIN_TEMPERATURA = 9
    ARCHIVO = '/tmp/temperatura-pileta.txt'
    logging.info("Iniciando background_check_ds18x20_temperatura_pileta() - PIN_TEMPERATURA: %s - ARCHIVO: %s",
        PIN_TEMPERATURA, ARCHIVO)
    try:
        # proxy.pinMode(PIN_TEMPERATURA, ArduinoProxy.INPUT)
        value = proxy.ds18x20_read(PIN_TEMPERATURA)
        with open(ARCHIVO, 'a') as f:
            f.write(value)
            f.write("\n")
    except:
        logging.exception("ERROR en ds18x20_read()... En vez de salir, solo esperaremos un momento"
            " y reiniciaremos...")
        time.sleep(10)
        # os._exit(1)


def check_pin_digital(proxy):
    """
    Tarea en BACKGROUND
    """
    PIN_ALARMA_PATIO = 12
    logging.info("Iniciando check_pin_digital() - PIN_ALARMA_PATIO: %s",
        PIN_ALARMA_PATIO)
    try:
        proxy.pinMode(PIN_ALARMA_PATIO, ArduinoProxy.INPUT)
        proxy.digitalWrite(PIN_ALARMA_PATIO, ArduinoProxy.HIGH)

        ultimo_valor = ArduinoProxy.HIGH
        while True:
            value = proxy.digitalRead(PIN_ALARMA_PATIO)
            if value != ultimo_valor:
                print "ALARMA PATIO. Nuevo valor:", value
                ultimo_valor = value
        if value == ArduinoProxy.HIGH:
            subprocess.call('/home/scripts/alarma/alarma.txt', shell=True)
        else:
            subprocess.call('/home/scripts/alarma/fin_alarma.txt', shell=True)
            time.sleep(0.1)
    except:
        logging.exception("ERROR in check_pin_digital()... "
            "Haremos 'os._exit(1)' para forzar el reinicio del servidor y de Arduino")
        os._exit(1)

 
def start_webserver(port, proxy=None, on_error_handler=None):
    directory = os.path.split(__file__)[0]
    static_dir = os.path.join(directory, 'static')
    logger.info("Using '%s' as directory for templates, images, css, etc.", static_dir)
    conf = {
        '/': {
            'tools.sessions.on': True,
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': static_dir,
        }
    }
    
    jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(static_dir))
    
    cherrypy.config.update({
        'log.screen': False,
        'server.socket_port': port,
    })

    bgtask = BackgroundTask(5, background_check_ping, args=[proxy])
    bgtask.start()

    bgtask = BackgroundTask(5, check_pin_digital, args=[proxy])
    bgtask.start()
    
    bgtask = BackgroundTask(5, check_pin0_digital, args=[proxy])
    bgtask.start()

    bgtask = BackgroundTask(10, background_check_ds18x20_temperatura_pileta, args=[proxy])
    bgtask.start()

    cherrypy.quickstart(Root(jinja2_env, proxy=proxy, on_error_handler=on_error_handler), '/', config=conf)

    # cherrypy.log.error_log.setLevel(logging.ERROR)
    # cherrypy.log.access_log.setLevel(logging.ERROR)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # CherryPy examples
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #
    #    # Set up site-wide config first so we get a log if errors occur.
    #    cherrypy.config.update({'environment': 'production',
    #                            'log.error_file': 'site.log',
    #                            'log.screen': True})
    #
    #    conf = {'/feed': {'tools.staticdir.on': True,
    #                      'tools.staticdir.dir': os.path.join(current_dir, 'feeds'),
    #                      'tools.staticdir.content_types': {'rss': 'application/xml',
    #                                                        'atom': 'application/atom+xml'}}}
    #    cherrypy.quickstart(Root(), '/', config=conf)
    #
    #    cherrypy.config.update({
    #        'server.socket_host': '64.72.221.48',
    #        'server.socket_port': 80,
    #    })
    #
    #    config = {'/':
    #        {
    #            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
    #            'tools.trailing_slash.on': False,
    #        }
    #    }
    #    cherrypy.tree.mount(Root(), "/script_name_root", config=config)
