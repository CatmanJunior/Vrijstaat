import datetime
import os
import logging

def initLog():
	logOrdinalDate = str(datetime.date.today().toordinal())
	if not os.path.isfile('logs/' + logOrdinalDate + '.log'):
		with open('logs/' + logOrdinalDate + '.log', 'w') as f:
	   		pass
	logging.basicConfig(filename='logs/' + logOrdinalDate + '.log', filemode='a', format='%(asctime)s %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logging.info('-------------------------------------------------------------------')
logging.info('Program started')
logging.info('-------------------------------------------------------------------')

initLog()

name = "Bert"
logging.error(f'{name} raised an error')
try:
  c = a / b
except Exception as e:
  logging.exception("Exception occurred")