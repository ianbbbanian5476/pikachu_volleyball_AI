# PIKACHU VOLLEYBALL AI TRAINING
## Development Environment (開發環境)
### Package Version (套件版本)
以下環境版本為開發中使用的版本，可以在架構環境時作參考。
> [!NOTE]
> Environment packages may change as development progresses
```
Python             3.10.5
certifi            2023.7.22
charset-normalizer 3.2.0
cloudpickle        2.2.1
EasyProcess        1.1
entrypoint2        1.1
filelock           3.12.4
gym                0.26.2
gym-notices        0.0.8
idna               3.4
Jinja2             3.1.2
MarkupSafe         2.1.3
MouseInfo          0.1.3
mpmath             1.3.0
mss                9.0.1
networkx           3.1
numpy              1.25.2
opencv-python      4.8.0.76
Pillow             10.0.1
pip                23.2.1
PyAutoGUI          0.9.54
pygame             2.5.1
PyGetWindow        0.0.9
PyMsgBox           1.0.9
pyperclip          1.8.2
PyRect             0.2.0
pyscreenshot       3.1
PyScreeze          0.1.29
pytweening         1.0.7
requests           2.31.0
setuptools         68.2.0
sympy              1.12
torch              2.0.1
torchvision        0.15.2
typing_extensions  4.8.0
urllib3            2.0.5
wheel              0.41.2
```
### Installation of Virtualenv
1. Python 3.10.5
2. Install virtualenv
```
pip install virtualenv
```
3. build env
```
virtualenv myenv
```
4. Active env
> **Windows** 
```
.\venv\Scripts\myenv
```
> **MacOS** 
```
$ source ./venv/bin/myenv
```
## Development Progress
- [X] README
- [ ] complete AI training
## Q-learning
![](https://i.imgur.com/NUebRzl.png)
### expected reward(期望獎金)
價值函數公式 **Q<sub>k</sub>(a) = r(a<sub>1</sub>) + r(a<sub>2</sub>) + …… + r(a<sub>n</sub>) / n** 

寫成程式碼:
```python
def exp_reward(a,history):
    reward_a=history[a] #history[a]儲存了拉霸a每次獲得獎金的紀錄
    return sum(reward_a)/len(reward_a)
```
### 探索
> 【利用】 | 利用平均(期望)獎金找出最佳動作
> [!NOTE]
> 將每個動作帶入 Q<sub>k</sub>(a),去找出能達得到最大期望獎金的動作,此種作法不會建議未玩過的機台,只使用到利用策略,稱**貪婪法**
```python
def get_best_action(actions,history):
    best_action = 0
    max_action_value = 0
    for i in range(len(actions)):
        cur_action_value = exp_reward(actions[i],history) 
        if cur_action_value > max_action_value:
            best_action = i #若cur_action_value比較大，即更新索引best_action的值
            max_action_value = cur_action_value
    return best_action 
```
