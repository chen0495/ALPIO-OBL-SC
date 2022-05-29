本文实验主体文件为“PIO_反向学习_正余弦.ipynb”，请在对应环境下运行该文件  

## 介绍
  模糊Petri网(FPN)基于专家知识库模糊产生式规则对模糊或不精确的知识进行表述。但FPN模型中的参数（如权值、阈值和确信度）依赖专家知识和经验，因而存在参数精度难以保证、自适应能力较差、泛化能力弱等缺陷。而群智能优化算法则具有较强的自适应能力，能够基于一组初始参数进行参数自优化，因此将改进鸽群算法引入FPN的参数优化问题当中可以弥补FPN的上述缺陷，提高其推理结果的准确度，使FPN的性能在专家知识库等应用领域更加高效可靠。  
  本文提出一种基于反向学习策略和正弦余弦优化策略的改进鸽群算法（Adaptive Learning Pigeon-Inspired Optimization and Opposition-based Learining with Sine and Cosine,ALPIO-OBL-SC）对FPN参数进行优化。

## 实验结果展示
实验基于此FPN模型：  
![FPN模型](https://cdn.jsdelivr.net/gh/chen0495/newpicgo/img2022/202205291512884.png)  
测试函数收敛性测试对比结果：  
![收敛性测试对比](https://cdn.jsdelivr.net/gh/chen0495/newpicgo/img2022/202205291510210.png)  
FPN收敛性测试对比结果：  
![](https://cdn.jsdelivr.net/gh/chen0495/newpicgo/img2022/202205291514421.png)  

## 实验环境
实验环境：
 - Intel(R) Core(TM) i7-8550U CPU@1.80GHz 
 - win10 Pro操作系统
 - 16G内存
 - Python3.8
 - Jupyter Notebook 6.4.10  

## 目录结构
- PIO鸽群优化算法
	- Function.py `测试函数包`
	- main.py `标准鸽群算法入口，已废弃`
	- PIO.py `标准鸽群算法主体，已废弃`
	- PIO_WOA.ipynb `PIO、ALPIO-OBL-SC、WOA三类算法对比展示，jupyter notebook`
	- PIO_反向学习_正余弦.ipynb `PIO、ALPIO-OBL-SC两类算法对比展示，jupyter notebook`
	- ReadMe.txt `说明文件.txt`
	- README.md `说明文件.md`
	- 改进鲸鱼算法.ipynb `WOA算法展示`
	
