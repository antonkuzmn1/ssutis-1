from app.lab.lab1 import main as lab1
from app.lab.lab2 import main as lab2

def main(lab_num: int):
    match lab_num:
        case 1:
            lab1()
        case 2:
            lab2()