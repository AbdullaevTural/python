import interface as ui
import logger as lg
import editer as ed


lg.logging.info('Start')
ed.init_data_base('base_phone.csv')
ui.ls_menu()