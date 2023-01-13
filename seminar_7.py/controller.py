import model
import view
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

def main_function():
  try:
   select =view.greeting()
  except Exception:
    logging.warning("Введено не коректное значение")
  if select == 1:
     logging.info("Выбран режим конкулятор")
     primer = view.get_math_example()
     result = model.calc(primer)
     view.view_result(result)
     logging.info(f"Введен результат '{result}")
  elif select == 2:
    logging.info("Выбран режим конвертер")
    massa = view.get_massa()
    logging.info("Введено значение'{massa}'")
    value = model.converter(massa)
    view.view_result(value)
     
     
