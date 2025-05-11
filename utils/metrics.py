import numpy as np
from utils.ssnr import snrseg
import pesq
import pystoi
SAMPLE_RATE = 16000

def calc_snrseg(speech: np.ndarray, processed: np.ndarray) -> float:
    v = snrseg(clean_speech=speech, processed_speech=processed, fs=SAMPLE_RATE)
    if isinstance(v, np.float64):
        v = v.item()
    return v

def calc_pesq(speech: np.ndarray, processed: np.ndarray) -> float:
    return pesq.pesq(ref=speech, deg=processed, fs=SAMPLE_RATE)

def calc_stoi(speech: np.ndarray, processed: np.ndarray) -> float:
    v = pystoi.stoi(x=speech, y=processed, fs_sig=SAMPLE_RATE)
    if isinstance(v, np.float64):
        v = v.item()
    return v