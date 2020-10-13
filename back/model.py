import torch
from torch import nn

from models import cnnlstm_attention

def generate_model(opt, device):
	assert opt.model in [
		'cnnlstm'
	]

	if opt.model == 'cnnlstm':
		model = cnnlstm.Cnnlstm_attention(num_classes=opt.n_classes)
	return model.to(device)