import numpy as np
import h5py
import gdown
from os import listdir

import torch
from torch.autograd import Variable
from torch.utils.data import Dataset

DATA_DIR = 'data'
DATA_FILE_BASE = 'ply_data_train'
DATA_FILE_EXT = '.h5'

class FromNpDataset(Dataset):
    def __init__(self, np_data, transform=None):
        self.data = np_data
        self.transform = transform

    def __len__(self):
        return self.data.shape[0]

    def __getitem__(self, idx):
        sample = self.data[idx]
        if self.transform:
            sample = self.transform(sample)
        return Variable(torch.from_numpy(sample))

class ModelnetDataset(FromNpDataset):

    DATA_URLS = [
        'https://drive.google.com/uc?export=download&id=1MNgxTzGCw5By8a9aNLi7pYjcuEoRUxsR',
        'https://drive.google.com/uc?export=download&id=1co-dX33hgpDk7vUDYS-n-oOWJHSuLBkq',
        'https://drive.google.com/uc?export=download&id=1VDqD4PdqGdbfsOKdQAc4zZTsH4a1Nyqo',
        'https://drive.google.com/uc?export=download&id=1N5DlhvDQ1IkdMlpIDaKtZXqGu12ULG4F',
        'https://drive.google.com/uc?export=download&id=1UlcrapAbSBRDhCNVsuPMEaEAcvDXxOLY',
    ]

    def __init__(self, transform=None):
        for idx, url in enumerate(data_urls):
            file_path = os.path.join(DATA_DIR, DATA_FILE_BASE+str(idx)+DATA_FILE_EXT)
            if not os.path.exists(file_path):
                gdown.download(url, file_path, quiet=False)

        data_list = []
        h5_files = [ f for f in listdir(DATA_DIR)
                        if os.path.isfile(os.path.join(DATA_DIR, f))
                        if os.path.splitext(f)[1] == DATA_FILE_EXT ]
        for f in h5_files:
            hf = h5py.File(os.path.join(DATA_DIR, f), 'r')
            data_list.append(hf.get('data'))

        data = np.transpose(np.concatenate(train_list, axis=0), (0, 2, 1))

        super(self, data, trasnform=transform)
