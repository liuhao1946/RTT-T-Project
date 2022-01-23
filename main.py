# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import PySimpleGUI as sg
import time
from datetime import datetime
import threading
import pylink
import re
import json
import logging
#import traceback


base64_main_icon = b'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'

THREAD_RUN_INTERVAL_S = 0.002

RTT_DATA_WIN = '-DB_OUT-'+sg.WRITE_ONLY_KEY

class JlinkThread(threading.Thread):

    gui_wakeup_tick_th = 0

    def __init__(self, window,jlink,timestamp = False,thread_start=False):
        super().__init__(daemon=True)
        self._thread_start = thread_start
        self.jlink = jlink
        self.window = window
        self.timestamp = timestamp
        self.event = threading.Event()
        self.event.clear()

    def run(self):
        rtt_data_list = []
        rtt_data_list_temp = []
        gui_wake_tick = 0
        rtt_data_none_cnt = 0
        time_to = False

        while True:
            if self._thread_start:
                try:
                    rtt_data_list_temp = self.jlink.rtt_read(0,2048) #1ms = 1k
                    if len(rtt_data_list_temp):
                        rtt_data_list = rtt_data_list + rtt_data_list_temp
                        rtt_data_none_cnt = 0
                    else:
                        rtt_data_none_cnt = rtt_data_none_cnt + 1

                    #Turn on the timeout function,self.gui_wakeup_tick_th != 0
                    if self.gui_wakeup_tick_th != 0:
                        if rtt_data_none_cnt >= self.gui_wakeup_tick_th:
                            rtt_data_none_cnt = 0
                            time_to = True
                    else:
                    #Turn off the timeout function, 10ms automatically submit data once to the GUI
                        gui_wake_tick = gui_wake_tick + 1
                        if gui_wake_tick >= 5:
                            gui_wake_tick = 0
                            time_to = True

                    if time_to:
                        time_to = False
                        if len(rtt_data_list):
                            str_data = ''.join([chr(i) for i in rtt_data_list])
                            if self.timestamp == True:
                                str_data = '[' + datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[0:-3] + '] ' + str_data
                            self.window.write_event_value('-JLINK_READ_DATA_THREAD-', str_data)
                            rtt_data_list = []

                    time.sleep(THREAD_RUN_INTERVAL_S)
                except Exception as e:
                    logging.debug('Thread:rtt error [' + str(e) + ']\n')
                    print(str(e))
                    self.window.write_event_value('-JLINK_READ_DATA_THREAD-', 'J-Link connect lost')
                    self._thread_start = False
                except :
                    logging.debug('Thread:rtt error\n')
                    self.window.write_event_value('-JLINK_READ_DATA_THREAD-', 'J-Link connect lost')
                    self._thread_start = False
            else:
                print(rtt_data_list)
                logging.debug('Thread:rtt data length [' + str(len(rtt_data_list)) + ']')
                logging.debug('Thread:rtt data [' + ''.join([chr(i) for i in rtt_data_list]) +']')
                logging.debug('Thread:GUI wakeup tick threshold {}'.format(self.gui_wakeup_tick_th))
                logging.debug('Thread:J-Link thread wait......')
                self.event.wait()
                self.event.clear()

    def jlink_thread_ctr(self, state):
        self._thread_start = state
        if state:
            self.event.set()
            logging.debug('Thread:J-Link thread enable')
        else:
            self.event.clear()
            logging.debug('Thread:J-Link thread disble')

    def jlink_timestamp_set(self, state):
        self.timestamp = state

def jlink_reset(jlink):
    try:
        jlink.rtt_stop()
    except:
        print("rtt stop error\n")
        pass
    if jlink.opened():
        jlink.close()

def main():
    logging.basicConfig(filename='rtt-t.log',filemode='w',encoding='utf-8', level=logging.DEBUG,\
                        format='%(asctime)s %(message)s',datefmt='%Y/%m/%d %I:%M:%S')
    logging.debug('----------------------------------------------------------------')
    logging.debug('----------------------------------------------------------------')
    logging.debug('---------------RTT-T Debug Log---------------')
    logging.debug('----------------------------------------------------------------')
    logging.debug('----------------------------------------------------------------')

    with open('config.json', 'r') as f:
        json_data = json.load(f)

    chip_list = json_data['chip model']
    jk_interface_list = json_data['jlink interface']
    jk_speed = json_data['Speed']
    rx_timeout = json_data['Rx Timeout']
    sn = json_data['SN']
    font_type = json_data['font'][0]
    font_size = json_data['font size']
    try:
        data_window_w = int(json_data['data window width'])
    except:
        data_window_w = 83

    font = font_type + ' '

    jlink = pylink.JLink()
    right_click_menu = ['',['Clear','Scroll to the end']]

    cfg_frame_layout = [[sg.Button('Connect J-Link',pad=((45,3),(16,16)),key='-JK_CONNECT-',size=(18,2),button_color=('grey0','grey100'),font=(font+str(12)))],\
                    [sg.Button('Open Timestamp',key='-TIMESTAMP_CTR-',pad=((45,3),(16,16)),button_color=('grey0','grey100'),size=(18,2),font=(font+str(12)))],\
                    [sg.Button('Open Real-time saving data',key='-RT_DATA_SAVE-',pad=((45,3),(16,16)),size=(18,2),button_color=('grey0','grey100'),font=(font+str(12)))],\
                    [sg.Button('Save all data',key='-DATA_SAVE-',pad=((45,3),(16,16)),size=(18,2),button_color=('grey0','grey100'),font=(font+str(12)))],\
                    [sg.Text('Chip Model'),sg.Combo(chip_list,chip_list[0],size=(16,1),pad=((23,3),(20,16)),key='-CHIP_SEL-')],\
                    [sg.Text('J-Link Interface'),sg.Combo(jk_interface_list,jk_interface_list[0],size=(16,1),key='-JK_INTER-',pad=((0,3),(20,16)))],\
                    [sg.Text('RX Timout',pad=(10,20)),sg.InputText(rx_timeout,key='-RX_TIMEOUT-',size=(18,1),pad=((26,3),(20,16)),tooltip='0 means no timeout,Unit ms')],\
                    [sg.Text('J-Link S/N'),sg.InputText(sn,key='-SN-',pad=((24,3),(20,16)),size=(18,1))],\
                    [sg.Text('Speed(KHz)'), sg.InputText(jk_speed,pad=((14,3),(20,16)),key='-SPEED-',size=(18,1))],\
                  ]

    sd_bt_frame_layout = [[sg.Button('Send',key='-SD_DATA_BT-',pad=((45,28),(6,6)),size=(18,2),button_color=('grey0','grey100'),font=(font+str(12)))]]
    sd_data_frame_layout = [[sg.InputText('cmd:time syn',key='-SD_DATA_TXT-',size=(50,1),pad=((9,8),(10,15)),font=(font+str(20)),tooltip='Text type')]]

    layout = [[sg.Frame('Config', cfg_frame_layout, vertical_alignment='top',key='-CFG-'),\
               sg.Multiline(autoscroll=True,key=RTT_DATA_WIN,size=(data_window_w,31),pad=(10,10),right_click_menu=right_click_menu,font=(font+font_size+' bold'),expand_x=True,expand_y=True)],
              [sg.Frame('Send data',sd_bt_frame_layout,vertical_alignment='top'), \
               sg.Frame('Text Data',sd_data_frame_layout,vertical_alignment='top')],
             ]

    window = sg.Window('RTT Tool 1.5', layout,finalize=True,element_padding=(10,1),return_keyboard_events=False,icon=base64_main_icon,resizable=True)
    window.set_min_size(window.size)

    #window['-CFG-'].expand(True, True, True)
    window[RTT_DATA_WIN].expand(True, True, True)

    jlink_thread = JlinkThread(window,jlink)
    jlink_thread.start()

    mul_scroll_end = False
    real_time_save_file_name = False
    real_time_save_data = ''

    while True:
        event, values = window.read(timeout=200)

        if event == sg.WIN_CLOSED:
            jlink_thread.jlink_thread_ctr(False)
            jlink_reset(jlink)
            break

        #print(event, values)
        #Scroll bar in the middle position, as the data in the text box increases, y1 increases and y2 decreases
        y1, y2 = window[RTT_DATA_WIN].get_vscroll_position()
        if mul_scroll_end == True and bool(1 - y2):
            mul_scroll_end = False
            window[RTT_DATA_WIN].update(autoscroll=False)
        elif mul_scroll_end == False and y2 == 1:
            mul_scroll_end = True
            window[RTT_DATA_WIN].update(autoscroll=True)

        if event == '-JK_CONNECT-':
            if window['-JK_CONNECT-'].get_text() == 'Connect J-Link':
                jlink_op_suc = 0
                try:
                    jlink.open()
                    ser_num = jlink.serial_number
                    jlink.close()
                except pylink.errors.JLinkException as e:
                    sg.popup(e)
                    jlink_op_suc = 1

                #J-Link reads S/N successfully
                if jlink_op_suc == 0:
                    window['-SN-'].update(str(ser_num))
                    window[RTT_DATA_WIN].write('LOG:J-Link SN:'+str(ser_num)+'\n')
                    try:
                        jlink.open(str(ser_num))
                        #Set J-Link interface
                        jk_interface = window['-JK_INTER-'].get()
                        if  jk_interface == 'SWD':
                            jlink.set_tif(pylink.enums.JLinkInterfaces.SWD)

                        window[RTT_DATA_WIN].write('LOG:J-Link interface:' + jk_interface + '\n')
                        jlink.set_speed(int(window['-SPEED-'].get()))
                        window[RTT_DATA_WIN].write('LOG:J-Link speed:' + window['-SPEED-'].get() + 'KHz''\n')
                        #Connect J-Link
                        jlink.connect(window['-CHIP_SEL-'].get())
                        #Set Reset I/O
                        #jlink.set_reset_strategy(pylink.enums.JLinkResetStrategyCortexM3.RESETPIN)
                        jlink.reset(ms=10, halt=False)
                        #J-Link is connected
                        if jlink.connected():
                            window['-DB_OUT-' + sg.WRITE_ONLY_KEY].write('LOG:J-Link connect success!\n')
                            window['-JK_CONNECT-'].update(button_color=('grey0','green4'))
                            window['-JK_CONNECT-'].update('Disconnect J-Link')

                            #Check timeout time
                            try:
                                time_ms = int(window['-RX_TIMEOUT-'].get())
                            except:
                                sg.popup('Receive timeout time is set incorrectly')
                                time_ms = 0
                                window['-RX_TIMEOUT-'].update('0')

                            jlink_thread.gui_wakeup_tick_th = int(time_ms / (THREAD_RUN_INTERVAL_S * 10 ** 3))
                            #print('time_ms:', time_ms,jlink_thread.gui_wakeup_tick_th)
                            window[RTT_DATA_WIN].write('LOG:RTT rx data timout:' + window['-RX_TIMEOUT-'].get() + '\n')

                            if not jlink_thread.is_alive():
                                jlink_thread.start()
                            jlink_thread.jlink_thread_ctr(True)

                            jlink.rtt_start()
                            window['-RX_TIMEOUT-'].update(disabled=True)
                            window['-SN-'].update(disabled=True)
                            window['-SPEED-'].update(disabled=True)
                    except ValueError:
                        logging.debug('Speed setting error')
                        sg.popup('Speed setting error')
                        jlink_reset(jlink)
                    except Exception as e:
                        logging.debug('J-Link Operation error[' + str(e) + ']')
                        sg.popup('J-Link Operation error[' + str(e) + ']')
                        jlink_reset(jlink)
            else:
                    #Thread stop
                    jlink_thread.jlink_thread_ctr(False)
                    jlink_reset(jlink)
                    window[RTT_DATA_WIN].write('LOG:J-Link disconnect!\n')
                    window['-JK_CONNECT-'].update(button_color=('grey0', 'grey100'))
                    window['-JK_CONNECT-'].update('Connect J-Link')
                    window['-RX_TIMEOUT-'].update(disabled=False)
                    window['-SN-'].update(disabled=False)
                    window['-SPEED-'].update(disabled=False)

        elif event == 'Clear':
            window['-DB_OUT-' + sg.WRITE_ONLY_KEY].update('')

        elif event == '-TIMESTAMP_CTR-':
            if window['-TIMESTAMP_CTR-'].get_text() == 'Open Timestamp':
                window['-TIMESTAMP_CTR-'].update(button_color=('grey0', 'green4'))
                window['-TIMESTAMP_CTR-'].update('Close Timestamp')
                jlink_thread.jlink_timestamp_set(True)
            else:
                window['-TIMESTAMP_CTR-'].update(button_color=('grey0', 'grey100'))
                window['-TIMESTAMP_CTR-'].update('Open Timestamp')
                jlink_thread.jlink_timestamp_set(False)

        elif event == 'Scroll to the end':
            mul_scroll_end = True
            window['-DB_OUT-' + sg.WRITE_ONLY_KEY].update(autoscroll=True)

        elif event == '-DATA_SAVE-':
            file_name =  r'log_' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.txt'
            rtt_data_str = re.sub('(\r\n)+','\n',window[RTT_DATA_WIN].get())
           #file_name = os.path.dirname(os.path.realpath(sys.argv[0])) + '\\log\\' + file_name
           #print(file_name)
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(rtt_data_str)
            sg.popup_no_wait('File saved successfully')

        elif event == '-RT_DATA_SAVE-':
            if window['-RT_DATA_SAVE-'].get_text() == 'Open Real-time saving data':
                window['-RT_DATA_SAVE-'].update(button_color=('grey0','green4'))
                window['-RT_DATA_SAVE-'].update('Close Real-time saving data')
                real_time_save_file_name = r'real_time_log_' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.txt'
            else:
                window['-RT_DATA_SAVE-'].update(button_color=('grey0', 'grey100'))
                window['-RT_DATA_SAVE-'].update('Open Real-time saving data')

        elif event == '__TIMEOUT__':
            if len(real_time_save_data) > 0:
                try:
                    with open(real_time_save_file_name, 'a', encoding='utf-8') as f:
                        f.write(real_time_save_data)
                    real_time_save_data = ''
                except Exception as e:
                    logging.debug('Write real time data to file error[' + str(e) + ']\n')
                except:
                    logging.debug('Write real time data to file error')
                    sg.Print("Write real time data to file error")

        elif event == '-JLINK_READ_DATA_THREAD-':
            if values['-JLINK_READ_DATA_THREAD-'] != 'J-Link connect lost':
                window['-DB_OUT-' + sg.WRITE_ONLY_KEY].write(values['-JLINK_READ_DATA_THREAD-'])
                if window['-RT_DATA_SAVE-'].get_text() == 'Close Real-time saving data':
                    real_time_save_data =  real_time_save_data + re.sub('(\r\n)+','\n',values['-JLINK_READ_DATA_THREAD-'])
            else:
                logging.debug('J-Link connect lost')
                jlink_reset(jlink)
                jlink_thread.jlink_thread_ctr(False)
                window['-DB_OUT-' + sg.WRITE_ONLY_KEY].write('LOG:J-Link connection has been lost' + '\n')
                window['-JK_CONNECT-'].update(button_color=('grey0', 'grey100'))
                window['-JK_CONNECT-'].update('Connect J-Link')
                window['-RX_TIMEOUT-'].update(disabled=False)
                window['-SN-'].update(disabled=False)
                window['-SPEED-'].update(disabled=False)

        elif event == '-SD_DATA_BT-':
            data_cmd = window['-SD_DATA_TXT-'].get()
            if data_cmd.startswith('cmd:'):
                if data_cmd.find('time syn') >= 0:
                    if jlink.opened():
                        try:
                            time_str = 'time syn:' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                            time_list = [ord(i) for i in time_str]
                            jlink.rtt_write(0,time_list)
                            logging.debug('Data send success(cmd:time syn):'+ time_str)
                        except Exception as e:
                            logging.debug('Data send failt(cmd:time syn)[' + str(e) + ']\n')
                        except:
                            logging.debug('Data send failt(cmd:time syn)')
            else:
                if jlink.opened():
                    try:
                        time_list = [ord(i) for i in data_cmd]
                        jlink.rtt_write(0, time_list)
                        logging.debug('Data send success:' + data_cmd)
                    except Exception as e:
                        logging.debug('Data send error[' + str(e) + ']\n')
                    except:
                        logging.debug('Data send error')
                pass

    window.close()

if __name__ == '__main__':
    main()
