'''
@Author: Senkita
'''

import PySimpleGUI as sg
import os

class Interface:
    # 完成
    def finish(self, name):
        layout = [
            [sg.T('文件名为：{}'.format(name))],
            [sg.OK('确定')]
        ]
        window = sg.Window('完成', layout)
        event = window.Read()
        if event[0] in (None, '确定'):
            window.Close()

    # 读取文件路径
    def file_selector(self):
        layout = [
            [sg.T('请选择英文文本路径：')],
            [
                sg.I(
                    size=(40, None),
                    disabled=True
                ),
                sg.FileBrowse(
                    button_text='打开',
                    file_types=((
                        '文本文档',
                        '*.txt'),)
                )
            ],
            [sg.T('请选择词性配置文件路径：')],
            [
                sg.I(
                    size=(40, None),
                    disabled=True,
                    default_text='part_of_speech.json'
                ),
                sg.FileBrowse(
                    button_text='打开',
                    file_types=((
                        '词性配置文件',
                        '*.json'),)
                )
            ],
            [sg.Submit('确定'), sg.Cancel('取消')]
        ]

        window = sg.Window('词频词性分析', layout)

        event, value = window.Read()

        if event == '确定':
            window.Close()
            if '' == value[0]:
                warning = sg.Popup('警告！', '存在漏填项！')
                if warning in (None, 'OK'):
                    return self.file_selector()
            elif os.path.exists(value[1]) != True:
                warning = sg.Popup('警告！', '词性配置文件不存在！')
                if warning in (None, 'OK'):
                    return self.file_selector()
            else:
                return value[0], value[1]
        elif event in (None, '取消'):
            window.Close()