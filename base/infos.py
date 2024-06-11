import torch
import os


def os_infos():
    print(" === OS name : {}".format(os.name))
    print(" === OS sep : {}".format(os.sep))
    print(" === OS path : {}".format(os.path))
    print(" === OS curdir: {}".format(os.curdir))
    print(" === OS cwd : {}".format(os.getcwd()))


def base_infos():
    print("PyTorch version is: {}".format(torch.__version__))
    print("you should know that cuda is available: {}, and version is : {}".format(torch.cuda.is_available(), torch.version.cuda))
    print("cuda device 0 is {}".format(torch.cuda.get_device_name(0)))
