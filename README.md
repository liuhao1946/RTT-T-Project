# RTT（Real Time Transfer） Tool（RTT-T）
---

[RTT-T下载地址(windows平台)](https://github.com/liuhao1946/RTT-T-Project/releases)

### 描述
这是一个**J-Llink RTT**软件，用来接收由MCU通过SEGGER RTT发送的数据。相比官方J-Llink RTT Viewer软件，该软件有以下特点：
* 使用python基于**PySampleGUI**编写

* 接收RTT信息后能附带时间戳
* 不会自动清除数据框中的数据，是否清除以及什么时候清除将由自己决定
* 支持一键保存数据框中的所有数据
* 支持实时记录数据到文件
* 向上滚动鼠标滚动轮就能停止在当前界面。向下将滚动条滚到最低端就能实时看到当前接收到的数据
* 每次连接J-Link都会复位MCU
* 同步电脑时间到MCU
* 通过RTT-T发送自定义数据到MCU

---
### 软件更新说明
当前最新版本为v1.5，相比v1.3版本，有以下不同
* 修补了v1.3版本的bug

* 当软件内部出现异常时，能够将详细的异常信息输出到rtt-t.log中

![](https://github.com/liuhao1946/RTT-T-Project/blob/master/image/3.png)

---
### RTT-T功能演示

![](https://github.com/liuhao1946/RTT-T-Project/blob/master/image/1.gif)

---
### RTT-T的使用说明
* RTT-T自身打印出来的信息是开头带有LOG:xxx的字符串

* RTT-T使用的是**0数据通道**，这意味着MCU也必须使用SEGGER RTT的**0数据通道**

```c
SEGGER_RTT_printf(0,"test\n");
```

* 如果MCU端要获得到RTT-T的数据，有两个地方需要留意
1. 将MCU中RTT模块的接收缓存设置到合适的长度

2. MCU在程序中做如下轮训调用，以查询RTT发送过来的数据：
```c
#include "string.h"

uint8_t rtt_rx_data[33];

void str_to_int(char *p, int32_t *pv)
{
	uint8_t sign;
	char c;

	sign = *p;
	if (p[0] == '-' || p[0] == '+')
	{
		p++;
	}
	*pv = 0;
	while (*p >= '0' && *p <= '9')
	{
		c = *p++;
		*pv = *pv * 10 + (c-'0');
	}

	*pv = (sign != '-') ? *pv: -(*pv);
}

void timer_10ms(void )
{
   uint8_t len;
    
   len = SEGGER_RTT_Read(0, rtt_rx_data, 32);
   rtt_rx_data[len] = 0;
    
   if(len > 0)
   {
       char *p;
       char temp[6];
       uint8_t time[6];
       int32_t temp_dt;
       
       p = strstr(rtt_rx_data, "time syn:");
       //time syn:2022-01-16-16-27-30
       if(p != 0)
       {
           uint8_t i;

           p = p + 11;
           memset(temp,0,6);
           //字符串时间转换为整形，结果保存在time中
           for(i = 0; i < 6; i++)
           {
               memcpy(temp,p,2);
               str_to_int(temp, &temp_dt);
               time[i] = temp_dt;
               p += 3;
           }
           
       }

   }
}
```

* 如果需要同步电脑时间到MCU
1. 连接J-Llink

2. 在Text Data输入框中输入字符串指令"cmd:time syn"（软件默认）

3. 点击Send按钮，RTT-T会将如下字符串格式的电脑时间发送到MCU

   "time syn:2022-01-16-15-08-05"  

* 打开**实时数据保存**或者**保存数据框中的全部数据**时，RTT-T会自动在应用程序所在目录创建文件

  实时数据保存的文件名称：real_time_log_xxx(xxx为年月日时分秒)
  
  保存数据框中的全部数据文件名称：log_xxx(xxx为年月日时分秒)

* Rx Timeout参数的说明
  这个参数的含义是在RTT-T每次接收到一笔数据（≥1）后，RTT-T都会等待Rx Timeout（ms）。在Rx Timeout内接收到的数据RTT-T认为是一包数据。当超过Rx Timeout后，RTT-T就会为这包数据打上一个时间戳（如果时间戳打开的话）。这可以更好的辅助RTT-T在合适的数据位置打上时间戳。
  
  如果Rx Timeout = 0，表示RTT-T不使用超时机制，这可能造成的一个问题是时间戳的位置打的不准。
  
  **注：**
  **如果设置Rx Timeout，该值应该至少≥2（ms），推荐≥10（ms）**

* 如果需要源码，这里需要提醒一下

1. 软件依赖的主要的第三方库为：

    [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI)
  
    [pylink-square](https://github.com/square/pylink)
  
2. 源码中使用的PySimpleGUI版本为4.51.1。我在该版本中增加了获得数据框滚动条相对位置的函数（官方没有提供这个接口），因此你在安装了PySimpleGUI后，还需要在PySimpleGUI.py中增加下面代码（就放在set_vscroll_position()函数后面，这个函数是PySimpleGUI中存在的）
```python
    def get_vscroll_position(self):
        """
        Get the relative position of the scrollbar

        :return: (y1,y2)
        :rtype: tuple
        """
        try:
            return self.Widget.yview()
        except Exception as e:
            print('Warning get the vertical scroll (yview failed)')
            print(e)
            return None
```
---

### RTT-T的配置

由于配置选项一般不会变动，所以软件相关的可配置选项全部放在了**应用程序所在目录**下的**config.json**中。如需要修改配置，通过修改这个文件中相应的参数即可。具体如下：

**增加芯片型号**
* 打开官方J-Link RTT Viewer软件，找到你需要的芯片型号（比如，需要增加**nRF52840_xxAA**）

* 打开config.json文件，将芯片型号添加到"chip model"中

![](https://github.com/liuhao1946/RTT-T-Project/blob/master/image/2.gif)

**更换数据框中的字体**

打开config.json文件，将需要的字体放在"font"列表的第一项（类似添加nRF52840_xxAA）

**更换数据框中的字体大小**

打开config.json文件，修改"font size"中的数字，数字越大，字体越大

**修改软件启动时数据框的宽度，以兼容不同电脑屏幕尺寸**

打开config.json文件，修改"data window width"，默认是83，可以在此基础上增大或者减少

**注：修改config.json文件后保存，然后重启软件，新修改的参数才会生效**




